import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])

width = img.shape[0]
height = img.shape[1]

# 'brightness' ASCII characters
# From darkest to brightest.
chars = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
ascii = []

# Function to take in a pixel's color values
def turnIntoGrey(red, green, blue):
    # Output a grey version of this pixel
    return (0.2126 * red) + (.7152 * green) + (0.0722 * blue)

# For every pixel in the image:
for i in range(width):
    for j in range(height):
        red = img[i, j, 2]
        green = img[i, j, 1]
        blue = img[i, j, 0]
        grey = turnIntoGrey(red, green, blue)
        img.itemset((i, j, 2), grey)
        img.itemset((i, j, 1), grey)
        img.itemset((i, j, 0), grey)
        ascii.append(chars[int(round(grey, 0)) / 28])
    ascii.append("\n")

output = open("ascii.txt", "w+")

# Go through each element in ascii list:
for i in range(len(ascii)):
    # Write it to ascii.txt:
    output.write(ascii[i])

output.close()
