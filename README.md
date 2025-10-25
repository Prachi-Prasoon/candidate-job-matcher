# Candidate–Job Matcher

A **semantic job-matching chatbot** that helps candidates find the most relevant job opportunities based on their resume or skills. Built with **sentence embeddings** and **cosine similarity**, the system is fully offline and does **not require any API keys**.  

---

## Features

- 🔹 Match candidate profiles to jobs across **multiple domains**: Tech, Product, Research, Business, Creative, Healthcare, Finance, and more.  
- 🔹 **Fast and offline** matching using embeddings from `sentence-transformers`.  
- 🔹 Returns **top N matching jobs** with similarity scores.  
- 🔹 Fully **portfolio-ready**, lightweight, and easy to extend.  

---

## Tech Stack

- **Python 3.10+**  
- **Gradio** – Interactive web UI  
- **PyTorch** – Backend for embeddings  
- **Sentence-Transformers** – Pretrained model for semantic embeddings  
- **NumPy & tqdm** – Utilities for computations and progress tracking  

---

## Folder Structure

candidate-job-matcher/
│
├── data/
│ └── jobs.json # Job postings (50+ diverse roles)
│
├── src/
│ ├── app.py # Main Gradio app
│ ├── build_index.py # Build embeddings from jobs.json
│ ├── utils.py # Utilities: embeddings & job matching
│ └── job_embeddings.pt # Saved embeddings (auto-generated)
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation


