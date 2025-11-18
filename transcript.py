from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url):
    """Extract video ID from any YouTube URL or Shorts."""
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]

    if "youtube.com/shorts/" in url:
        return url.split("shorts/")[-1].split("?")[0]

    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]

    return None


def get_transcript_from_youtube(url):
    """Fetch transcript using YouTubeTranscriptApi with all edge-case handling."""
    try:
        video_id = extract_video_id(url)
        if not video_id:
            return None, " Invalid YouTube URL"

        try:
            # Try English transcript first
            transcript_list = YouTubeTranscriptApi.get_transcript(
                video_id, languages=['en', 'en-IN']
            )
        except NoTranscriptFound:
            # Try auto-generated transcripts
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id).find_manually_created_transcript(['en', 'en-IN']).fetch()
        except TranscriptsDisabled:
            return None, " This video has transcripts disabled."
        except Exception:
            return None, " No English transcript available."

        transcript_text = " ".join([t["text"] for t in transcript_list])
        return transcript_text, None

    except Exception as e:
        return None, f" Error retrieving transcript: {str(e)}"


def load_transcript_from_file(file_path):
    """Load transcript from uploaded text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read(), None
    except Exception as e:
        return None, f" Failed to load transcript: {str(e)}"


if __name__ == "__main__":
    print("Transcript module ready.")