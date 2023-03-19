import cv2

face_cassade = cv2.CascadeClassifier("frontaldef.xml")
upper_cassade = cv2.CascadeClassifier("uppedef.xml")
left_cassade =  cv2.CascadeClassifier("leftdef.xml")
right_cassade =  cv2.CascadeClassifier("rightdef.xml")

img = cv2.imread('kay1tap.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cassade.detectMultiScale(gray,1.3,5)
for(x,y,w,h)in faces:
    img =  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

uppers = upper_cassade.detectMultiScale(gray)
for(ex,ey,ew,eh) in uppers:
    img_eye = cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

lefts = left_cassade.detectMultiScale(gray,1.90,8)
for(cx,cy,cw,ch) in lefts:
    img_letf = cv2.rectangle(img,(cx,cy),(cx+cw,cy+ch),(0,0,0),3)
    
rights = right_cassade.detectMultiScale(gray,1.90,7)
for(rx,ry,rw,rh) in rights:
    img_right = cv2.rectangle(img,(rx,ry),(rx+rw,ry+rh),(0,255,255),2)
    
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows