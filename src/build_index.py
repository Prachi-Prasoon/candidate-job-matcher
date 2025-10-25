import json
import torch
from pathlib import Path
from utils import compute_embeddings

# Paths
DATA_PATH = Path(__file__).parent.parent / "data" / "jobs.json"
EMB_PATH = Path(__file__).parent / "job_embeddings.pt"


def build_index():
    """Build job embeddings and save them"""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    job_texts = [f"{job['title']}. {job['description']}" for job in jobs]
    embeddings = compute_embeddings(job_texts)

    torch.save({"jobs": jobs, "embeddings": embeddings}, EMB_PATH)
    print(f"✅ Saved embeddings to {EMB_PATH}")


if __name__ == "__main__":
    build_index()
