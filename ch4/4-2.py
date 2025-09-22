import cv2 as cv

img=cv.imread(r"C:\Users\kim\cv_practice\ch3\soccer.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray,50,150)
canny2=cv.Canny(gray,75,175)

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)

cv.waitKey(0)
cv.destroyAllWindows()