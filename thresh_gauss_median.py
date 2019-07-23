# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
pic = cv2.imread('noisy.png')
# 0=> gray 1=>white
#pixel value below threshold_value turn to gray amd greater than will turn to white

threshold_value=12

T_value,binary_threshold =cv2.threshold(pic,threshold_value,255,cv2.THRESH_BINARY)
gray_scaled = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

#(pic,t_value,max(white),Type of threshold)

#Gauusian Threshold
#gaus = cv2.adaptiveThreshold(pic,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('original',pic)
cv2.imshow("threshold",binary_threshold)
#cv2.imshow("gaussian",gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


#plt.imshow(binary_threshold)
#plt.show()


#Gaussian Blurr (Smoothness)


#matrix=(7,7) #7 by 7 one's
#blur=cv2.GaussianBlur(pic,matrix,0)
#plt.imshow(blur)
#plt.show()


#Median Blurr(to remove noise)

#kernal = 3
#median = cv2.medianBlur(pic,kernal)
#plt.imshow(median)
#plt.show()   
