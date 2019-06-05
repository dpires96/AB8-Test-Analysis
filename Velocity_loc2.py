import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


#Define quality of measurements
q = 3
size = 25*q,15
x = np.arange(0,15*q)

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


#Convert h value to the velocity
def Velocity(h):
    V = (-1/240*h+1)*120
    return V



def pixelsimages(z):
    #Open image
    namefile = 'Velocity_0'
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
    #plt.imshow(im) 
    #plt.show()
    
    #Pixellize image
    im_resized = im.resize(size)
    #plt.imshow(im_resized)
    #plt.show()
    
    pixelsimage = []
    del pixelsimage
    pixelsimage = list(im_resized.getdata())
    #print(pixelsimage)
    
    return pixelsimage

def Vlstx(pixelsimagex):  
    #Create a list with the velocities for each pixel of interest
    Vlst = []
    pixline = []
    
    rin = 87*q   
    rout = rin + 15*q
    
    for i in np.arange(rin,rout): 
        r = int(pixelsimagex[i][0])
        g = int(pixelsimagex[i][1])
        b = int(pixelsimagex[i][2])

        h,s,v = rgb2hsv(r, g, b)
        Vlst.append(Velocity(h))
        pixline.append((r,g,b)) 
        

    return Vlst

pixelsimages(100)
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def create_list(numlst, lenlst):
    for i in range(1,numlst+1):
        command = "" # this line is here to clear out the previous command
        command = "Vlst_" + str(i) + " = np.zeros(lenlst)"
        exec(command)















