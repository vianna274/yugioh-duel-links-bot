# import the necessary packages
import numpy as np
import argparse
import cv2

# load the image and convert it to grayscale
image = cv2.imread("images/searchingImage.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)

# display the results of the naive attempt
cv2.imshow("Naive", image)

# apply a Gaussian blur to the image then find the brightest
# region
#gray = cv2.GaussianBlur(gray, (100, 100), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, 15, (255, 0, 0), 2)
print (maxLoc)
# display the results of our newly improved method
cv2.imshow("Robust", image)
cv2.waitKey(0)
if maxLoc[0] > 10:
	print ("EOQ")
