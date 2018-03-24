# Fourier analysis of Amplitude Modulation

import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt

class TimeFrequency():
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.time = np.arange(self.start, self.stop, self.step)
        self.freq = fourier.fftfreq(self.time.size, 0.1)

    def time_array(self):
        return self.time

    def frequencies(self):
        return self.freq

class Filter(object):
    def __init__(self, cutoff):
        self.cutoff_frequency = cutoff
        
    def LPF(self):
        time = TimeFrequency(-1000, 1000, 0.1)
        return np.sinc(6.28*self.cutoff_frequency*time.time_array())

class dsbsc(object):
    def __init__(self, message_signal, carrier_frequency, time_scale_tuple):
        self.m = message_signal
        self.cf = carrier_frequency
        self.tf = TimeFrequency(time_scale_tuple[0], time_scale_tuple[1], time_scale_tuple[2])
        self.t = self.tf.time_array()
        self.freq = self.tf.frequencies()

    def generate_carrier(self):
        return np.cos(6.28*self.cf*self.t)

    def modulate(self):
        return self.generate_carrier()*self.m

    def receiver_multiplier(self):
        return self.modulate()*(2*self.generate_carrier())

    def demodulate(self, lpf_cutoff=0.1):

        # initiate a lowpass filter
        filter_object = Filter(lpf_cutoff)
        LPF_filter = filter_object.LPF()

        # generate the fourier transform of the lowpass filter
        lpf_ft = fourier.fft(LPF_filter)

        # generate the fourier transform of the receiver multiplier
        receiver_multiplier_fft = fourier.fft(self.receiver_multiplier())

        # multiply the fourier transforms to generate the output's fourier transform
        # in time domain, it the signals should be convolved.
        output_transform = lpf_ft*receiver_multiplier_fft

        # take the inverse fourier transform to generate the output in time domain.
        demodulated_signal = fourier.ifft(output_transform)

        return demodulated_signal

    def spectral_magnitude_plot(self, title, *args):
        for i in args:
            plt.plot(self.freq, np.abs(fourier.fft(i)))
        plt.title(title)
        plt.show()

    def time_plot(self, title, *args):
        for i in args:
            plt.plot(self.t, i)
        plt.title(title)
        plt.show()


def test_script():
    time = (-1000, 1000, 0.1)
    t = np.arange(-1000, 1000, 0.1)
    m = np.sin(6.28*20*t)

    scheme = dsbsc(m, 1000, time)
    multiplier = scheme.receiver_multiplier()

    # dsbsc modulated time plot
    scheme.time_plot("DSBSC Modulated Signal in time domain", scheme.modulate())
    # dsbsc modulated frequncy plot
    scheme.spectral_magnitude_plot("DSBSC Modulated Signal's FFT", scheme.modulate())

    # dsbsc receiver multiplier time plot.
    scheme.time_plot("Input to Lowpass Filter", multiplier)
    # dsbsc receiver multiplier frequency output.
    scheme.spectral_magnitude_plot("FFT of Lowpass Filter's input", multiplier)

    # lpf filter in time domain
    scheme.time_plot("Sinc Filter (Lowpass Filter) in time domain", Filter(0.1).LPF())
    # lpf filter frequency output
    scheme.spectral_magnitude_plot("Sinc Filter FFT", Filter(0.1).LPF())

    # demodulated signal in time domain
    scheme.time_plot("Message and Demodulated Signal", m, scheme.demodulate(0.1)/16.0)
    # demodulated signal frequency ouptut
    demodulated = scheme.demodulate(0.1)
    scheme.spectral_magnitude_plot("Demodulated Signal FFT", demodulated)

