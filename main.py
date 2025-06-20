import os
from dotenv import load_dotenv
from reel_uploader import upload_reel
[span_1](start_span)from instagram_upload import upload_photo_to_instagram # Changed here[span_1](end_span)
from caption_formatter import format_caption
from watermark_handler import process_media

load_dotenv()

def handle_post(file_path, caption, is_reel=False, cover_path=None):
    print(f"[📦] Handling {'Reel' if is_reel else 'Image'} Upload...")

    final_caption = format_caption(caption)

    processed_file = process_media(file_path)

    if is_reel:
        upload_reel(processed_file, final_caption, cover_path)
    else:
        [span_2](start_span)upload_photo_to_instagram(processed_file, final_caption) # Changed here[span_2](end_span)

if __name__ == "__main__":
    handle_post("downloads/sample.jpg", "Follow @mewsinsta for more!")
    # handle_post("downloads/reel.mp4", "🔥 Hot news reel!", is_reel=True, cover_path="downloads/cover.jpg")

