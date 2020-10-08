import cv2
import datetime

cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

cap.set(3,1280)
cap.set(4,720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame , datet , (10,50) , font , 1 , (0,0,255) , 1 ,cv2.LINE_AA) 
        cv2.imshow("Frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    

cap.release()
cv2.destroyAllWindows()


