from embeddings import get_embedding, cosine

class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, title, description, transcript):
        """Evaluate how relevant the transcript is to the title/description."""
        
        if not transcript:
            return {
                "score": 0,
                "explanation": "Transcript not available."
            }

        # Combine title + description as the expected topic
        combined_topic = title
        if description:
            combined_topic += " " + description

        # Generate embeddings
        topic_emb = get_embedding(combined_topic)
        transcript_emb = get_embedding(transcript)

        # Compare using cosine similarity
        similarity = cosine(topic_emb, transcript_emb)

        # Convert similarity to percentage score
        relevance_score = round(similarity * 100, 2)

        # Explanation
        explanation = self.generate_explanation(relevance_score)

        return {
            "score": relevance_score,
            "explanation": explanation
        }

    def generate_explanation(self, score):
        if score > 80:
            return "Content strongly matches the provided title/topic."
        elif score > 60:
            return "Content is mostly relevant but contains some off-topic sections."
        elif score > 40:
            return "Content partially matches the title, with several irrelevant sections."
        else:
            return "Content is largely irrelevant to the given title/topic."


if __name__ == "__main__":
    print("Evaluator module ready.")
