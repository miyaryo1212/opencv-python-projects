import cv2

img = cv2.imread("./images/doge.jpg")

cv2.imshow("doge", img)
cv2.waitKey(0)