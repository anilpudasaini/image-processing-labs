# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:13:13 2022

@author: Anil Pudasaini 076MSICE003
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#creating a function to negate the image

def threshold (image):
    #user input
    global threshold_value
    threshold_value = int (input ("Enter the value of threshold  ")) 
    while threshold_value not in range(256): 
        print('Value should be in range 0 to 255. TRY AGAIN!!')
        threshold_value = int (input ("Enter the value of threshold  ")) 
    
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    #defining new array for manipulated image
    temp = np.zeros(shape=(r,c))
    
    for i in range(r):
        for j in range(c):
            if(numpy_image[i][j]>=threshold_value):
                temp[i][j] = numpy_image[i][j]
            else:
                temp[i][j] = 0
            
            
    
    after_threshold_image = Image.fromarray(temp)
    
    return after_threshold_image 


# reading image and converting to gray scale
loaded_img = Image.open('cats.jpg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
final_img = threshold(loaded_img)

#displaying the images
fig = plt.figure(figsize = (10,10))

fig.add_subplot(1,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(1,2,2)
plt.imshow(final_img, cmap='gray')
plt.title('Thresholded image with value ' +str(threshold_value))



