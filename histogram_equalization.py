# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:30:16 2022

@author: Anil Pudasaini 076MSICE003

The contrast of an image is enhanced when various shades in the image becomes
more distinct. We can do so by darkening the shades of the darker pixels and vice versa. This is equivalent to widening the range of pixel intensities. To have a good contrast, the following histogram characteristics are desirable:
the pixel intensities are uniformly distributed across the full range of values
(each intensity value is equally probable), and
the cumulative histogram is increasing linearly across the full intensity range.
Histogram equalization modifies the distribution of pixel intensities to achieve
these characteristics.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# reading image and converting to gray scale
loaded_img = Image.open('histo.jpeg').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)


"""
STEP 1: Normalized cumulative histogram
"""
#flattening image array and counting number of pixels having same intensity level
numpy_array = np.array(image)
flat_img = numpy_array.flatten()
plt.hist(flat_img,bins = 256)
histogram = np.zeros(256)

for pixel in flat_img:
    histogram[pixel] +=1

#plt.plot(histogram)

#normalize
sum_pixels = np.sum(histogram)
histogram_array = histogram/sum_pixels

#normalized cumulative histogram   0  --> 1
chistogram_array = np.cumsum(histogram_array)

#plt.plot(chistogram_array)

"""
STEP 2: Pixel mapping lookup table
"""
transform_map = np.floor(255 * chistogram_array).astype(np.uint8)


"""
STEP 3: Transformation
"""
# flatten image array into 1D list
img_list = list(flat_img)

# transform pixel values to equalize
eq_img_list = [transform_map[p] for p in img_list]

# reshape and write back into img_array
eq_img_array = np.reshape(np.array(eq_img_list), numpy_array.shape)

#convert NumPy array to pillow Image
eq_img = Image.fromarray(eq_img_array, mode='L')

"""
Step 4: VISUALIZING
"""
#displaying the images
fig = plt.figure(figsize = (10,10))

fig.add_subplot(2,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(2,2,2)
plt.imshow(eq_img, cmap = 'gray')
plt.title('Histogram Equalized image')

#plotting histogram after flatenning
np_original = np.array(image)
flat = np_original.flatten()
fig.add_subplot(2,2,3)
plt.hist(flat, bins=50)

#
np_final_img = np.array(eq_img)
flat = np_final_img.flatten()
fig.add_subplot(2,2,4)
plt.hist(flat, bins=50)