import cv2
import numpy as  np

def detect_rectangle_contour(frames, color_frame):
    if not color_frame:
        return

    # Convert the color frame to OpenCV format
    color_image = np.asanyarray(color_frame.get_data())

    # TODO: Perform projection mapping and obtain the projected rectangle

    # Detect the rectangle in the color image
    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Filter out small contours
        if cv2.contourArea(contour) > 500:
            # TODO: Perform further processing to identify the rectangle if necessary
            x, y, w, h = cv2.boundingRect(contour)

            # Draw the rectangle with green borders
            cv2.rectangle(color_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Print the coordinates of the corners
            print("Coordinates of the corners:")
            print(f"Top-left: ({x}, {y})")
            print(f"Top-right: ({x + w}, {y})")
            print(f"Bottom-left: ({x}, {y + h})")
            print(f"Bottom-right: ({x + w}, {y + h})")

    # Display the color image with the projected rectangle
    cv2.imshow("RealSense", color_image)
    return x,y,w,h
