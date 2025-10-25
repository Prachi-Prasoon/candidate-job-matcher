import torch
from sentence_transformers import SentenceTransformer, util

# Sentence Transformer model
MODEL_NAME = "sentence-transformers/paraphrase-MiniLM-L3-v2"
model = SentenceTransformer(MODEL_NAME)


def compute_embeddings(texts):
    """Compute embeddings for a list of texts"""
    return model.encode(texts, convert_to_tensor=True)


def get_top_matches(candidate_text, jobs, job_embeddings, top_k=5):
    """Return top K matching jobs based on cosine similarity"""
    candidate_emb = model.encode(candidate_text, convert_to_tensor=True)
    scores = util.cos_sim(candidate_emb, job_embeddings)[0]
    top_results = torch.topk(scores, k=min(top_k, len(jobs)))
    matches = []
    for score, idx in zip(top_results.values, top_results.indices):
        job = jobs[idx]
        matches.append(f"{job['title']} (Score: {score:.3f})\n{job['description']}")
    return "\n\n".join(matches)
