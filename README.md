# 🎓 College Admission Q&A Bot

**AdmissionBot** is a conversational agent designed to assist prospective students with college‑admission questions—deadlines, requirements, procedures, and more.

## 🎯 Project Overview
The goal of this project is to create a helpful information assistant for college applicants by:
- Answering frequently asked questions.
- Handling follow‑up questions within the same session (context awareness).
- Delivering clear, concise responses.

## 🧠 Methodology
- Built in **Python** using the **ChatterBot** library with the **BestMatch** logic adapter.
- Trained on:
  - The ChatterBot English corpus.
  - A custom dataset of admission‑related questions and answers stored in `data/admission_data.yml`.
- Context memory allows multi‑step conversations (e.g., “What are the deadlines? … How do I apply?”).

## 🗂 Project Structure
```bash
AIML-Project-2--CollegeQ-A-Chatbot/
├── data/
│ └── admission_data.yml # Domain-specific Q&A pairs
├── admission_bot.py # Main chatbot script
├── requirements.txt
└── README.md
```

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nysajain/AIML-Project-2--CollegeQ-A-Chatbot.git
   cd AIML-Project-2--CollegeQ-A-Chatbot
2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## 🚀 Running the Bot
Start the chatbot via:

```bash
python admission_bot.py
```

Sample questions to try:

- “When is the application deadline?”

- “What documents do I need?”

- “How can I apply for scholarships?”

## 📊 Results & Key Findings
The bot can answer most standard admission queries based on the training data.

Additional training data improves coverage and accuracy.

Feedback from users can highlight missing questions and inform future updates.

## 📂 Sample Dataset
The file data/admission_data.yml includes example Q&A pairs. Feel free to expand it with more detailed or college‑specific questions.

## 👩‍💻 Contributions
Nysa Jain – developer and project lead.
Contributions via issues or pull requests are welcome!
