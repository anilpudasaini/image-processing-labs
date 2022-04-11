# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:23:00 2022

@author: Anil Pudasaini 076MSICE003

Zooming can be done by 2 methods :
    1 Nearest Neighbour Interpolation
    2. Bilinear Interpolation
    
    I have used Nearest Neighbour Interpolation
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def zoom(image,factor):   
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    zoom_img_r = int(np.floor(r * factor))
    zoom_img_c = int(np.floor(c * factor))  #for float factors
    
    #defining new array for manipulated image
    zoom = np.zeros(shape=(zoom_img_r,zoom_img_c))
    
    for i in range(0,zoom_img_r):
        for j in range(0,zoom_img_c):
            zoom[i][j] = numpy_image[int(i/factor)][int(j/factor)]
            
            
    
    zoomed_image = Image.fromarray(zoom)
    
    return zoomed_image 


# reading image and converting to gray scale
global factor
factor = 4
loaded_img = Image.open('girl.jpg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
final_img = zoom(loaded_img,factor)

'''
saving the image
if final_img.mode != 'RGB':
    final_img = final_img.convert('RGB')
final_img.save("saved.jpg")
'''
#displaying the images

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 7), dpi=90,sharex = 'row', sharey ='row')
ax[0].set_title('Original image')
ax[0].imshow(image, cmap='gray')
ax[1].imshow(final_img, cmap='gray')
ax[1].set_title('Zoomed Image by a factor of ' +str(factor) + ' times')
