import os
import cv2

# read image
image_path = os.path.join('.','data','cat.jpg')

img = cv2.imread(image_path)

# Write image

cv2.imwrite(os.path.join('.','data','cat_out.jpg'),img)

# visualize image
cv2.imshow('cat', img)
cv2.waitKey(5000)