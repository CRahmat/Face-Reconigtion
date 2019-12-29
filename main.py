import cv2
#DETECTED IMAGE
#Read face from image
#img = cv2.imread('photo-test.jpg',100)
#edge = hasil convert ke edge
#Semakin besar nilainya maka keakuratan akan berkurang
#edge = cv2.Canny(img, 50,50)
#cv2.imshow('Deceted Edge',edge)
#cv2.imshow('Original',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#DETECTED VIDEOS
video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()

    edge = cv2.Canny(frame, 100, 100)

    cv2.imshow("Face-Reconigtion", edge)

    exit = cv2.waitKey(1) & 0xff

    if exit == ord('x'):
        break
cv2.destroyAllWindows()
video.release()