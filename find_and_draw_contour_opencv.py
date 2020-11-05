import cv2 
import numpy as Np

img = cv2.imread("RGB_Balls.jpg")
imgray = cv2.cvtColor( img , cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold( imgray , 127 , 255 , 0)
contours , heirarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
print("Number of contours = "+ str(len(contours)))

cv2.drawContours( img , contours , -1 , (0,255,0) , 3)

cv2.imshow("image1",img)
cv2.imshow("image2",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()