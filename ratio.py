import numpy as np
import argparse
import imutils
import cv2

image = cv2.imread(r'C:\Users\v23ASayed2\Desktop\Vodafone\contour approximation\0_back.jpg')
ratio_in_x = image.shape[0]/ 360
print(ratio_in_x)
print(image.shape[0])