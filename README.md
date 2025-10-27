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

<img width="514" height="347" alt="image" src="https://github.com/user-attachments/assets/84c2e708-7fa8-497a-92cf-189d54a7489b" />



---

## Installation & Setup

1. **Clone the repository**

2. **Create a virtual environment (recommended)**

python -m venv venv

**Windows**
venv\Scripts\activate

**macOS/Linux**
source venv/bin/activate


3. **Install dependencies**

pip install -r requirements.txt


## How to Run

1. **Build embeddings:**

python src/build_index.py

2. **Launch the Gradio app:**

python src/app.py

3. **Use the app:**

a. Paste your resume or skills into the input box.

b. Select the number of top matches to display.

c. Click Search to see recommended jobs along with similarity scores.


## Example Usage

Candidate Input:
"Experienced Python developer with knowledge of machine learning and APIs."

Top Matches Output:
1. Software Engineer (Score: 0.532)
   Develop and maintain software applications using Python, Java, JavaScript...
2. Data Analyst (Score: 0.499)
   Analyze datasets, build ML models, and generate insights...


## Key Features

- Demonstrates semantic NLP matching using embeddings.

- Shows end-to-end project skills: data processing → embeddings → similarity search → web UI.

- Lightweight and fully offline: no external API keys required.

- Easily extendable: add more job postings or change the model for higher accuracy.


