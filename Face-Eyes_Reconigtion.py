import cv2
#algoritma face dan eyes
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

#Mengambil Video dari WebCam
video = cv2.VideoCapture(0)
#Karena sebenarnya video merupakan gambar yang bergerak maka digunakan perulangan
#Agar gambar yang di tampilkan dapat real-time
while True:
    _, frame = video.read()
    line = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    wajah = face.detectMultiScale(line, 1.2, 5)
    for(x, y, k ,l)in wajah:
        #cv2.rectangle(image, start-point, end-point, color, thickless
        cv2.rectangle(frame, (x, y), (x+k, y+l), (0,255,0), 3)
        roi_warna = frame[y:y + l, x:x + k]
        roi_line = line[y:y + l, x:x + k]
        mata = eye.detectMultiScale(roi_warna, 1.2, 6)
        for (x1, y1, k1, l1) in mata:
            cv2.rectangle(roi_warna, (x1, y1), (x1 + k1, y1 + l1), (255, 255, 0), 3)
    cv2.imshow("Face Reconigtion ",frame)
    exit = cv2.waitKey(5) & 0xff
    if exit == ord('x'):
        break
cv2.destroyAllWindows()
video.release()