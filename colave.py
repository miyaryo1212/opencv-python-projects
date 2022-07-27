# calc color average
import cv2
import os

img = cv2.imread(".\images\doge.jpg", cv2.IMREAD_COLOR)

boxFromX = 20
boxFromY = 40
boxToX = 80
boxToY = 60

imgBox = img[boxFromY: boxToY, boxFromX: boxToX]

b = imgBox.T[0].flatten().mean()
g = imgBox.T[1].flatten().mean()
r = imgBox.T[2].flatten().mean()

print("B: %.2f" % (b))
print("G: %.2f" % (g))
print("R: %.2f" % (r))

imgBoxHsv = cv2.cvtColor(imgBox,cv2.COLOR_BGR2HSV)

h = imgBoxHsv.T[0].flatten().mean()
s = imgBoxHsv.T[1].flatten().mean()
v = imgBoxHsv.T[2].flatten().mean()

print("Hue: %.2f" % (h))
print("Salute: %.2f" % (s))
print("Value: %.2f" % (v))