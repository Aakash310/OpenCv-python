import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('WIN_20191027_21_03_06_Pro.jpg')
#img = cv2.resize( img , (512,512))
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret , frame = cap.read()

    gray = cv2.cvtColor( frame , cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

    for x,y,w,h in faces:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (255,0,0) , 3)

    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()    

