import numpy as np
import cv2
from keras.models import load_model
from yolo_utils import infer_image, show_image
import imutils

class ALPR:
    """
    Class that c...
    """

    def __init__(self, frame, height, width):
        self.net = cv2.dnn.readNetFromDarknet('yolo.cfg', 'yolov3.weights')
        # Get the labels
        self.labels = open('coco-labels').read().strip().split('\n')
        # Intializing colors to represent each label uniquely
        self.colors = np.random.randint(0, 255, size=(len(self.labels), 3), dtype='uint8')
        self.layer_names = self.net.getLayerNames()
        self.layer_names = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.frame = frame
        self.height = height
        self.width = width


    def infer(self, frame):
        self.frame, _, _, _, _ = infer_image(self.net, self.layer_names, self.height, self.width, frame, self.colors, self.labels)
        return self.frame
