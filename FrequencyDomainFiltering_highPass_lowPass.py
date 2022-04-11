# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:31:07 2022

@author: uSer
"""

from skimage import exposure
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

loaded_img = Image.open('smoothing.png').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)

#converting spatial domain into frequency domain

f = np.fft.fft2(image)
fshift = np.fft.ifftshift(f) #shift the origin to the centre of image
#exposure is used just to see the frequency image cleary
#True frequency domain image is fshift
frequency_image = exposure.adjust_log(np.abs(fshift),1)

row,col = image.size


crow = int(row/2)
ccol = int(col/2)

#kernel = np.zeros((row,col),np.uint8)
#kernel[crow-30:crow+30, ccol-30:ccol+30] = 1 

#TO MAKE THIS HIGH PASS FILTER
kernel = np.ones((row,col),np.uint8)
kernel[crow-30:crow+30, ccol-30:ccol+30] = 0

#THIS PART OF THE CODE IS ONLY FOR EASIER DEMONSTRATION AS ADJUSTED EXPOSURE IMG IS USED
filtered_freq_img = frequency_image * kernel

inverse_shift = np.fft.ifftshift(filtered_freq_img)

spatial_img_after_filtering = np.abs(np.fft.ifft2(inverse_shift))

#THIS IS THE REAL FILTER

filtered_freq_img_real = fshift * kernel

inverse_shift_real = np.fft.ifftshift(filtered_freq_img_real)

spatial_img_after_filtering = np.abs(np.fft.ifft2(inverse_shift_real))


fig,axes = plt.subplots(nrows = 2, ncols=3,figsize=(14,10))
ax = axes.ravel()
ax[0].imshow(image,cmap ='gray')
ax[0].set_title('Spatial Image')

ax[1].imshow(frequency_image,cmap ='gray')
ax[1].set_title('Frequency Image')

ax[2].imshow(kernel,cmap='gray')
ax[2].set_title('Low Pass Kernel')

ax[3].imshow(filtered_freq_img,cmap='gray')
ax[3].set_title('Filtered Frequency Image')

ax[4].imshow(inverse_shift,cmap='gray')
ax[4].set_title('Frequency Image after Inverse FShift')

ax[5].imshow(spatial_img_after_filtering,cmap='gray')
ax[5].set_title('Final Image Using Low Pass Filter')