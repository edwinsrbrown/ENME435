import numpy as np
import matplotlib
import cv2
import imutils

print("All packages imported properly!")

image = cv2.imread("testudo.jpg")
cv2.imshow("Caption here", image)

# resizing image with imutls
image_resized = imutils.resize(image, width=400)
cv2.imshow("Resized Testudo", image_resized)

cv2.waitKey(0) # so the image doesn't just appear and disappear
