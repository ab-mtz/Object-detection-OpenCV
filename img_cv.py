import sys
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from IPython.display import Image, display

def main():
    print(sys.argv[1])
    filename = sys.argv[1]
    object_detection_with_bounding_boxes(filename)

def object_detection_with_bounding_boxes(filename, model="yolov3", confidence=0.2):
    # Read the image into a numpy array
    img = cv2.imread(filename)
     
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
     
    # Print current image's filename
    print(f"========================\nImage processed: {filename}\n")
     
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}\n")
     
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)
     
    # Save the image in the directory images_with_boxes
    cv2.imwrite(f'images_with_boxes/{filename}', output_image)
     
    # Display the image with bounding boxes
    display(Image(f'images_with_boxes/{filename}'))

if __name__ == '__main__':
    main()
