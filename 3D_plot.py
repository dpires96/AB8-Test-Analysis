from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import statistics

#Data given
data=pd.read_csv('Spanwisetest4.csv')

#Experimental data
datablue=pd.read_csv('blueData.csv')
datared=pd.read_csv('redData.csv')

#CT Data
blueCT_data=pd.read_csv('blueDataCT.csv')
blackCT_data=pd.read_csv('blackDataCT.csv')
redCT_data=pd.read_csv('redDataCT.csv')

#Experimental data storage
span_data_blue=[]
correlation_blue=[]
for i in range(13):
    span_data_blue.append(datablue.loc[i][0])
    correlation_blue.append(datablue.loc[i][1])

span_data_red=[]
correlation_red=[]
for i in range(8):
    span_data_red.append(datared.loc[i][0])
    correlation_red.append(datared.loc[i][1])

#CT data storage
span_data_CT_red_coarse=[]
correlation_CT_red_coarse=[]
span_data_CT_blue_medium=[]
correlation_CT_blue_medium=[]
span_data_CT_black_fine=[]
correlation_CT_black_fine=[]
for i in range(65):
    span_data_CT_red_coarse.append(redCT_data.loc[i][0])
    correlation_CT_red_coarse.append(redCT_data.loc[i][1])
for i in range(83):
    span_data_CT_blue_medium.append(blueCT_data.loc[i][0])
    correlation_CT_blue_medium.append(blueCT_data.loc[i][1])
for i in range(65):
    span_data_CT_black_fine.append(blackCT_data.loc[i][0])
    correlation_CT_black_fine.append(blackCT_data.loc[i][1])

#Given data storage
span_data=[]
time_data=[]
pressure_data=np.zeros([200,720])
for i in range(200):
    span_data.append(data.loc[i+1][0])

for i in range(720):
    time_data.append(data.loc[0][i+1])

for i in range(200):
    for j in range(720):
        pressure_data[i,j]=data.loc[i+1][j+1]

#Average finding
averageOfPos=[]
for i in range(200):
    averageOfPos.append(np.average(pressure_data[:,i]))

#Correlation coefficient process
correlationTest=[]
correlationCoefTest=np.corrcoef(pressure_data, rowvar=True)
finalCorrelation=[]
#print(correlationCoefTest[:,99])
scalingCoef=0.15660133/7.0
spanTest=[]
for i in range(200):
    spanTest.append(span_data[i] -  (1.06 / 7) * span_data[i])
    finalCorrelation.append(correlationCoefTest[i][99]-scalingCoef*span_data[i])
    #finalCorrelation.append(np.corrcoef)


#Scaling coefficient
coef100=74.71029758
coef0=26.79919337

#(statistics.stdev(pressure_data[0])*statistics.stdev(pressure_data[i]))
#Correlation process from correlation coeficients
for i in range(200):
    correlationTest.append(np.correlate(pressure_data[i], pressure_data[0])*(10**(-9))/statistics.stdev(pressure_data[0])*statistics.stdev(pressure_data[i])/1.35200046)
    #correlationTest.append(np.corrcoef(pressure_data[i], pressure_data[0])[1,0])
    #correlationTest.append(np.correlate(pressure_data[0], pressure_data[i])/(statistics.stdev(pressure_data[0])*statistics.stdev(pressure_data[i])))
#print(np.correlate(pressure_data[0], pressure_data[0])*(10**(-9))/statistics.stdev(pressure_data[0])*statistics.stdev(pressure_data[0]))
#print(np.correlate(pressure_data[100], pressure_data[0])*(10**(-9))/statistics.stdev(pressure_data[100])*statistics.stdev(pressure_data[0]))
#print(np.correlate(pressure_data[199], pressure_data[0])*(10**(-9))/statistics.stdev(pressure_data[199])*statistics.stdev(pressure_data[0]))

#Plot properties
plt.style.use(["ggplot"])
plt.figure(figsize=(16,9))
plt.ylim(bottom=0, top=1)
plt.xlim(left=0, right=8)
plt.xlabel('Z/D',fontsize=18)
plt.ylabel('R',fontsize=18)
plt.tick_params(labelsize=18)


#Experimental data plot
plt.scatter(span_data_blue,correlation_blue,s=100,color="blue",marker='x', label='Casalino et.al.,Exp. (Re_D=22000), [7]')
plt.scatter(span_data_red,correlation_red,s=100,color="red",label='Szepessy & Bearman, Exp. (Re_D=43000), [6]')

