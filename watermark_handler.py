import cv2
import numpy as np
import os

def detect_and_blur_watermark(image_path, output_path, overlay_logo_path=None):
    img = cv2.imread(image_path)

    if img is None:
        print(f"❌ Error: Could not read image from {image_path}")
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        [span_20](start_span)if w * h > 150:[span_20](end_span)
            roi = img[y:y+h, x:x+w]
            blurred = cv2.GaussianBlur(roi, (23, 23), 30)
            img[y:y+h, x:x+w] = blurred

    if overlay_logo_path:
        logo = cv2.imread(overlay_logo_path, cv2.IMREAD_UNCHANGED)
        [span_21](start_span)if logo is not None:[span_21](end_span)
            logo_height, logo_width = logo.shape[:2]
            img_height, img_width = img.shape[:2]

            target_width = 100
            target_height = int(logo_height * (target_width / logo_width))
            if target_height > 100:
                target_height = 100
                target_width = int(logo_width * (target_height / logo_height))

            logo = cv2.resize(logo, (target_width, target_height), interpolation=cv2.INTER_AREA)

            y_offset, x_offset = 10, img_width - logo.shape[1] - 10

            if y_offset + logo.shape[0] > img_height or x_offset + logo.shape[1] > img_width:
                print("⚠️ Warning: Logo might be too large for the image. Placing partially or not at all.")

            if logo.shape[2] == 4: # RGBA (with transparency)
                alpha_s = logo[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s

                for c in range(0, 3):
                    img[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1], c] = \
                        (alpha_s * logo[:, :, c] +
                         alpha_l * img[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1], c])
            else: # RGB (no transparency)
                img[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1]] = logo[:, :, :3]
        else:
            print(f"❌ Error: Could not read overlay logo from {overlay_logo_path}")

    cv2.imwrite(output_path, img)
    return True

def process_media(file_path):
    base, ext = os.path.splitext(file_path)
    output_file_path = f"{base}_processed{ext}"

    # You should set this in your .env file
    your_overlay_logo_path = os.getenv("OVERLAY_LOGO_PATH", None)

    if detect_and_blur_watermark(file_path, output_file_path, your_overlay_logo_path):
        print(f"[🖼️] Media processed and saved to {output_file_path}")
        return output_file_path
    else:
        print(f"[❌] Failed to process media: {file_path}")
        return None
