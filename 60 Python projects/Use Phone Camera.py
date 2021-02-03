import cv2
import numpy

url="http://192.168.l.6:8888"

cp=cv2.VideoCapture(url)

while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
