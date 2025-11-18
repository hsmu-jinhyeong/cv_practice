import cv2 as cv
import mediapipe as mp
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

img=cv.imread(r'C:\Users\kim\cv_practice\cv10\data\tennis.jpg')

mp_face_detection=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils

face_detection=mp_face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
res=face_detection.process(cv.cvtColor(img,cv.COLOR_BGR2RGB))

if not res.detections:
    print('얼굴 검출에 실패했습니다. 다시 시도하세요.')
else:
    for detection in res.detections:
        mp_drawing.draw_detection(img,detection)
    cv.imshow('Face detection by MediaPipe',img)

cv.waitKey()
cv.destroyAllWindows()