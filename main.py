import cv2
import numpy as np

cap = cv2.VideoCapture('b.mp4')

if cap.isOpened()== False :
    print("An error has occured")
    exit()

oshit = open("output.txt","w")
oshit.close()
oshit = open("output.txt","a")
oshit.write("{")

segs = 0
lastframe = None
while cap.isOpened():
        r, frame = cap.read()
        frame = cv2.resize(frame, (60,40),cv2.INTER_AREA)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = np.round(np.round(frame/255,2)*100)
        frame = str(frame.tolist())
        #print(frame)
        frame = frame.replace(".0","")
        frame = frame.replace(" ","")
        frame = frame.replace("100","99")
        frame = frame.replace("],","],\n")
        frame = frame.replace("[","{")
        frame = frame.replace("]","}")
        oshit.write(frame+",\n")
        lastframe = frame
        segs+=1
    
oshit.write("}")
oshit.close()
