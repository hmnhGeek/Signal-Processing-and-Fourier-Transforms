# Double Side Band - Supressed Carrier Modulation Scheme

## DSB-SC 
Similar to amplitude modulation but not carrying the carrier information, the DSBSC modulation scheme is good if you have the carrier information at the receiver end.
If carrier information is available, then a coherent detector can demodulate the receieved signal. A coherent detector consists of a multiplier and a lowpass filter.
A multiplier uses the same carrier which was used at the transmitter end to multiply it with the receieved signal. The envelope of the multiplier's output is the message signal. But the multiplier's output
contains twice the carrier frequency components and that is why a lowpass filter is used, which removes them and throws the envelope or the message signal as the output.

## Sample Run
This script has an in-built test function to show how the DSB-SC modulation scheme works.

### The signal is modulated using a carrier at 1000 Hz and received at the receiver
The message signal has 10 Hz frequency.

#### Time domain
![Modulated Signal](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/DSBSC%20Modulated%20in%20time%20domain.jpeg)
#### Frequency domain
![Frequency domain](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/DSBSC%20mod%20signal%20fft.jpg)

### Then the signal is multiplied by the same carrier
#### Time domain
![Multiplied Signal](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/input%20to%20lpf.jpg)
#### Frequency domain
![Frequency domain](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/input%20lpf%20fft.jpg)

### The Lowpass Filter or Sinc Filter
#### Time domain
![Sinc Filter](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/sinc%20filter.jpg)
#### Frequency domain
![Frequency domain](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/sinc%20filter%20fft.jpg)

### The Sinc filter removes the high frequency content and the message signal is received
The green signal is the demodulated signal with some phase shift. Blue signal is the original message signal.
#### Time domain
![Message Signal](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/demodulated.jpg)
#### Frequency domain
![Frequency domain](https://github.com/hmnhGeek/Signal-Processing-and-Fourier-Transforms/blob/master/DSBS%20Modulation%20Scheme%20using%20Sinc%20Filter/Sample%20Images/demodulated%20fft.jpg)
