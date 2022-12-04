import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
# import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,h,w = hand['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w


        if aspectRatio >1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap]= imgResize

        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite", imgWhite)


    cv2.imshow("Image", img)
    cv2.waitKey(1)