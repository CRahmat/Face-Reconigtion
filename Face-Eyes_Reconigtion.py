import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    line = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = face.detectMultiScale(line, 1.3, 5)
    for(x, y, k ,l)in wajah:
        cv2.rectangle(frame, (x, y), (x+k, y+l), (0,255,0), 4)
        roi_warna = frame[y:y + l, x:x + k]
        roi_line = line[y:y + l, x:x + k]
        mata = eye.detectMultiScale(roi_warna, 1.5, 3)
        for (x1, y1, k1, l1) in mata:
            cv2.rectangle(roi_warna, (x1, y1), (x1 + k1, y1 + l1), (255, 255, 0), 3)
    cv2.imshow("Face Reconigtion ",frame)
    exit = cv2.waitKey(1) & 0xff
    if exit == ord('x'):
        break
cv2.destroyAllWindows()
video.release()