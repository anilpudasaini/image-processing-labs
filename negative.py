# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:37:21 2022
@author: Anil 076MSICE003

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#creating a function to negate the image

def negative(image):
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    temp = np.zeros(shape=(r,c))
    
    for i in range(r):
        for j in range(c):
            temp[i][j] = 255 - numpy_image[i][j] #s = (L – 1) – r L:maximum intensity
    
    negative = Image.fromarray(temp)
    
    return negative 


# reading image and converting to gray scale
loaded_img = Image.open('girl.jpg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
neg_img = negative(loaded_img)

"""
If you have an L mode image, 
that means it is a single channel image - normally interpreted as greyscale. 
The L means that is just stores the Luminance. It is very compact, but only 
stores a greyscale, not colour.

"""
#displaying the images
fig = plt.figure(figsize = (7,5))

fig.add_subplot(1,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(1,2,2)
plt.imshow(neg_img, cmap='gray')
plt.title('Negative image')


