import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
from cv2 import LINE_4

img = cv2.imread("./images/doge.jpg")

cv2.putText(img,
            text="HERE IS DOGE",
            org=(100, 300),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4,)

cv2.imshow("Window", img)
cv2.waitKey(0)