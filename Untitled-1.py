import cv2
import pyautogui
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, image = cap.read()
    cv2.imshow("Volume",image)
    rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output = hand.process(rgb)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)
    key = cv2.waitKey(10)
    if key == 27:
        break
cap.release()