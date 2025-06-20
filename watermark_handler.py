import cv2
import numpy as np
import os

# Load your watermark image
WATERMARK_PATH = "your_watermark.png"  # make sure this file exists in your project

def overlay_watermark(base_image_path, save_path):
    try:
        image = cv2.imread(base_image_path)
        watermark = cv2.imread(WATERMARK_PATH, cv2.IMREAD_UNCHANGED)

        if image is None or watermark is None:
            print("Error loading image or watermark.")
            return base_image_path  # fallback

        (h_img, w_img) = image.shape[:2]
        (h_wm, w_wm) = watermark.shape[:2]

        # Resize watermark to 1/5 of image width
        scale = w_img // 5
        scale_ratio = scale / w_wm
        new_w = int(w_wm * scale_ratio)
        new_h = int(h_wm * scale_ratio)
        watermark = cv2.resize(watermark, (new_w, new_h))

        # Position: top-right corner
        x_offset = w_img - new_w - 10
        y_offset = 10

        # Overlay watermark
        overlay = image.copy()

        for c in range(0, 3):  # for each color channel
            overlay[y_offset:y_offset+new_h, x_offset:x_offset+new_w, c] = \
                watermark[:, :, c] * (watermark[:, :, 3] / 255.0) + \
                overlay[y_offset:y_offset+new_h, x_offset:x_offset+new_w, c] * (1.0 - watermark[:, :, 3] / 255.0)

        cv2.imwrite(save_path, overlay)
        return save_path

    except Exception as e:
        print(f"Error during watermarking: {e}")
        return base_image_path


def process_media(input_path):
    # Generate output filename
    base, ext = os.path.splitext(input_path)
    output_path = base + "_processed" + ext

    # Apply overlay
    result_path = overlay_watermark(input_path, output_path)
    return result_path
