import requests
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return None


def get_transcript_from_youtube(url):
    """Fetch transcript using YouTubeTranscriptApi."""
    try:
        video_id = extract_video_id(url)
        if not video_id:
            return None, "Invalid YouTube URL"

        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = " ".join([t["text"] for t in transcript_list])
        return transcript_text, None

    except Exception as e:
        return None, f"Error retrieving transcript: {str(e)}"


def load_transcript_from_file(file_path):
    """Load transcript from a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read(), None
    except Exception as e:
        return None, f"Failed to load transcript: {str(e)}"


if __name__ == "__main__":
    print("Transcript module ready.")