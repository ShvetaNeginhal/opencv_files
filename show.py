import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images.png',0)
#img1 = cv2.imwrite('images_003.jpg',img)

cv2.imshow('Original',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

#plt.imshow(img, cmap='YlOrRd')
#plt.show()
#cv2.startWindowThread() 