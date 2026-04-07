

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


SKILLS_DATABASE = [
    
    "python", "java", "javascript", "c++", "c#", "ruby", "swift", "kotlin",
    
    "html", "css", "react", "angular", "nodejs", "flask", "django",
    
    "sql", "mysql", "postgresql", "mongodb", "oracle", "redis",
    
    "git", "docker", "kubernetes", "aws", "azure", "linux", "jenkins",
  
    "machine learning", "deep learning", "pandas", "numpy", "tensorflow",
    "data analysis", "matplotlib",

    "communication", "teamwork", "problem solving", "leadership",
 
    "rest api", "agile", "scrum", "data structures", "algorithms"
]


def clean_text(text):
    """loweing the case and removing pucuation frm the given text """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def extract_skills(text):
    """maatch our skills against the database """
    cleaned = clean_text(text)
    found_skills = []

    for skill in SKILLS_DATABASE:
        if skill in cleaned:
            found_skills.append(skill)

    return list(set(found_skills))  


def calculate_match_score(resume_skills, job_skills):
    """calculating the skills that are prseent in the resume """
    if not job_skills:
        return 0

    matched = [skill for skill in job_skills if skill in resume_skills]
    score = round((len(matched) / len(job_skills)) * 100, 2)
    return score, matched


def get_missing_skills(resume_skills, job_skills):
    """return  all the skill required in job but missing from resume"""
    return [skill for skill in job_skills if skill not in resume_skills]


def analyze(resume_text, job_text):
    """return all results"""
    resume_skills  = extract_skills(resume_text)
    job_skills     = extract_skills(job_text)

    score, matched = calculate_match_score(resume_skills, job_skills)
    missing        = get_missing_skills(resume_skills, job_skills)

    return {
        "resume_skills"  : sorted(resume_skills),
        "job_skills"     : sorted(job_skills),
        "matched_skills" : sorted(matched),
        "missing_skills" : sorted(missing),
        "match_score"    : score
    }