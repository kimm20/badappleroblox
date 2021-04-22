import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture("uwu.mp4")
data=[]
#data[t][y][x]

while True:
    ret,frame=cap.read()
    if ret:
        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame,(44,25))
        frame = np.array(frame)/255
        data.append(frame)
            
    else:
        break
cv2.destroyAllWindows()
file=open("pros.txt","w+")
ee=[]
for i in range(len(data)):
    oo=data[i].tolist()
    for y in range(len(oo)):
        for x in range(len(oo[y])):
            oo[y][x]=np.round(oo[y][x],2)
                
    ee.append(oo)
ee = str(ee)
ee = ee.replace("[","{")
ee = ee.replace("]","}")

file.write(ee)
file.close()
