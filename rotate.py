# -*- coding: utf-8 -*-
#shifting and rotating
import numpy as np
import cv2
import matplotlib.pyplot as plt
pic = cv2.imread('images.png')

cols=pic.shape[1]
rows=pic.shape[0]
center=(cols/2,rows/2)
angle=-90

#M=np.float32([[1,0,350],[0,1,200]])
#shifted = cv2.warpAffine(pic,M,(cols,rows))

#params(center,angle,size of the image=>1-normal,2-double size,0)
M=cv2.getRotationMatrix2D(center,angle,1)
rotate = cv2.warpAffine(pic,M,(cols,rows))
plt.imshow(rotate)
plt.show()

