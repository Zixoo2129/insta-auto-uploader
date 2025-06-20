import random
import re

VIRAL_HASHTAGS = [
    "#trending", "#news", "#breaking", "#viral", "#reels", "#dailyupdate", "#instadaily",
    "#foryou", "#explorepage", "#todaynews", "#india", "#update", "#instanews"
]

def format_caption(original_caption, old_username="@mewsinsta", new_username="@newswire.in"):
    modified_caption = re.sub(re.escape(old_username), new_username, original_caption, flags=re.IGNORECASE)
    modified_caption = modified_caption.strip()
    selected_tags = random.sample(VIRAL_HASHTAGS, 10)
    hashtags = " ".join(selected_tags)
    final_caption = f"{modified_caption}\n{hashtags}" # Changed here
    return final_caption
