# -*- coding: utf-8 -*-

import cv2
import numpy as np
#import matplotlib.pyplot as plt
#pic = cv2.imread('images.png')
cap= cv2.VideoCapture(0)

while(1):
	_,frame = cap.read()

	threshold_1 = 100
	threshold_2 = 200
	edge = cv2.Canny(frame,threshold_1,threshold_2)
	cv2.imshow('Original',edge)
	#plt.show()
	k=cv2.waitKey(5) & 0xFF	
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()
