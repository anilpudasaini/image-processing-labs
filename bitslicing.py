# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:27:09 2022
@author: Anil 076MSICE003

"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# reading image and converting to gray scale
load_img = Image.open('lion.jpg').convert('L')
img = load_img.resize((400,400))
# convert to numpy array 
numpy_image = np.array(img)

#setting figure width and height
fig = plt.figure()
fig.set_figheight(100)
fig.set_figwidth(100)
fig.add_subplot(9,1,1)
plt.imshow(img, cmap='gray')
plt.title('Original image')

#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(numpy_image.shape[0]):
  for j in range(numpy_image.shape[1]):
    lst.append(np.binary_repr(numpy_image[i][j] ,width=8)) # width = no. of bits

# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.

#a = np.array([int(i) for i in lst[17]],dtype = np.uint8)
#array([1, 0, 1, 1, 1, 1, 0, 0], dtype=uint8)
#a[0] = 1 ie. LSB-----> MSB

eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(400,400)
eight_bit_image = Image.fromarray(eight_bit_img)
fig.add_subplot(9,1,2)
plt.imshow(eight_bit_image, cmap='gray')
plt.title('8 bit')

seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(400,400) 
seven_bit_image = Image.fromarray(seven_bit_img)
fig.add_subplot(9,1,3)
plt.imshow(seven_bit_image, cmap='gray')
plt.title('7 bit')

six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(400,400)
six_bit_image = Image.fromarray(six_bit_img)
fig.add_subplot(9,1,4)
plt.imshow(six_bit_image, cmap='gray')
plt.title('6 bit')


five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(400,400)
five_bit_image = Image.fromarray(five_bit_img)
fig.add_subplot(9,1,5)
plt.imshow(five_bit_image, cmap='gray')
plt.title('5 bit')

four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(400,400)
four_bit_img = Image.fromarray(four_bit_img)
fig.add_subplot(9,1,6)
plt.imshow(four_bit_img, cmap='gray')
plt.title('4 bit')


three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(400,400)
three_bit_img = Image.fromarray(three_bit_img)
fig.add_subplot(9,1,7)
plt.imshow(three_bit_img, cmap='gray')
plt.title('3 bit')

two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(400,400)
two_bit_img = Image.fromarray(two_bit_img)
fig.add_subplot(9,1,8)
plt.imshow(two_bit_img, cmap='gray')
plt.title('2 bit')

one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(400,400)
one_bit_img = Image.fromarray(one_bit_img)
fig.add_subplot(9,1,9)
plt.imshow(one_bit_img, cmap='gray')
plt.title('1 bit')

addedImage = eight_bit_img + seven_bit_img + six_bit_img + five_bit_img
plt.imshow(addedImage, cmap='gray')
plt.title('Reconstructed using 8,7,6,5 bit planes')
