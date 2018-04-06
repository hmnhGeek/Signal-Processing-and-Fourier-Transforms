from __future__ import division
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation
import time
plt.rcParams['axes.facecolor'] = 'black'

# Tunable Parameters
f = 5
max_sampling_freq = 200
transition_time = 0.01 #seconds

def functionGenerator(time_array):
	return np.sinc(2*np.pi*f*time_array)**3 + np.sin(2*np.pi*f*time_array)*np.cos(2*np.pi*f*time_array)**2
#----------------------------

fs = range(1, max_sampling_freq+1)

for i in range(len(fs)):
	t = np.arange(-1/f, 1+ 1/f, 1/fs[i])
	tor = np.arange(-1/f, 1+ 1/f, 0.001)
	sig = functionGenerator(tor)
	signal = functionGenerator(t)
	plt.pause(transition_time)
	plt.cla()
	plt.grid(linestyle='dotted')
	plt.title("Sampling at "+str(fs[i])+" Hz")
	plt.plot(t, signal, marker='o', color="b", label = "CH2: Sampled Signal")
	plt.xlabel("Time ($t$) in seconds")
	plt.plot(tor, sig, color='yellow', label="CH1: Orignal Signal")
	legend = plt.legend()
	plt.setp(legend.get_texts(), color='w')

plt.plot(t, signal, color='b')
plt.show()
