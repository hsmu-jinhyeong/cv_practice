import cv2 as cv
import sys

img = cv.imread(r"C:\Users\kim\test\ch3\rose.png")

if img is None:
    sys.exit("Could not read the image.")

ix, iy = -1, -1  # 시작 좌표 초기화

def draw(event, x, y, flags, param):
    global ix, iy, img

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y  # 시작 좌표 저장

    elif event == cv.EVENT_LBUTTONUP:
        # ROI 추출
        x1, y1, x2, y2 = min(ix, x), min(iy, y), max(ix, x), max(iy, y)
        patch = img[y1:y2, x1:x2, :]

        if patch.size == 0:  # 빈 ROI 방지
            return

        # 원본에 사각형 그리기
        cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # 다양한 보간법으로 리사이즈
        patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

        # 결과 출력
        cv.imshow('Resize - Nearest', patch1)
        cv.imshow('Resize - Bilinear', patch2)
        cv.imshow('Resize - Bicubic', patch3)

    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):  # q 키 누르면 종료
        cv.destroyAllWindows()
        break
