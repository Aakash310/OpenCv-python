import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event , x , y , flag , param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img , (x,y) , 3 , (0,0,255) , -1)
        myColorImage = np.zeros((512,512,3) , np.uint8)

        myColorImage[:] = [blue,green,red]
        cv2.imshow('color',myColorImage)
        

#img = np.zeros((512,512,3) , np.uint8)
img = cv2.imread('Lenna.png',1)
cv2.imshow("image",img)
points = []
cv2.setMouseCallback("image" , click_event)

cv2.waitKey()
cv2.destroyAllWindows()
