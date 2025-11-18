def simple_segmenter(transcript_text, window_size=40):
    """
    Breaks transcript text into equal-size word chunks.
    No timestamps (simple version).
    Returns list of:
    {
        'start': index,
        'end': index,
        'text': 'chunk text'
    }
    """

    words = transcript_text.split()
    segments = []

    start = 0
    end = window_size

    index = 0
    while start < len(words):
        chunk_words = words[start:end]
        text = " ".join(chunk_words)

        segments.append({
            "start": index,
            "end": index + 1,
            "text": text
        })

        start += window_size
        end += window_size
        index += 1

    return segments