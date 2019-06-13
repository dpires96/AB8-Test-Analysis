import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from sklearn.cluster import KMeans
from scipy.fftpack import fft
from scipy.fftpack import fftfreq
import matlab as mlab

from matplotlib.mlab import psd
df = pd.read_excel('FFT_dipole.xlsx', sheet_name=0)



time = df['Unnamed: 0']
p_up = df['3D above the cylinder ']
p_behind = df['3D behind the cylinder ']

t = time[1:]
p0 = (20*10**(-6))**2
p_u = np.array(p_up[1:])
p_b = np.array(p_behind[1:])
#print(max(p_b))

xx = psd(p_b, NFFT=2**10, Fs = 1/0.0000476416, scale_by_freq = False)
yy = psd(p_u, NFFT=2**10, Fs = 1/0.0000476416, scale_by_freq = False)
#f = fft(p_b)
#print(f)
# label='Behind the cylinder' label='Above the cylinder'
xxp = xx[0]
yyp = yy[0]
xxfreq = xx[1]*0.007/100
yyfreq = yy[1]*0.007/100

for i, px in enumerate(xxp):
    xxp[i] = 10*(np.log10(px/p0))

for j,py in enumerate(yyp):
    yyp[j] = 10*(np.log10(py/p0))
#N = 720
#g = fftfreq(N)
#x = np.linspace(0,1,N-1)
plt.plot(xxfreq, xxp, color = "red", label = "Behind the cylinder")
plt.plot(yyfreq, yyp, color = "mediumblue", label = "Above the cylinder")
#plt.plot(x,np.imag(f[1:]))
plt.legend(loc='upper right')
plt.ylabel('Power Spectral Density [dB]')
plt.xlabel('Strouhal Number [-]')
plt.show()









