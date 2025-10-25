import json
import torch
import gradio as gr
from pathlib import Path
from utils import get_top_matches

# Paths
DATA_PATH = Path(__file__).parent.parent / "data" / "jobs.json"
EMB_PATH = Path(__file__).parent / "job_embeddings.pt"

# Load embeddings (or auto-build if missing)
if not EMB_PATH.exists():
    print("Embeddings not found, building now...")
    from build_index import build_index
    build_index()

data = torch.load(EMB_PATH)
jobs = data["jobs"]
job_embeddings = data["embeddings"]

print(f"✅ Loaded {len(jobs)} job postings.")


def search_jobs(candidate_text, top_k=5):
    """Return top K job matches"""
    if not candidate_text.strip():
        return "Please enter candidate details."
    return get_top_matches(candidate_text, jobs, job_embeddings, top_k)


# Gradio UI
def main():
    with gr.Blocks(title="Candidate-Job Matcher") as demo:
        gr.Markdown("## 🧠 Candidate–Job Matcher")

        resume_input = gr.Textbox(
            lines=7,
            label="Candidate Details",
            placeholder="Paste resume or skills here..."
        )
        topk_slider = gr.Slider(1, 10, value=5, step=1, label="Number of Matches")
        output_box = gr.Textbox(lines=20, label="Results")
        run_button = gr.Button("Search")

        run_button.click(fn=search_jobs, inputs=[resume_input, topk_slider], outputs=output_box)

    demo.launch()


if __name__ == "__main__":
    main()
