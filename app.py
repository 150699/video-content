import streamlit as st
from evaluator import Evaluator
from segmenter import simple_segmenter

st.title("🎥 Video Content Relevance Evaluator")
st.write("Upload transcript + enter title to evaluate relevance.")


# -------------------------------------------
# INPUTS
# -------------------------------------------

title = st.text_input("Video Title / Topic")
description = st.text_area("Video Description (Optional)")

transcript = st.text_area(
    "Paste Video Transcript",
    placeholder="Paste full text transcript of the video here..."
)


# -------------------------------------------
# PROCESS BUTTON
# -------------------------------------------

if st.button("Run Evaluation"):
    if not title:
        st.error(" Title is required!")
    elif not transcript:
        st.error(" Transcript is required!")
    else:
        st.info("⏳ Processing... Please wait...")

        # 1. Segment transcript
        segments = simple_segmenter(transcript, window_size=40)

        # 2. Evaluate using model
        evaluator = Evaluator(title, description)
        scored_segments = evaluator.score_segments(segments)
        final_score = evaluator.aggregate_score(scored_segments)

        # -------------------------------------------
        # OUTPUT
        # -------------------------------------------
        st.success(f"✅ Relevance Score: **{final_score}%**")

        # Detailed view
        st.subheader("Segment Scores")
        for seg in scored_segments:
            sim = round((seg['similarity'] + 1) / 2 * 100, 2)
            st.write(
                f"**Segment {seg['start']}–{seg['end']}** "
                f"- Relevance: **{sim}%**\n"
                f"Text: _{seg['text']}_"
            )