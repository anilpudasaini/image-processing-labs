# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:07:29 2022

@author: Anil 076MSICE003
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

#creating a function to negate the image

def powerLaw(image,constant,gamma):
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    temp = np.zeros(shape=(r,c))
    
    for i in range(r):
        for j in range(c):
            temp[i][j] = constant * (numpy_image[i][j] ** gamma) #Correcting gamma s=cr^γ
    
    power = Image.fromarray(temp)
    
    return power


# reading image and converting to gray scale
loaded_img = Image.open('einstein.jpg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
power_img = powerLaw(loaded_img,1,10)

"""
s=cr^γ
This symbol γ is called gamma, due to which this transformation
is also known as gamma transformation.
Variation in the value of γ varies the enhancement of the images. 
Different display devices / monitors have their own gamma correction, 
that’s why they display their image at different intensity.
This type of transformation is used for enhancing images for different type 
of display devices. The gamma of different display devices is different. 
For example Gamma of CRT lies in between of 1.8 to 2.5, that means the image displayed
on CRT is dark.
"""
#displaying the images
fig = plt.figure(figsize = (7,25))

fig.add_subplot(5,1,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(5,1,2)
power_img1 = powerLaw(loaded_img,1,1.20)
plt.imshow(power_img1, cmap='gray')
plt.title('Gamma = 1.2')

fig.add_subplot(5,1,3)
power_img2 = powerLaw(loaded_img,1,1.25)
plt.imshow(power_img2, cmap='gray')
plt.title('Ganma = 1.25')

fig.add_subplot(5,1,4)
power_img3 = powerLaw(loaded_img,1,1.30)
plt.imshow(power_img3, cmap='gray')
plt.title('Gamma = 1.3')

fig.add_subplot(5,1,5)
power_img4 = powerLaw(loaded_img,1,1.35)
plt.imshow(power_img4, cmap='gray')
plt.title('Gamma = 1.35')



