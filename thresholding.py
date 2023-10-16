import cv2
import numpy as np

# Read the input image
img = cv2.imread(r'C:\Users\v23ASayed2\Desktop\Vodafone\national IDs\IDs\202212_C_2021011_3_01065773743_1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set the threshold value
threshold_value = 128

# Threshold the image
ret, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Create a binary mask by applying a morphological open operation to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Invert the mask
mask = cv2.bitwise_not(mask)

# Apply the mask to the original image to segment the colored objects
color = (0, 0, 255)  # Color for the segmented objects (in BGR format)
result = cv2.bitwise_and(img, img, mask=mask)
result[mask == 0] = color

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()