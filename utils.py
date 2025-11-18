import re

def clean_text(text: str):
    """Remove extra spaces, newlines, and symbols."""
    if not text:
        return ""

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def safe_get(d, key, default=None):
    """Safely get dictionary values."""
    try:
        return d.get(key, default)
    except:
        return default