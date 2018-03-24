# Double Side Band - Supressed Carrier Modulation Scheme

## DSB-SC 
Similar to Amplitude modulation but not carrying the carrier information, the DSBSC modulation scheme is good if you have the carrier information at the receiver end.
If carrier information is available, then a coherent detector can demodulate the receieved signal. A coherent detector consists of a multiplier and a lowpass filter.
A multiplier uses the same carrier which was used at the transmitter end to multiply it with the receieved signal. The envelope of the multiplier's output is the message signal. But the multiplier's output
contains twice the carrier frequency components and that is why a lowpass filter is used, which removes them and throws the envelope or the message signal as the output.

## Sample Run
This script has an in-built test function to show how this script runs.

### The signal is modulated using a carrier as 1000 Hz
The message signal has 10 Hz frequency.
![Modulated Signal](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/DSBSC%20Modulated%20in%20time%20domain.jpeg)
