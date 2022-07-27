import cv2

img = cv2.imread("./images/doge.jpg")

img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("doge", img_rotate)
cv2.waitKey(0)