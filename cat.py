import cv2

faceCascade = cv2.CascadeClassifier("eyedetected.xml")


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for(x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_ITALIC,0.8,color,3)
    return img

def detect(img,faceCascade):
    img=draw_boundary(img,faceCascade,1.1,10,(255,0,0),"Cat")
    return img
   
cap = cv2.VideoCapture(0)
while(True):
     ret,frame = cap.read()
     frame = detect(frame,faceCascade)
     cv2.imshow('Video Processing',frame)
     if(cv2.waitKey(1) & 0xFF== ord('q')): #wait for q then quite
         break
cap.release()# GB the Cpu clock
cv2.destroyAllWindows()