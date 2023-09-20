import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound

# Code to open webcam
video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    #Testing ret
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("object_detection", output_image)

   

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
print(labels)

