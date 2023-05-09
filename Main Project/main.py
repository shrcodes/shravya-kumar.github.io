import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

brushThickness = 8
eraserThickness = 50
shape = "freestyle"

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]

#default color
drawColor = (255, 0, 0)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 650)
detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((700,800 ,3), np.uint8)


while True:
    # 1.import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!=0:
        #print(lmList)

        #tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        x0, y0 = lmList[4][1:]

        # 3. check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        # 4. If Selection mode - Two fingers are up
        #xp, yp = 0, 0
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")

            #Checking for the click
            if y1 < 90:
                if 9 < x1 < 100:
                    drawColor = (255, 0, 0)
                    if shape == 'freestyle':
                        header = overlayList[0]
                    elif shape == 'circle':
                        header = overlayList[6]
                    elif shape == 'rectangle':
                        header = overlayList[7]
                    elif shape == 'ellipse':
                        header = overlayList[8]
                elif 160 < x1 < 240:
                    drawColor = (0, 0, 255)
                    if shape == 'freestyle':
                        header = overlayList[10]
                    elif shape == 'circle':
                        header = overlayList[11]
                    elif shape == 'rectangle':
                        header = overlayList[12]
                    elif shape == 'ellipse':
                        header = overlayList[13]
                elif 300 < x1 < 390:
                    drawColor = (0, 255, 0)
                    if shape == 'freestyle':
                        header = overlayList[1]
                    elif shape == 'circle':
                        header = overlayList[2]
                    elif shape == 'rectangle':
                        header = overlayList[3]
                    elif shape == 'ellipse':
                        header = overlayList[4]
                elif 462 < x1 < 630:
                    header = overlayList[5]
                    drawColor = (0, 0, 0)

            if y1 > 95 and y1 < 148:
                #if x1 < 15:
                 #   header = overlayList[9]

                if 5 < x1 < 90 and drawColor == (255, 0, 0):
                    header = overlayList[0]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (255, 0, 0):
                    header = overlayList[6]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (255, 0, 0):
                    header = overlayList[7]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (255, 0, 0):
                    header = overlayList[8]
                    shape = 'ellipse'
                elif 5 < x1 < 90 and drawColor == (0, 0, 255):
                    header = overlayList[10]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (0, 0, 255):
                    header = overlayList[11]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (0, 0, 255):
                    header = overlayList[12]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (0, 0, 255):
                    header = overlayList[13]
                    shape = 'ellipse'
                if 5 < x1 < 90 and drawColor == (0, 255, 0):
                    header = overlayList[1]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (0, 255, 0):
                    header = overlayList[2]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (0, 255, 0):
                    header = overlayList[3]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (0, 255, 0):
                    header = overlayList[4]
                    shape = 'ellipse'
            cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), drawColor, cv2.FILLED)

        # 5. if Drawing mode - index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                if shape == 'freestyle':
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)


                xp, yp = x1, y1
                #draw
                if shape == 'freestyle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    if u <= 25:
                        cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
                        cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.putText(img, str(u), (500,650 ), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str("brushThickness="), (0, 650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(int(brushThickness)), (450, 650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

                # Rectangle
                elif shape == 'rectangle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.rectangle(img, (x0, y0), (x1, y1), drawColor)
                    cv2.putText(img, "Length of Diagonal = ", (0,650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(u), (530, 650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)//530,700
                    if fingers[4]:
                        cv2.rectangle(imgCanvas, (x0, y0), (x1, y1), drawColor)


                # Circle
                elif shape == 'circle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.putText(img, "Radius Of Circe = ", (0, 650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)//0,700
                    cv2.putText(img, str(u), (450, 650), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)//450,700
                    cv2.circle(img, (x0, y0), u, drawColor)
                    if fingers[4]:
                        cv2.circle(imgCanvas, (x0, y0), u, drawColor)

                # Ellipse
                if shape == 'ellipse':
                    z1, z2 = lmList[4][1:]
                    # cv2.ellipse(img,(x1,y1),(int(z1/2),int(z2/2)),0,0,360,255,0)
                    a = z1 - x1
                    b = (z2 - x2)
                    if x1 > 250:
                        b = int(b / 2)
                    if a < 0:
                        a = -1 * a
                    if b < 0:
                        b = -1 * b
                    cv2.ellipse(img, (x1, y1), (a, b), 0, 0, 360, drawColor)
                    cv2.putText(img, "Major AL, Minor AL = ", (0, 640), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(a), (550, 640), cv2.FONT_HERSHEY_PLAIN, 3, (123, 20, 255), 3)
                    cv2.putText(img, str(b), (640, 640), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    if fingers[4]:
                        cv2.ellipse(imgCanvas, (x1, y1), (a, b), 0, 0, 360, drawColor)

            xp, yp = x1, y1

            # Clear Canvas when 2 fingers are up
            if fingers[2] and fingers[3] and fingers[0] == 0 and fingers[1] == 0 and fingers[4] == 0:
                imgCanvas = np.zeros((500, 640, 3), np.uint8)//720,1280

    '''imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)'''

    # Setting header image
    img[0:148, 0:640] = header
    #imgCanvas = cv2.resize(img2, (720, 1280))
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Air Canvas", img)
    cv2.imshow("Black Board", imgCanvas)
    #cv2.imshow("Inverse", imgInv)
    cv2.waitKey(1)

'''import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

brushThickness = 8
eraserThickness = 50
shape = "freestyle"

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[0]

#default color
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.handDetector(detectionCon=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)


while True:
    # 1.import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!=0:
        #print(lmList)

        #tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        x0, y0 = lmList[4][1:]

        # 3. check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        # 4. If Selection mode - Two fingers are up
        #xp, yp = 0, 0
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")

            #Checking for the click
            if y1 < 90:
                if 9 < x1 < 86:
                    header = overlayList[0]
                    drawColor = (255, 0, 0)
                elif 174 < x1 < 240:
                    header = overlayList[10]
                    drawColor = (0, 0, 255)
                elif 300 < x1 < 390:
                    header = overlayList[1]
                    drawColor = (0, 255, 0)
                elif 462 < x1 < 630:
                    header = overlayList[5]
                    drawColor = (0, 0, 0)

            if y1 > 95 and y1 < 148:
                if x1 < 15:
                    header = overlayList[1]

                elif 5 < x1 < 90 and drawColor == (255, 0, 255):
                    header = overlayList[0]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (255, 0, 255):
                    header = overlayList[6]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (255, 0, 255):
                    header = overlayList[7]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (255, 0, 255):
                    header = overlayList[8]
                    shape = 'elipse'
                elif 5 < x1 < 90 and drawColor == (255, 0, 0):
                    header = overlayList[10]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (255, 0, 0):
                    header = overlayList[11]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (255, 0, 0):
                    header = overlayList[12]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (255, 0, 0):
                    header = overlayList[13]
                    shape = 'elipse'
                if 5 < x1 < 90 and drawColor == (0, 255, 0):
                    header = overlayList[1]
                    shape = 'freestyle'
                elif 162 < x1 < 240 and drawColor == (0, 255, 0):
                    header = overlayList[2]
                    shape = 'circle'
                elif 315 < x1 < 396 and drawColor == (0, 255, 0):
                    header = overlayList[3]
                    shape = 'rectangle'
                elif 515 < x1 < 604 and drawColor == (0, 255, 0):
                    header = overlayList[4]
                    shape = 'elipse'
            cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), drawColor, cv2.FILLED)

        # 5. if Drawing mode - index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)


                xp, yp = x1, y1
                #draw
                if shape == 'freestyle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    if u <= 25:
                        cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
                        cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.putText(img, str(u), (600, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str("brushThickness="), (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(int(brushThickness)), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

                # Rectangle
                elif shape == 'rectangle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.rectangle(img, (x0, y0), (x1, y1), drawColor)
                    cv2.putText(img, "Length of Diagonal = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(u), (530, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    if fingers[4]:
                        cv2.rectangle(imgCanvas, (x0, y0), (x1, y1), drawColor)


                # Circle
                elif shape == 'circle':
                    z1, z2 = lmList[4][1:]
                    # print(z1,z2)
                    result = int(((((z1 - x1) ** 2) + ((z2 - y1) ** 2)) ** 0.5))
                    # print(result)
                    if result < 0:
                        result = -1 * result
                    u = result
                    cv2.putText(img, "Radius Of Circe = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(u), (450, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.circle(img, (x0, y0), u, drawColor)
                    if fingers[4]:
                        cv2.circle(imgCanvas, (x0, y0), u, drawColor)

                # Ellipse
                if shape == 'elipse':
                    z1, z2 = lmList[4][1:]
                    # cv2.ellipse(img,(x1,y1),(int(z1/2),int(z2/2)),0,0,360,255,0)
                    a = z1 - x1
                    b = (z2 - x2)
                    if x1 > 250:
                        b = int(b / 2)
                    if a < 0:
                        a = -1 * a
                    if b < 0:
                        b = -1 * b
                    cv2.ellipse(img, (x1, y1), (a, b), 0, 0, 360, 255, 0)
                    cv2.putText(img, "Major AL, Minor AL = ", (0, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    cv2.putText(img, str(a), (550, 700), cv2.FONT_HERSHEY_PLAIN, 3, (123, 20, 255), 3)
                    cv2.putText(img, str(b), (700, 700), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                    if fingers[4]:
                        cv2.ellipse(imgCanvas, (x1, y1), (a, b), 0, 0, 360, 255, 0)

            xp, yp = x1, y1

            # Clear Canvas when 2 fingers are up
            if fingers[2] and fingers[3] and fingers[0] == 0 and fingers[1] == 0 and fingers[4] == 0:
                imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)////////////////
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)/////////////////

    # Setting header image
    img[0:148, 0:640] = header
    #imgCanvas = cv2.resize(img2, (720, 1280))
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Air Canvas", img)
    cv2.imshow("Black Board", imgCanvas)
    #cv2.imshow("Inverse", imgInv)
    cv2.waitKey(1)'''

