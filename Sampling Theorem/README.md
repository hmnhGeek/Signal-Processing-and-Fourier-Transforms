# Sampling 

## Introduction
When we take discrete samples of a continuous time signal, then that process is called sampling. Theoretically speaking, we are losing most of the information but if sampling theorem is followed then practically, the signal can be generated back from the samples.

## Sampler
Here the working of sampler.py file is shown. I am using numpy sinc signal here centered at time space 0.5 seconds. It is possible to work with another signal. Just open the file and edit the function named functionGenerator with the desired numpy signal.

### Display the Signal
Generating the signal with 1 Hz frequency.

```
python3.5 sampler.py --signal --staticframe -f 1
```

### Sample the Signal at 20, 50, 100 and 1000 Hz

```
python3.5 sampler.py  --staticframe -f 1 --fs 20
python3.5 sampler.py  --staticframe -f 1 --fs 50
python3.5 sampler.py  --staticframe -f 1 --fs 100
python3.5 sampler.py  --staticframe -f 1 --fs 1000
```

### Display the sampled signal only at 100 Hz

```
python3.5 sampler.py  -f 1 --fs 100 --staticframe --showsampleonly
```

### Run an animation for Sampling frequency from 1 Hz to 500 Hz

```
python3.5 sampler.py  -f 1 --fs 500 -t 0.01
```
where 't' is for the transition time of animation and has nothing to do with the signal or samples.

## Author
Himanshu Sharma