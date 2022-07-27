import cv2

img = cv2.imread("./images/doge.jpg")

img_resize = cv2.resize(img, (200, 200))

cv2.imshow("doge", img_resize)
cv2.waitKey(0)