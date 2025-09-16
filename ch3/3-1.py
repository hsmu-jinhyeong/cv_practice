import cv2 as cv
import sys

img = cv.imread(r"C:\Users\kim\test\ch3\soccer.jpg")


if img is None:
    sys.exit("Could not read the image.")

cv.imshow('original', img)
cv.imshow('Upper left half', img[0:img.shape[0]//2, 0:img.shape[1]//2,:])
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,:])

cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()