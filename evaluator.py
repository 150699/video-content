from embeddings import get_embedding, cosine

SIM_RELEVANT = 0.65
SIM_PARTIAL = 0.45


class Evaluator:
    def __init__(self, title, description=None):
        self.title = title
        self.description = description

        # Create embeddings
        self.title_emb = get_embedding(title)
        self.desc_emb = get_embedding(description) if description else None

    def score_segments(self, segments):
        """
        segments → list of:
        {
            'start': seconds,
            'end': seconds,
            'text': "segment text"
        }
        """
        results = []
        for seg in segments:
            seg_emb = get_embedding(seg["text"])
            sim_title = cosine(self.title_emb, seg_emb)

            if self.desc_emb:
                sim_desc = cosine(self.desc_emb, seg_emb)
                similarity = max(sim_title, sim_desc)
            else:
                similarity = sim_title

            results.append({
                **seg,
                "similarity": similarity
            })

        return results

    def aggregate_score(self, scored_segments):
        """
        Convert similarity scores (-1 to 1) → final score (0–100)
        weighted by segment duration
        """
        weights = []
        values = []

        for seg in scored_segments:
            duration = seg["end"] - seg["start"]
            score_0_1 = (seg["similarity"] + 1) / 2   # normalize to 0–1

            weights.append(duration)
            values.append(score_0_1)

        # Weighted average
        total_weight = sum(weights)
        base_score = sum(w * v for w, v in zip(weights, values)) / (total_weight + 1e-9)

        final_score = base_score * 100

        # Clamp
        if final_score < 0:
            final_score = 0
        if final_score > 100:
            final_score = 100

        return round(final_score, 2)