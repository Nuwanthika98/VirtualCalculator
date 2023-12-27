import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 50), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        4, (0, 0, 0), 5)
            return True
        else:
            return False


# Buttons
buttonListValues = [['7', '8', '9', '='],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '*', 'AC', '/']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 70 + 280
        ypos = y * 70 + 80

        buttonList.append(Button((xpos, ypos), 75, 75, buttonListValues[y][x]))

# Variables
myEquation = ''
delayCounter = 0

# Webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw Answer box
    cv2.rectangle(img, (280, 5), (280 + 285, 5 + 70),
                  (225, 225, 225), cv2.FILLED)

    cv2.rectangle(img, (280, 5), (280 + 285, 5 + 70),
                  (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    # Check for Hand
    if hands:
        # Find distance between fingers
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        print(length)
        x, y = lmList[8]

        # If clicked check which button and perform action
        if length < 48 and delayCounter == 0:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y):
                    myValue = buttonListValues[int(i % 4)][int(i / 4)]  # get correct number
                    if myValue == 'AC':
                        myEquation = ''
                    elif myValue == '=':
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # to avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Write the Final answer
    cv2.putText(img, myEquation, (280, 60), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 0, 0), 3)

    # Display
    key = cv2.waitKey(1)
    cv2.imshow("Image", img)


    #Stop calculator
    if key==ord('c'):
        cap.release()
