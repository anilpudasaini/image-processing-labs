# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:44:07 2022

@author: Anil Pudasaini 076MSICE003
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#creating a function to perform gray_level_slicing

def gray_level_slicing(image):
    #user input
    global start,end
    start, end = input("Enter range of intensities values: ").split()    
    image = image.resize((400,400), Image.LANCZOS)
    #converting to numpy array
    numpy_image = np.array(image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    #defining new array for manipulated image
    temp = np.zeros(shape=(r,c))
    
    for i in range(r):
        for j in range(c):
            if(numpy_image[i][j] in range(int(start),int(end))):
                temp[i][j] = 255          #0 for dark and 255 for white
            else:
                temp[i][j] = numpy_image[i][j]
            
            
    
    sliced_image = Image.fromarray(temp)
    
    return sliced_image 


# reading image and converting to gray scale
loaded_img = Image.open('forest.jpeg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
final_img = gray_level_slicing(loaded_img)

'''
saving the image
if final_img.mode != 'RGB':
    final_img = final_img.convert('RGB')
final_img.save("saved.jpg")
'''
#displaying the images
fig = plt.figure(figsize = (10,10))

fig.add_subplot(1,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(1,2,2)
plt.imshow(final_img, cmap='gray')
plt.title('Gray level slicing between intensities ' +str(start) +' and ' + str(end))



