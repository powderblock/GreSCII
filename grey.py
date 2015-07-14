import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1], 0)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
