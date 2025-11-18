import streamlit as st
from evaluator import Evaluator
from transcript import get_transcript_from_youtube, load_transcript_from_file

st.title("🎥 Video Content Relevance Evaluator")
st.write("Analyze if a video's content matches its title & topic.")

evaluator = Evaluator()

# --- Input Section ---
option = st.radio("Select Input Method:", ["YouTube URL", "Upload Transcript File"])

title = st.text_input("Video Title")
description = st.text_area("Video Description (optional)")

transcript_text = ""

# If YouTube selected
if option == "YouTube URL":
    youtube_url = st.text_input("Enter YouTube Video URL")

    if youtube_url:
        with st.spinner("Fetching transcript..."):
            transcript_text, error = get_transcript_from_youtube(youtube_url)

        if error:
            st.error(error)
        else:
            st.success("Transcript fetched successfully!")
            st.text_area("Transcript Preview:", transcript_text, height=200)

# If File Upload selected
else:
    uploaded_file = st.file_uploader("Upload a .txt transcript file", type=["txt"])

    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        transcript_text = content
        st.text_area("Transcript Preview:", transcript_text, height=200)


# --- Submit for Evaluation ---
if st.button("Evaluate Relevance"):
    if not title:
        st.error("Please enter a title!")
    elif not transcript_text:
        st.error("Transcript unavailable!")
    else:
        result = evaluator.evaluate(title, description, transcript_text)

        st.subheader("📊 Relevance Score")
        st.metric("Score", f"{result['score']} %")

        st.subheader("📝 Explanation")
        st.write(result["explanation"])