#CT data plot
#plt.plot(span_data_CT_black_fine,correlation_CT_black_fine,color='green', label='CT fine')
plt.plot(span_data_CT_blue_medium,correlation_CT_blue_medium,linewidth=3, color='purple', label='Teruna, C. et al., medium, [4]')
plt.plot(span_data_CT_red_coarse, correlation_CT_red_coarse,linewidth=3, color='cyan', label='Teruna,C. et al., coarse, [1]')

#Our data plot
plt.plot(spanTest,finalCorrelation,linewidth=5,color='black', label='Given Data (Re_D=47800)')

#Plotting trigger
plt.legend()
plt.savefig('span_correlation.pdf', dpi=300)
plt.show()

breakpoint()


pressure_data_test=pressure_data/pressure_data[100,:]
#print(time_data[179], time_data[359], time_data[539], time_data[719])
plt.subplot(5,1,1)
plt.gca().set_title('P/P_0 vs l/l_0 @ t=0.0000s')
plt.plot(span_data,pressure_data_test[:,0])
plt.xlabel('l/l_0')
plt.ylabel('P/P_0')
plt.subplot(5,1,2)
plt.gca().set_title('P/P_0 vs l/l_0 @ t=0.0085s')
plt.plot(span_data,pressure_data_test[:,179])
plt.xlabel('l/l_0')
plt.ylabel('P/P_0')
plt.subplot(5,1,3)
plt.gca().set_title('P/P_0 vs l/l_0 @ t=0.0171s')
plt.plot(span_data,pressure_data_test[:,359])
plt.xlabel('l/l_0')
plt.ylabel('P/P_0')
plt.subplot(5,1,4)
plt.gca().set_title('P/P_0 vs l/l_0 @ t=0.0257s')
plt.plot(span_data,pressure_data_test[:,539])
plt.xlabel('l/l_0')
plt.ylabel('P/P_0')
plt.subplot(5,1,5)
plt.gca().set_title('P/P_0 vs l/l_0 @ t=0.0343s')
plt.plot(span_data,pressure_data_test[:,719])
plt.xlabel('l/l_0')
plt.ylabel('P/P_0')

plt.show()


plt.subplot(5,2,1)
plt.gca().set_title('P/P_0 vs t @ 0 l/l_0')
plt.plot(time_data,pressure_data_test[0],color='r',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,2)
plt.gca().set_title('P/P_0 vs t @ 1 l/l_0')
plt.plot(time_data,pressure_data_test[199],color='b',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,3)
plt.gca().set_title('P/P_0 vs t @ 0.1 l/l_0')
plt.plot(time_data,pressure_data_test[19],color='r',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,4)
plt.gca().set_title('P/P_0 vs t @ 0.9 l/l_0')
plt.plot(time_data,pressure_data_test[179],color='b',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,5)
plt.gca().set_title('P/P_0 vs t @ 0.2 l/l_0')
plt.plot(time_data,pressure_data_test[39],color='r',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,6)
plt.gca().set_title('P/P_0 vs t @ 0.8 l/l_0')
plt.plot(time_data,pressure_data_test[159],color='b',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,7)
plt.gca().set_title('P/P_0 vs t @ 0.3 l/l_0')
plt.plot(time_data,pressure_data_test[59],color='r',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,8)
plt.gca().set_title('P/P_0 vs t @ 0.7 l/l_0')
plt.plot(time_data,pressure_data_test[139],color='b',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,9)
plt.gca().set_title('P/P_0 vs t @ 0.4 l/l_0')
plt.plot(time_data,pressure_data_test[79],color='r',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')
plt.subplot(5,2,10)
plt.gca().set_title('P/P_0 vs t @ 0.6 l/l_0')
plt.plot(time_data,pressure_data_test[119],color='b',linewidth=0.5)
plt.xlabel('t [s]')
plt.ylabel('P/P_0')

new_span_data=[]
for i in range(200):
    for j in range(720):
        new_span_data.append(span_data[i])

new_time_data=[]
for i in range(200):
    for j in range(720):
        new_time_data.append(time_data[j])

new_pressure_data=[]
for i in range(200):
    for j in range(720):
        new_pressure_data.append(pressure_data[i][j])

x = np.reshape(new_span_data, (200, 720))
y = np.reshape(new_time_data, (200, 720))
z = np.reshape(new_pressure_data, (200, 720))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('Spanwise Position')
ax.set_ylabel('Time [s]')
ax.set_zlabel('Pressure [Pa]')



# Plot the surface.
surf = ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=10, antialiased=True)

#surf = ax.plot_wireframe(x, y, z,rstride=10, cstride=10)
# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()