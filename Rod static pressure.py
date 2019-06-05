import numpy as np
import matplotlib.pyplot as plt
plt.style.use(["ggplot"])
var = np.genfromtxt("SurfaceTimeGraph.txt", dtype=str, skip_footer=308)
data = np.genfromtxt("SurfaceTimeGraph.txt", skip_header=1)


min_x = np.argmin(data[:,0])
positionx = data[:,0]-0.366865873336792-0.0035
angle = np.zeros(len(positionx))

for i in range(min_x):
    angle[i] = np.arccos(positionx[i]/0.0035)*180/np.pi -160

for i in range(min_x,len(positionx)):
    angle[i] = -1*np.arccos(positionx[i]/0.0035)*180/np.pi +200
 

P_static_up = data[:,1]
P_static_down = data[:,2]

U = 100 #m/s
rho = 1.223
P_freestream = 105000

cp_up = (P_static_up - P_freestream)/(0.5*rho*U**2)
cp_low = (P_static_down - P_freestream)/(0.5*rho*U**2)
cp_ave = (cp_up+cp_low)/2

#plt.plot(angle, cp_up, color='red', label='$Cp_{up}$')
#plt.plot(angle, cp_low, color = 'blue', label='$Cp_{low}$')
plt.plot(angle, cp_ave, color = 'black', label='Experiment (Re=$4.8*10^4$)')


dataref2 = np.genfromtxt("cp_rod_from_reference2.txt", skip_header=3)

xref2 = dataref2[:,0]
yref2 = dataref2[:,1]

plt.plot(xref2, yref2, color='red', linestyle='--', label='Boudet et. al. (LES) (Re=$4.8*10^4$)')


dataref3 = np.genfromtxt("cp_rod_from_reference3.txt", skip_header=3)

xref3 = dataref3[:,0]
yref3 = dataref3[:,1]


plt.plot(xref3, yref3, color='blue', linestyle='--', label='Jiang et. al. (LES) (Re=$4.8*10^4$)')

plt.grid(True)
plt.xlabel("Position [deg]", fontsize=14)
plt.ylabel("$Cp [-]$", fontsize=14)
plt.legend(loc='upper right', prop={'size': 10})
plt.show()









