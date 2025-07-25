import os
import requests
from dotenv import load_dotenv

load_dotenv()

IG_COOKIES = os.getenv("IG_COOKIES")

HEADERS = {
    "cookie": IG_COOKIES,
    "user-agent": "Mozilla/5.0",
}

def upload_reel(video_path, caption, cover_image_path=None):
    print("⚠️ Reel upload placeholder — Instagram doesn't allow Reels via public API.")
    print("To upload reels, you must use browser automation (Selenium + Cookie login).")
    print(f"Video: {video_path}")
    print(f"Caption: {caption}")
    print(f"Cover Image: {cover_image_path if cover_image_path else 'Default'}")

    # Placeholder: Real reel upload must be done via automated browser (selenium)
    return False
