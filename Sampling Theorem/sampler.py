from __future__ import division
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation
import time
import argparse as ap 
plt.rcParams['axes.facecolor'] = 'black'

parser = ap.ArgumentParser()
parser.add_argument("-f", type = float, help="Signal Frequency in Hz.", default=5)
parser.add_argument("--fs", type = int, help = "Sampling Frequency in Hz.", default = 100)
parser.add_argument("-t", type = float, help="Animation Transition time.", default = 0.01, nargs='?')
parser.add_argument("--staticframe", action="store_true", help="Display static graph.")
parser.add_argument("--showsampleonly", action="store_true", help="Display sampled signal only.")
parser.add_argument("--signal", action="store_true", help="Display the signal only.")
args = parser.parse_args()

# Tunable Parameters
f = args.f
max_sampling_freq = args.fs
transition_time = args.t #seconds

def functionGenerator(time_array):
	return np.sinc(2*np.pi*f*(time_array-0.5))
#----------------------------

def animation():
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
		if not args.signal:
			plt.plot(t, signal, marker='o', color="white", label = "CH2: Sampled Signal")
		plt.xlabel("Time ($t$) in seconds")
		if not args.showsampleonly:
			plt.plot(tor, sig, color='yellow', label="CH1: Orignal Signal")
		legend = plt.legend()
		plt.setp(legend.get_texts(), color='w')

	plt.plot(t, signal, color='white')
	plt.show()

def static():
	t = np.arange(-1/f, 1+ 1/f, 1/max_sampling_freq)
	tor = np.arange(-1/f, 1+ 1/f, 0.001)
	sig = functionGenerator(tor)
	signal = functionGenerator(t)
	plt.grid(linestyle='dotted')
	
	if not args.signal:
		plt.title("Sampling at "+str(max_sampling_freq)+" Hz")
		plt.plot(t, signal, marker='o', color="white", label = "CH2: Sampled Signal")
	plt.xlabel("Time ($t$) in seconds")
	if not args.showsampleonly:
		plt.plot(tor, sig, color='yellow', label="CH1: Orignal Signal")
	legend = plt.legend()
	plt.setp(legend.get_texts(), color='w')
	if not args.signal:
		plt.plot(t, signal, color='white')
	plt.show()

if args.staticframe:
	static()
else:
	animation()