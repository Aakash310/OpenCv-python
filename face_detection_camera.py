import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('WIN_20191027_21_03_06_Pro.jpg')
img = cv2.resize( img , (512,512))
gray = cv2.cvtColor( img , cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

for x,y,w,h in faces:
    cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0) , 3)

cv2.imshow('img',img)
cv2.waitKey(0)