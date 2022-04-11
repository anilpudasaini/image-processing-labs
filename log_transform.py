# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:37:21 2022
@author: Anil 076MSICE003 

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

#creating a function to negate the image

def log_transform(image,constant):
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    temp = np.zeros(shape=(r,c))
    
    for i in range(r):
        for j in range(c):
            temp[i][j] = constant * math.log(numpy_image[i][j]+1)
    
    log_t = Image.fromarray(temp)
    
    return log_t 


# reading image and converting to gray scale
loaded_img = Image.open('cats.jpg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
log_img = log_transform(loaded_img,75)

"""
Log transformation
The log transformations can be defined by this formula
s = clog(r + 1).
Where s and r are the pixel values of the output and the input image and c is a constant. The value 1 is added to each of the pixel value of the input image because if there is a pixel intensity of 0 in the image,
then log (0) is equal to infinity. So 1 is added, to make the minimum value at
least 1.During log transformation, the dark pixels in an image are expanded as compare 
to the higher pixel values. The higher pixel values are kind of compressed in log transformation. This result in following image enhancement.
The value of c in the log transform adjust the kind of enhancement you are looking for.
"""
#displaying the images
fig = plt.figure(figsize = (7,7))

fig.add_subplot(1,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(1,2,2)
plt.imshow(log_img, cmap='gray')
plt.title('Log Transformed image with c = 75')



