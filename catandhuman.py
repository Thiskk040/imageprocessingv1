import cv2

face_cassade = cv2.CascadeClassifier("frontaldef.xml")
eye_cassade = cv2.CascadeClassifier("eyedef.xml")
cat_cassade =  cv2.CascadeClassifier("catdef.xml")
img = cv2.imread('humanandcat.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cassade.detectMultiScale(gray,1.3,5)
for(x,y,w,h)in faces:
    img =  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

eyes = eye_cassade.detectMultiScale(gray,1.14,7)
for(ex,ey,ew,eh) in eyes:
    img_eye = cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cats = cat_cassade.detectMultiScale(gray,1.1,7)
for(cx,cy,cw,ch) in cats:
    img_cat = cv2.rectangle(img,(cx,cy),(cx+cw,cy+ch),(0,0,255),1)
    
        

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows