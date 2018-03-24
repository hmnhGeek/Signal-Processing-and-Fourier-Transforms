import matplotlib.pyplot as plt
import numpy as np

message_freq = 50
carrier_freq = 1000
t = np.arange(0, 50, 0.1)
message = np.sin(6.28*message_freq*t)

class AmplitudeModem:
    def modulate(self, message, fc):
        c = np.cos(6.28*fc*t)

        mod = message*c
        return mod

    def demodulate(self, received_array, fc, fm):
        c = np.cos(6.28*fc*t)

        demod = c*received_array
        baseband = demod
        return baseband

modulated = AmplitudeModem().modulate(message, carrier_freq)
demodulated = AmplitudeModem().demodulate(modulated, carrier_freq, message_freq)

fig = plt.figure()

ax = fig.add_subplot(131)
plt.plot(t, modulated, color = "green", label = "Carrier")
plt.plot(t, message, color="black", label = "Message Signal")
plt.xlabel("Time --->")
plt.ylabel("Amplitude --->")
plt.title("Carrier Wave at {} Hz".format(carrier_freq))
plt.grid(color = "orange")
plt.legend()

ax1 = fig.add_subplot(132)
plt.plot(t, demodulated, color = 'red', label = "Multiplier Output")
plt.plot(t, message, color = 'black', label = "Message Signal")
plt.xlabel("Time --->")
plt.ylabel("Amplitude --->")
plt.title("Demodulated Signal (Envelope)")
plt.legend()
plt.grid(color ="orange")

ax2 = fig.add_subplot(133)
plt.plot(t, message, color = 'black')
plt.xlabel("Time --->")
plt.ylabel("Amplitude --->")
plt.title("LPF Output")

plt.grid(color="orange")
plt.show()
