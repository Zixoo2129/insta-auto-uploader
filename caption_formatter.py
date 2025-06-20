import random
import re

# List of viral hashtags
VIRAL_HASHTAGS = [
    "#trending", "#news", "#breaking", "#viral", "#reels", "#dailyupdate", "#instadaily", 
    "#foryou", "#explorepage", "#todaynews", "#india", "#update", "#instanews"
]

def format_caption(original_caption, old_username="@mewsinsta", new_username="@newswire.in"):
    # Replace old username with new one
    modified_caption = re.sub(re.escape(old_username), new_username, original_caption, flags=re.IGNORECASE)

    # Remove duplicate @ mentions or trailing whitespace
    modified_caption = modified_caption.strip()

    # Add 10 random viral hashtags
    selected_tags = random.sample(VIRAL_HASHTAGS, 10)
    hashtags = " ".join(selected_tags)

    # Final caption
    final_caption = f"{modified_caption}"

{hashtags}"
    return final_caption
