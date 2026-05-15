from ultralytics import YOLO
import cv2 as cv
import cvzone 
import math
from sort import*

#cap = cv.VideoCapture(0)
#cap.set(3,640)
#cap.set(4, 480)
cap = cv.VideoCapture(r"D:\YOLO\Learning\videos\video1.mp4")


classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
    "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
    "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
    "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
    "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote",
    "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book",
    "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]


model =YOLO('yolov8n.pt')

tracker= Sort(max_age=5,min_hits=3,iou_threshold=0.3)

limits = [0,297,1280,297]

leftcount = set()
rightcount =set()


while cap.isOpened():
    success,img = cap.read()
    if not success:
        break

    results = model(img,stream=True)
    detections = np.empty((0,5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = map(int,box.xyxy[0])

            bbox =[x1,y1,x2,y2]
            #print(x1,y1,x2,y2)

            #cv.rectangle(img,(x1,y1),(x2,y2),thickness=2,color=(255,0,255))
            #conf = box.conf[0]
            cls =int(box.cls[0])
            label=classNames[cls]
            #conf1 = math.ceil((box.conf[0]*100)/100)

            conf = float(box.conf[0])          # tensor → float
            conf_percent = conf_percent = round(conf * 100, 2)

            if (label in ["car", "truck", "motorbike"]) and conf > 0.3:

                #cvzone.putTextRect(img,f'{label}',(max(0,x1),max(35,y1)))
                # cvzone.cornerRect(img,bbox=bbox,rt=5,t=3,l=9)

                currentarray= np.array([x1,y1,x2,y2,conf])
                detections= np.vstack((detections,currentarray))


            #print("confidence:" ,math.ceil((box.conf[0]*100)/100))
    resultstracker=tracker.update(detections)

    cv.line(img,(limits[0],limits[1]),(limits[2],limits[3]),color=(0,0,255),thickness=5)

    for result in resultstracker:

        x1,y1,x2,y2,ID= result
        x1,y1,x2,y2 =map(int , [x1,y1,x2,y2])
        w = x2 - x1
        h = y2 - y1

        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255,0,0))
        cx,cy= x1+w//2,y1+h//2
        cv.circle(img,(cx,cy),5,(0,0,255),cv.FILLED)

        if limits[0]<cx<limits[2]//2 and limits[1]-30<cy<limits[1]+30 :
                if ID not in leftcount :
                     leftcount.add(ID)
        if limits[0]//2<cx<limits[2] and limits[1]-30<cy<limits[1]+30 :
                if ID not in leftcount :
                     rightcount.add(ID)


                #cv.line(img,(limits[0],limits[1]),(limits[2],limits[3]),color=(0,255,0),thickness=5)
        #cvzone.cornerRect(img,(x1,y1,x2,y2),l=9,rt=2,colorR=(255,0,0))


    cvzone.putTextRect(img, f' IN: {len(leftcount)} OUT: {len(rightcount)}', (120, 640))

        #print(result)
    
    
    #print(totalcount)
    cv.imshow("image",img)
    
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv.destroyAllWindows()