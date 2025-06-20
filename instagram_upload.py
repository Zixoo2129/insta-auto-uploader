import os
import requests
from dotenv import load_dotenv

load_dotenv()

IG_COOKIES = os.getenv("IG_COOKIES")

def upload_photo_to_instagram(image_path, caption):
    headers = {
        "User-Agent": "Instagram 123.0.0.21.114",
        "Cookie": IG_COOKIES
    }

    upload_url = "https://www.instagram.com/create/upload/photo/"
    with open(image_path, 'rb') as f:
        files = {'photo': f}
        response = requests.post(upload_url, files=files, headers=headers)

    if response.status_code == 200:
        print("✅ Uploaded to Instagram")
    else:
        print(f"❌ Upload failed. Status code: {response.status_code}")
        print(response.text)
