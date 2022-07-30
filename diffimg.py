import cv2 as cv
img1 = cv.imread(".\images\img1.jpg")
img2 = cv.imread(".\images\img2.jpg")
img_diff = cv.absdiff(img1, img2)
cv.imwrite("diff.jpg", img_diff)