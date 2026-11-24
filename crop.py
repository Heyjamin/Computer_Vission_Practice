# crop

import os

import cv2

img = cv2.imread(os.path.join('.','data','cat.jpg'))

# def mouse_callback(event, x, y, flags, param):
#    if event == cv2.EVENT_MOUSEMOVE:
#         print(f"X: {x} | Y: {y}")

print(img.shape)

cropped_img = img[220:1100,470:1700]


cv2.imshow('img',img)
#cv2.setMouseCallback("img", mouse_callback)
cv2.imshow('cropped_img',cropped_img)
cv2.waitKey(0)
