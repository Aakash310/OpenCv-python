import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1 , (200,0) , (300,100) , (255,255,255) , -1)
img1 = cv2.resize(img1,(250,500))
img2 = cv2.imread('B_W.jpg')
img2 = cv2.resize(img2,(250,500))

#bitAnd = cv2.bitwise_and(img1,img2)
#bitOr = cv2.bitwise_or(img1,img2)
#bitXor = cv2.bitwise_xor(img1,img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("Image1" , img1)
cv2.imshow("image2" , img2)
#cv2.imshow("Image3",bitAnd)
#cv2.imshow("Image4",bitOr)
#cv2.imshow("Image5",bitXor)
cv2.imshow("Image6",bitNot1)
cv2.imshow("Image7",bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()