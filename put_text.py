# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
pic= np.zeros((500,500,3),dtype='uint8')

font=cv2.FONT_HERSHEY_DUPLEX

#(picture,text_name,(x,y),font,size of text,color,line_thickness,type of line)
cv2.putText(pic, 'Travel',(100,100),font,3,(255,255,255),4,cv2.LINE_8)

plt.imshow(pic, cmap='YlOrRd')
plt.show()
