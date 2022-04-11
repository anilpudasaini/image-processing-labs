"""
Created on Mon Mar 21 10:38:45 2022
@author: 076MSICE003
Contrast is a measure of the range of an image; i.e. 
how spread its intensities are. It has many formal definitions 
one famous is Michelson’s:
He says contrast =  ( Imax - Imin )/( Imax + I min )
Contrast is strongly tied to an image’s overall visual quality. Ideally,
we’d like images to use the entire range of values available to them.
Contrast Stretching and Histogram Equalisation have the same goal:
making the images to use entire range of values available to them.
But they use different techniques. Contrast Stretching works like mapping
it maps minimum intensity in the image to the minimum value in
 the range( 84 ==> 0 in the example above )
With the same way, it maps maximum intensity in the image to the maximum value
in the range( 153 ==> 255 in the example above )
This is why Contrast Stretching is un-reliable, if there exist only
two pixels have 0 and 255 intensity, it is totally useless.
However a better approach is Histogram Equalisation which uses probability distribution.


Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)

 

Io                                - Output pixel value

Ii                                 - Input pixel value

Mini                         - Minimum pixel value in the input image

Maxi                        - Maximum pixel value in the input image

Mino                        - Minimum pixel value in the output image

Maxo                       - Maximum pixel value in the output imag
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def contrast_stretching(input_image,outputLow,outputHigh):
    loaded_img = input_image.resize((400,400), Image.LANCZOS)
    #converitng it to array
    numpy_image = np.array(loaded_img)
    
    min_intensity = np.amin(numpy_image)
    max_intensity = np.amax(numpy_image)
    
    r = numpy_image.shape[0]
    c = numpy_image.shape[1]
    
    #defining new array for manipulated image
    temp = np.zeros(shape=(r,c))
    for i in range(r):
        for j in range(c):
            temp[i][j] = (numpy_image[i][j] - min_intensity) *(((outputHigh-outputLow)/max_intensity-min_intensity)+min_intensity)
    
    
    final_image = Image.fromarray(temp)
    
    return final_image

# reading image and converting to gray scale
loaded_img = Image.open('histo.png').convert('L')
image = loaded_img.resize((400,400), Image.LANCZOS)
final_img = contrast_stretching(loaded_img,0,255)

#displaying the images
fig = plt.figure(figsize = (10,10))

fig.add_subplot(2,2,1)
plt.imshow(image, cmap = 'gray')
plt.title('Original image')

fig.add_subplot(2,2,2)
plt.imshow(final_img, cmap = 'gray')
plt.title('Constrast Stretched')

#plotting histogram after flatenning
np_original = np.array(image)
flat = np_original.flatten()
fig.add_subplot(2,2,3)
plt.hist(flat, bins=256)

#
np_final_img = np.array(final_img)
flat = np_final_img.flatten()
fig.add_subplot(2,2,4)
plt.hist(flat, bins=256)



