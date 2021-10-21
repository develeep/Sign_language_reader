import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Camera open failed!")
    exit()
frameRate = 33
while True:
    retval, frame = cap.read()
    if not(retval):
        break
    cv.imshow('frame', ~frame)
    key = cv.waitKey(frameRate)

    if key == 27:
        break
if cap.isOpened():
    cap.release()
cv.destroyAllWindows()
