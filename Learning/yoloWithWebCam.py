from ultralytics import YOLO
import cv2 as cv
import cvzone 
import math

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4, 480)

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


model =YOLO('../yolo-weights/yolov8n.pt')

while True:
    success,img = cap.read()
    results = model(img,stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            bbox =[x1,y1,x2,y2]
            #print(x1,y1,x2,y2)

            #cv.rectangle(img,(x1,y1),(x2,y2),thickness=2,color=(255,0,255))
            cvzone.cornerRect(img,bbox=bbox,rt=2,t=3)
            conf = box.conf[0]
            cls =int(box.cls[0])
            label=classNames[cls]
            #conf1 = math.ceil((box.conf[0]*100)/100)
            conf = float(box.conf[0])          # tensor → float
            conf_percent = conf_percent = round(conf * 100, 2)

            

            print("confidence:" ,math.ceil((box.conf[0]*100)/100))
            cvzone.putTextRect(img,f'{label ,conf_percent}',(max(0,x1),max(35,y1)))


    cv.imshow("image",img)
    cv.waitKey(1)