import numpy as np
import cv2

#img = cv2.imread('Lenna.png',1)
img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img , (0,0) , (255,510) , (255,0,0) , 5)
img = cv2.arrowedLine(img , (0,255) , (255,255) , (255,0,0) , 5)

img = cv2.rectangle(img , (384,0) , (510,128), (0,255,0), 10)
img = cv2.rectangle(img , (255,255) , (400,400), (0,255,0), -1)

img = cv2.circle(img , (450,450) , 50 , (0,0,255) , 10)
img = cv2.circle(img , (447,63) , 63 , (0,0,255) , -1)

ing = cv2.putText(img , 'OpenCV' , (10,500) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 4 , (100,100,100) , 5 , cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()    