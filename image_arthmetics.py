#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:52:10 2018

@author: shwetha
"""

import cv2
import numpy as np


img1 = cv2.imread('dog.4023.jpg')
img2 = cv2.imread('dog.4025.jpg')

#add = img1 + img2
add = cv2.add(img1,img2)
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()