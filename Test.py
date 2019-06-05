# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:59:54 2019

@author: nduursma
"""

from Velocity_loc2 import *
import numpy as np
from matplotlib import pyplot as plt






#steps between pictures
step = 5
step2 = 5
step3 = 5

q2 = 15 #pixels analyzed per picture 

x = np.arange(0,15*q)
x2 = np.arange(0,q2)

Vavglst = np.zeros(q*15)
Vmaxlst = np.zeros(q2)
Vminlst = np.linspace(10000,10001, q2)


#Plot all velocity lines
for j in np.arange(0,678,step):
    pixelsimageplot = pixelsimages(j)
    Vlstx1 = Vlstx(pixelsimageplot)
 
    if j <=100:
        colourhex = rgb_to_hex((255-j,200,20))    #YELLOW
    elif j > 100 and j <=200:
        colourhex = rgb_to_hex((j-100,100,0))   #GREEN
    elif j > 200 and j <=300:
        colourhex = rgb_to_hex((j-200,100,150))    #BLUE
    elif j > 300 and j <=400:
        colourhex = rgb_to_hex((j-300,0,80))   #PURPLE
    elif j > 400 and j <=500:
        colourhex = rgb_to_hex((j-280,80,150))   #PINK
    elif j > 500 and j <=600:
        colourhex = rgb_to_hex((j-400,0,0))   #RED
    elif j > 600 and j <=700:
        colourhex = rgb_to_hex((j-445,110,0))   #ORANGE
    else: 
        colourhex = rgb_to_hex((j-600,200,0)) #YELLOW


    plt.plot(x,Vlstx1, colourhex)
plt.ylim(0,130)
plt.ylabel('Velocity [m/s]')
plt.xlabel('Distance downstream airfoil [-]')
plt.show()


#Compute average velocities
for j in np.arange(0,678,step):
    pixelsimageplot = pixelsimages(j)
    Vlstx1 = Vlstx(pixelsimageplot)
    
    for n in np.arange(0,len(Vavglst)):
        V = Vlstx1[n]
        Vavg = Vavglst[n]
        par = j//step
        Vavg = (Vavg*par + V)/(par+1)
        Vavglst[n] = Vavg        


plt.plot(x, Vavglst, 'g')
plt.ylim(0,130)
#plt.show()


#Define lower quality for min/max observations




#Compute min+max value
for j in np.arange(0,678,step2):
    pixelsimageplot = pixelsimages(j)
    Vlstx1 = Vlstx(pixelsimageplot)
    
    for m in np.arange(0,len(Vminlst)): 
        
        V = Vlstx1[m]
        Vmin = Vminlst[m]
        Vminlst[m] = min(V,Vmin)
        
        Vmax = Vmaxlst[m]
        Vmaxlst[m] = max(V,Vmax)


plt.plot(x2,Vmaxlst,'r')
plt.plot(x2,Vminlst,'b')
#plt.show()


      
numlst = q2
lenlst = 678//step3
boxplotdata = [] 

for i in range(0,numlst):
        command = "" # this line is here to clear out the previous command
        command = "Vlst_" + str(i) + " = []"
        exec(command)
           
for j in np.arange(0,678,step3):
    pixelsimageplot = pixelsimages(j)
    Vlstx1 = Vlstx(pixelsimageplot)
#should run lenlst times     
    for i in range(0,numlst):
       # for j in range(lenlst):
            V = Vlstx1[i]
            command = "" # this line is here to clear out the previous command
            command = "Vlst_" + str(i) + ".append(V)"
            exec(command)

for i in range(0,numlst):
    command = "" # this line is here to clear out the previous command
    command = "boxplotdata.append(Vlst_" + str(i) + ")"
    exec(command)
 
print(np.mean(Vavglst))

       
plt.style.use(["ggplot"])
plt.plot(x2,Vmaxlst,'r')
plt.plot(x2,Vminlst,'b')  
plt.plot(x, Vavglst, 'g')
plt.ylim(80,120)
plt.ylabel('Velocity [m/s]')
plt.xlabel('Distance downstream airfoil [-]')
plt.boxplot(boxplotdata, positions=np.arange(0,numlst))

plt.savefig('Boxplotloc2.pdf')
plt.show()
    
    
    

    











