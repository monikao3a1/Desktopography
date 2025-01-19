import cv2
import mediapipe as mp

def perform_hand_tracking(color_image):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    # Convert color image to RGB format
    color_image_rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

    # Perform hand tracking using MediaPipe
    results = hands.process(color_image_rgb)
    
    if results.multi_hand_landmarks:
        # Rest of the code for hand landmark detection and drawing landmarks on the image
        ...
    
    # Return the color image with hand landmarks drawn
    return color_image
