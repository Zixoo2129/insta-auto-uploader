import cv2
import numpy as np

def detect_and_blur_watermark(image_path, output_path, overlay_logo_path=None):
    img = cv2.imread(image_path)

    # Convert to grayscale for detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Basic watermark detection using thresholding
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Find contours of bright areas (likely watermark text/logos)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Apply blur only if contour area is large enough
        if w * h > 150:
            roi = img[y:y+h, x:x+w]
            blurred = cv2.GaussianBlur(roi, (23, 23), 30)
            img[y:y+h, x:x+w] = blurred

    # Optional overlay (your logo)
    if overlay_logo_path:
        logo = cv2.imread(overlay_logo_path, cv2.IMREAD_UNCHANGED)
        if logo is not None:
            logo = cv2.resize(logo, (100, 100))
            y_offset, x_offset = 10, img.shape[1] - 110
            for c in range(3):
                img[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1], c] = logo[:, :, c]

    # Save output
    cv2.imwrite(output_path, img)
