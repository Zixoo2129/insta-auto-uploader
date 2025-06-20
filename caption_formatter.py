import re

def clean_caption(original_caption):
    # Remove @mewsinsta or similar mentions and replace with your handle
    modified_caption = re.sub(r"@\w+", "@newswire.in", original_caption)

    # Add hashtags
    hashtags = [
        "#breakingnews", "#latestnews", "#trendingnow", "#indianews", "#reels", "#viral",
        "#newsupdate", "#headlines", "#instagramreels", "#tufaanexpress", "#news", "#updates",
        "#dailynews", "#media", "#journalism"
    ]
    hashtag_text = " ".join(hashtags)

    final_caption = f"""{modified_caption}

{hashtag_text}"""
    return final_caption
