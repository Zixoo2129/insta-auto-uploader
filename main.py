import os
from dotenv import load_dotenv
from telegram_bot import start_bot
from caption_formatter import clean_caption
from watermark_handler import process_media
from instagram_upload import upload_photo_to_instagram

load_dotenv()

# Set your watermark and test image here
WATERMARK_PATH = "your_watermark.png"
TEST_IMAGE_PATH = "downloads/sample.jpg"
TEST_CAPTION = "Follow @mewsinsta for more!"

def handle_post(media_path, caption):
    print("[📦] Handling Image Upload...")

    processed_file = process_media(media_path, WATERMARK_PATH)
    final_caption = clean_caption(caption)
    upload_photo_to_instagram(processed_file, final_caption)

if __name__ == "__main__":
    try:
        # TEST RUN – Remove or replace when using live Telegram flow
        handle_post(TEST_IMAGE_PATH, TEST_CAPTION)

        # Start Telegram Bot
        print("[🤖] Starting Telegram Bot...")
        start_bot()
    except Exception as e:
        print(f"[❌] Error in main: {e}")
