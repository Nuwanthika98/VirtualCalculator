# importing packages
import cv2

# importing the hand tracking module in the cvzone
from cvzone.HandTrackingModule import HandDetector

# adding webcam
cap = cv2.VideoCapture(0)

# loop
while True:
    # get image from webcam
    success, img = cap.read()

