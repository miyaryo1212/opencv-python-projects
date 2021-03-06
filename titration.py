# Import only if not previously imported
import cv2
import sys
import numpy as np

from cv2 import rectangle
# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file
cap = cv2.VideoCapture(0)

videoWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
videoHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
videoFPS = int(cap.get(cv2.CAP_PROP_FPS))

print(f'''{"Width: "}{videoWidth}
{"Height: "}{videoHeight}
{"FPS: "}{videoFPS}''')

rectangleFromX = int(videoWidth / 2 - videoWidth / 25)
rectangleFromY = int(videoHeight * 4 / 5 - videoHeight / 30)
rectangleToX = int(videoWidth / 2 + videoWidth / 25)
rectangleToY = int(videoHeight * 4 / 5 + videoHeight / 30)

boxFromX = rectangleFromX + 1
boxFromY = rectangleFromY + 1
boxToX = rectangleToX - 1
boxToY = rectangleToY - 1

if cap.isOpened() == False:
    print("Error in opening video stream or file")
    sys.exit()

while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    frame_bgr = img
    frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ### BGR形式での処理 ###

    imgBox = frame_bgr[boxFromY: boxToY, boxFromX: boxToX]
    b = imgBox.T[0].flatten().mean()
    g = imgBox.T[1].flatten().mean()
    r = imgBox.T[2].flatten().mean()

    targetColor_b = 0
    targetColor_g = 0
    targetColor_r = 255

    cv2.rectangle(frame_bgr, (videoWidth - 130, videoHeight - 90),
                  (videoWidth - 20, videoHeight-20), (195, 195, 195), thickness=-1)
    cv2.rectangle(frame_bgr, (videoWidth - 75, videoHeight - 75),
                  (videoWidth - 35, videoHeight - 35), (b, g, r), thickness=-1)
    cv2.rectangle(frame_bgr, (videoWidth - 115, videoHeight - 75),
                  (videoWidth - 75, videoHeight - 35), (targetColor_b, targetColor_g, targetColor_r), thickness=-1)
    cv2.rectangle(frame_bgr, (rectangleFromX, rectangleFromY),
                  (rectangleToX, rectangleToY), (0, 255, 0))

    ### HSV形式での処理 ###

    lower = np.array([90, 64, 0])
    upper = np.array([150, 255, 255])

    frame_mask = cv2.inRange(frame_hsv, lower, upper)

    dst = cv2.bitwise_and(img, img, mask=frame_mask)

    if ret:
        cv2.imshow("Video - BGR", frame_bgr)
        cv2.imshow("Video - HSV", frame_hsv)
        cv2.imshow("img", dst)

        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
