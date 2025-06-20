import cv2
import numpy as np
import os

def detect_and_blur_watermark(image_path, output_path, overlay_logo_path=None):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not read image from {image_path}")
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Apply blur only if contour area is large enough
        if w * h > 150: # <--- THIS IS THE PROBLEMATIC LINE. YOU MUST MANUALLY RETYPE IT.
            roi = img[y:y+h, x:x+w]
            blurred = cv2.GaussianBlur(roi, (23, 23), 30)
            img[y:y+h, x:x+w] = blurred

    # ... (rest of the code as previously provided)
