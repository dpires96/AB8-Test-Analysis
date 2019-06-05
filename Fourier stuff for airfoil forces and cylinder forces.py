import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from scipy.fftpack import fft
from scipy.fftpack import fftfreq
from scipy import signal


#Airfoil forces
var = np.genfromtxt("Airfoilforces2.txt", dtype=str, skip_footer=720)
data = np.genfromtxt("Airfoilforces2.txt", skip_header=1)

Time = data[:,4]
angle = np.deg2rad(20)

Force_x = data[:,1]*np.cos(angle)-data[:,2]*np.sin(angle)
Force_x = Force_x-np.average(Force_x)
Force_y = data[:,1]*np.sin(angle)+data[:,2]*np.cos(angle)
Force_y = Force_y-np.average(Force_y)
#Force_z = data[:,3]


#xx = plt.psd(Force_x, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "blue", return_line = "True" )

#yy = plt.psd(Force_y, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "red", return_line = "True")


fx, Pxx_den = signal.welch(Force_x, fs=1/0.0000476416*((7/1000)/100), window='hann', nperseg=300, noverlap=None,
             nfft=None, detrend='constant', return_onesided=True,
             scaling='density', axis=-1)


fy, Pyy_den = signal.welch(Force_y, fs=1/0.0000476416*((7/1000)/100), window='hann', nperseg=300, noverlap=None,
             nfft=None, detrend='constant', return_onesided=True,
             scaling='density', axis=-1)

"""
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)
plt.subplot(221)
plt.psd(Force_x, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Red", return_line = "True")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]')
plt.ylabel('PSD [dB/Hz]')  
plt.title('PSD graph for airfoil forces in x-direction')
"""


plt.subplot(111)
plt.semilogy(fx, Pxx_den, color='Red')
plt.axhline(10**0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]', fontsize=18)
plt.ylabel('PSD [$V^2$/Hz]', fontsize=18)  
plt.title('Smoothed PSD graph for airfoil forces in x-direction', fontsize=24)
plt.show()

"""
plt.subplot(222)
plt.psd(Force_y, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Blue", return_line = "True")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]')
plt.ylabel('PSD [dB/Hz]')  
plt.title('PSD graph for airfoil forces in y-direction')
"""


plt.subplot(111)
plt.semilogy(fy, Pyy_den, color='Blue')
plt.axhline(10**0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]', fontsize=18)
plt.ylabel('PSD [$V^2$/Hz]', fontsize=18)  
plt.title('Smoothed PSD graph for airfoil forces in y-direction', fontsize=24)
plt.show()





#Cylinder forces
var2 = np.genfromtxt("Cylinderforces.txt", dtype=str, skip_footer=722)
data2 = np.genfromtxt("Cylinderforces.txt", skip_header=1)

Frame_number2 = data2[:,0]
Force_x2 = data2[:,1]*np.cos(angle)-data2[:,2]*np.sin(angle)
Force_x2 = Force_x2-np.average(Force_x2)
Force_y2 = data2[:,1]*np.sin(angle)+data2[:,2]*np.cos(angle)
Force_y2 = Force_y2-np.average(Force_y2)
#Force_z2 = data2[:,3]

#xx2 = plt.psd(Force_x2, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Orange", return_line = "True")


#yy2 = plt.psd(Force_y2, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Green", return_line = "True")


fx2, Pxx_den2 = signal.welch(Force_x2, fs=1/0.0000476416*((7/1000)/100), window='hann', nperseg=300, noverlap=None,
             nfft=None, detrend='constant', return_onesided=True,
             scaling='density', axis=-1)


fy2, Pyy_den2 = signal.welch(Force_y2, fs=1/0.0000476416*((7/1000)/100), window='hann', nperseg=300, noverlap=None,
             nfft=None, detrend='constant', return_onesided=True,
             scaling='density', axis=-1)

"""
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)
plt.subplot(221)
plt.psd(Force_x2, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Orange", return_line = "True")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]')
plt.ylabel('Power Spectral Density [dB/Hz]')  
plt.title('PSD graph for cylinder forces in x-direction')
"""


plt.subplot(111)
plt.semilogy(fx2, Pxx_den2, color='Orange')
plt.axhline(10**0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]', fontsize=18)
plt.ylabel('PSD [$V^2$/Hz]', fontsize=18)  
plt.title('Smoothed PSD graph for cylinder forces in x-direction', fontsize=24)
plt.show()

"""
plt.subplot(222)
plt.psd(Force_y2, NFFT=2**10, Fs = 1/0.0000476416*((7/1000)/100), color = "Green", return_line = "True")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]')
plt.ylabel('Power Spectral Density [dB/Hz]')  
plt.title('PSD graph for cylinder forces in y-direction')
"""


plt.subplot(111)
plt.semilogy(fy2, Pyy_den2, color='Green')
plt.axhline(10**0, color='black')
plt.axvline(0, color='black')
plt.xlabel('$St_{d}$ [-]', fontsize=18)
plt.ylabel('PSD [$V^2$/Hz]', fontsize=18)  
plt.title('Smoothed PSD graph for cylinder forces in y-direction', fontsize=24)
plt.show()

