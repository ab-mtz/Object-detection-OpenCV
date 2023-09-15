import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound

# Code to open a picture
video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw.bbox(frame, bbox, label, conf)

    cv2.imshow("object detection", frame)

    for item in label:
        if item in labels:
            pass
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
vid.realease()

cv2.destroyAllWindows()
