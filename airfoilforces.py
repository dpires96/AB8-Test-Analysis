import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
plt.style.use(["ggplot"])

data = np.genfromtxt("airfoil_forces.csv",delimiter=",",skip_header=1)
time = data[:,0]      #frames
x = data[:,1]         #N
y = data[:,2]         #N
z = data[:,3]         #N
V = 100               #m/s
t_s =512*0.00000009305#s
f_s = t_s**(-1)     
f_max = f_s/2
L = 39.7*10**(-3)              #mm
##window = np.hanning(len(x))
##freq_frames = np.fft.rfftfreq(len(time))
##freq = freq_frames/t_s
##
##windowedx = [window[i] * x[i] for i in range(len(x))]
##fftx = np.fft.rfft(windowedx)
##fftxamplitudes = abs(fftx)/len(x)
##windowedy = [window[i] * y[i] for i in range(len(x))]
##ffty = np.fft.rfft(windowedy)
##fftyamplitudes = abs(ffty)/len(x)
##
##windowedz = [window[i] * z[i] for i in range(len(x))]
##fftz = np.fft.rfft(windowedz)
##fftzamplitudes = abs(fftz)/len(x)


f,fftywelch = signal.welch(y, fs=f_s, window='hann', nperseg=256, noverlap=128)
stro = f*L/V
##plt.plot(freq,fftxamplitudes)
##plt.plot(freq,fftyamplitudes)
##plt.plot(freq,fftzamplitudes)
##plt.plot(f,fftywelch, "r")
plt.semilogy(f, fftywelch)
plt.ylabel("PSD [N^2/Hz]")
plt.xlabel('Frequency [Hz]')
plt.show()

