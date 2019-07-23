# -*- coding: utf-8 -*-
#Drawing,rectangle,line,circle
import cv2
import matplotlib.pyplot as plt
import numpy as np
pic= np.zeros((500,500,3),dtype='uint8')
color=(255,0,255)
#cv2.shape(picture,(x,y,(x,y),color,RGB))
#cv2.rectangle(pic,(0,1),(400,300),color,3,lineType=8,shift=0)
#cv2.line(pic,(250,350),(200,200),color)
#cv2.circle(pic,(250,250),50,color)
plt.imshow(pic, cmap='YlOrRd')
plt.show()
#cv2.imshow('dark',pic)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


