import os
import requests
from dotenv import load_dotenv

load_dotenv()

# This line reads the cookie string from your .env file
IG_COOKIES = os.getenv("IG_COOKIES")

def upload_photo_to_instagram(image_path, caption):
    if not IG_COOKIES:
        print("Error: IG_COOKIES environment variable not set. Cannot upload to Instagram.")
        return False

    headers = {
        "User-Agent": "Instagram 123.0.0.21.114",
        "Cookie": IG_COOKIES # This is where the cookie from .env is used
    }

    upload_url = "https://www.instagram.com/create/upload/photo/"
    try:
        with open(image_path, 'rb') as f:
            files = {'photo': f}
            response = requests.post(upload_url, files=files, headers=headers)

        if response.status_code == 200:
            print("Upload successful to Instagram")
            return True
        else:
            print(f"Upload failed. Status code: {response.status_code}")
            print(response.text)
            return False
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return False
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return False

