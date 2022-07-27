import cv2

img = cv2.imread("./images/doge.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("doge", img_gray)
cv2.waitKey(0)