import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import statistics 

#Define quality of measurements
m = 480
n = 360
size = m,n
step = 1

#Convert RGB to HSV
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0: 
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v


def dpdt(z,i):
    #Open image
    namefile = 'dpdt_0'
    if z == 0:
        z = '000'
    elif z < 10:
        z = '00'+ str(z)
    elif z < 100:
        z = '0' + str(z)
    else: 
        z = str(z)
        
    namefile = namefile + z + '.png'
    im = Image.open(namefile)    
    pixelsimage = list(im.getdata())

   
    r = int(pixelsimage[i][0])
    g = int(pixelsimage[i][1])
    b = int(pixelsimage[i][2])
    #v = (r+g+b)/(3*255)
    h,s,v = rgb2hsv(r, g, b)
    return v*2-1



i1 = 200*m+ 120
i2 = 200*m + 200
i3 = 175*m + 300
i4 = 70*m + 300
v1lst= []
v2lst = []
v3lst = []
v4lst = []
tlst = []
t = 0
tstep = (4.76*10**-5)*step
tstart = 600
tstop = tstart + 50

for p in np.arange(0,678,step):   
    v1 = dpdt(p,i1)
    v2 = dpdt(p,i2)
    v3 = dpdt(p,i3)
    v4 = dpdt(p,i4)
    v1lst.append(v1)
    v2lst.append(v2)
    v3lst.append(v3)
    v4lst.append(v4)
    tlst.append(t)
    t = t + tstep


print(statistics.stdev(v1lst), statistics.mean(v1lst))
print(statistics.stdev(v2lst), statistics.mean(v2lst))
print(statistics.stdev(v3lst), statistics.mean(v3lst))
print(statistics.stdev(v4lst), statistics.mean(v4lst))



plt.style.use(["ggplot"])
plt.plot(tlst[tstart:tstop],  v1lst[tstart:tstop], 'indigo')
plt.xlabel('Time [s]')
plt.ylabel('dP/dt [-]')
plt.ylim(-1.1,1.1)
plt.show()  

plt.plot(tlst[tstart:tstop],  v2lst[tstart:tstop], 'red')
plt.xlabel('Time [s]')
plt.ylabel('dP/dt [-]')
plt.ylim(-1.1,1.1)
plt.show()

plt.plot(tlst[tstart:tstop],  v3lst[tstart:tstop], 'forestgreen')
plt.xlabel('Time [s]')
plt.ylabel('dP/dt [-]')
plt.ylim(-1.1,1.1)
plt.show()

plt.plot(tlst[tstart:tstop],  v4lst[tstart:tstop], 'royalblue')
plt.xlabel('Time [s]')
plt.ylabel('dP/dt [-]')
plt.ylim(-1.1,1.1)
plt.show()   



































