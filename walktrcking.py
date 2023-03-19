import cv2
cap = cv2.VideoCapture(1)

#เเยกออกมาไว้หาเส้น contours ตอนที่มีการเคลื่อนไหว
check ,frame1 = cap.read()
check ,frame2 = cap.read()

while(cap.isOpened()):
   if check == True: #ป้องกัน error ที่เกิดจาก video เล่นจบเเล้ว เเต่โปรเเกรมยังทำงานอยู่

          #หาผลต่างของค่าที่มาจาก frame1 เเละ frame2 เพื่อหาค่าความคลาดเคลื่อนของเเต่ละเฟรม ใช้ในการหาวัตถุเคลื่อนที่
          motiondiff = cv2.absdiff(frame1,frame2)
          #นำภาพมาแปลงเป็น  grayscale 
          gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)

          #ใส่ความเบลอเข้าไปในวัตถุเพื่อพื้นที่จะได้มีความชัดเจนยิ่งขึ้น
          blur = cv2.GaussianBlur(gray,(5,5),0)

          #ใส่ threshold เพื่อเเยกรายละเอียดภายในภาพ
          thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)

          #นำมาขยายพื้นที่ต่อโดยใช้งาน dilation
          dilation = cv2.dilate(result,None,iterations=3)
        
          #นำภาพจากทีได้มาหาเส้น Contours
          contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            #-> ได้ผลลัพธ์เป็นเส้น contour กับ ลำดับชั้น
            #-> ตัวเเปร contours จะเก็บค่าพิกัด contours เอาไว้
            
            #วาดสี่เหลี่ยมในวัตถุที่กำลังเคลื่อนที่
          for contour in contours:
            #รับค่าจากตัวเเปร contours มาใส่
            (x,y,w,h) = cv2.boundingRect(contour)
            
            #ปรับจำนวนกล่องสี่เหลี่ยมไม่ให้กระจัดกระจาย
            if cv2.contourArea(contour)<1000:
              continue
            
            #สร้างกล่องสี่เหลี่ยม
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        #แสดงผลภาพ
          cv2.imshow("Output",frame1) #เป็นการเเสดงภาพที่อ่านตอลดเวลา


          #สร้างการขยับจาก frame1 ไปที่ frame2 
          frame1 = frame2
          check,frame2 = cap.read()
        
          if cv2.waitKey(1) & 0xFF == ord("q"):#เมื่อกด q จะรอดีเล 1 วิ เเล้วปิดออกไป
              break
   else:
       break #ถ้าหมดเวลาเเล้วก็ให้ปิด video ไป


cap.release() #ทำการคืนทรัพยากรให้เครื่อง
cv2.destroyAllWindows() #ทำการปิดหน้าต่าง