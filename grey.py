import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])

print "Red for pixel at 100, 100: " + str(img[100, 100, 2])
print "Green for pixel at 100, 100: " + str(img[100, 100, 1])
print "Blue for pixel at 100, 100: " + str(img[100, 100, 0])

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
