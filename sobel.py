#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:20:24 2018

@author: shwetha
"""

from scipy import *
from scipy import signal
from PIL import Image
import scipy.misc
import math

# The image that you want to use the Laplacian operator on
usedImage = 'xray.jpg'

# Open the desired JPEG image as an array
img = array(Image.open(usedImage).convert("L"))

# Laplacian operator
kernel1 = [[-1, 0, +1],
           [-2, 0, +2],
           [-1, 0, +1]]

kernel2 = [[+1, 0],
           [0, -1]]

kernel3 = [[-1, 0, +1],
           [-1, 0, +1],
           [-1, 0, +1]]

# CONVOLUTION 1
# Convolute the input image with the laplacian kernel
# Generate output array im of the convolution
im1 = signal.convolve(img, kernel1, mode='same')
im2 = signal.convolve(img, kernel2, mode='same')
im3 = signal.convolve(img, kernel3, mode='same')

# Print array to console
#print ('Im: Convolution 1')
#print (im)

# Save the arrays created as JPEG images
scipy.misc.imsave('im1.jpeg', im1)
scipy.misc.imsave('im2.jpeg', im2)
scipy.misc.imsave('im3.jpeg', im3)

# Add the convoluted image to the original to start sharpen
final_sobel1 = im1 + img
final_robert1 = im2 +img
final_prewitt1 = im3 +img

# Save combined image
scipy.misc.imsave('final_sobel.jpeg', final_sobel1)
scipy.misc.imsave('final_robert.jpeg', final_robert1)
scipy.misc.imsave('final_prewitt.jpeg', final_prewitt1)
print ('Finished Sharpening')