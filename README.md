# Resume Analyzer & Job Matcher

## Problem Statement

Every year, thousands of fresh graduates send out resumes and hear nothing back — not because they lack talent, but because their resume doesn't speak the language of the job description.

As a student stepping into the job market, I personally felt this frustration. You spend hours crafting a resume but have no way to know if it actually matches what the company is looking for.

That's why I built the **Resume Analyzer & Job Matcher** — a Python tool that reads your resume, understands what skills you have, compares them against a job description, and gives you an honest match score with clear suggestions on what's missing.

No guessing. No waiting for rejection emails. Just instant, actionable feedback so you can improve your resume before you even hit send.

---

## Setting Up the Project

Nothing fancy here — just Python and a few libraries. Here's how to get it running on your machine:

First, make sure you have Python installed. Then open your terminal, clone the project and step into the folder:
```bash
git clone https://github.com/<your-username>/resume-analyzer.git
cd resume-analyzer
```

Create a virtual environment so the libraries stay clean and don't mess with your system Python:
```bash
python -m venv venv
venv\Scripts\activate
```

You'll know it worked when you see `(venv)` appear at the start of your terminal line. Now install the three libraries the project needs:
```bash
pip install pypdf2 nltk colorama
```

One last thing — download the language data that NLTK needs to process text:
```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

That's it. Run the program with:
```bash
python main.py
```

---

## Test Cases

### Test Case 1 — High Match Resume
You give it a resume packed with relevant tech skills — Python, SQL, Git, REST API, Docker, AWS, Machine Learning and more. The idea here is to see how the tool responds when someone is genuinely well-qualified for the role. The tool should recognize most of the required skills, show a score of 75% or above, and display an **"Excellent Match!"** verdict in green.

![High Match Screenshot]()

---

### Test Case 2 — Low Match Resume
This time you give it a resume with completely unrelated skills like Cooking, Painting, and Music. This tests whether the tool handles a weak candidate gracefully — it should show a very low score, flag a long list of missing skills in red, and tell the user they have significant gaps to work on. No crashes, just honest feedback.

![Low Match Screenshot]()

---

### Test Case 3 — PDF Resume Upload
Instead of a plain text file, you feed the tool an actual PDF resume — the kind most people have saved on their laptop. This tests the PDF reading capability. The tool should open the file, extract all the text from it, and run the full analysis exactly like it does for a text file. No extra steps needed from the user.

![PDF Upload Screenshot]()
