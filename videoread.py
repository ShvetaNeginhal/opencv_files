#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:25:16 2018

@author: shwetha
"""

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

#to save the video into a file
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #out.write(frame)
    
    cv2.imshow('frame',frame)
    cv2.imshow("gray",gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
      