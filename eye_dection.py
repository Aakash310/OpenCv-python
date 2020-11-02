import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#img = cv2.imread('WIN_20191027_21_03_06_Pro.jpg')
#img = cv2.resize( img , (512,512))
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret , frame = cap.read()

    gray = cv2.cvtColor( frame , cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

    for x,y,w,h in faces:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (255,0,0) , 3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color , (ex,ey) , (ex+ew,ey+eh) , (0,255,0) , 5)

    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()    

