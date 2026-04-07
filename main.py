
import os
from colorama import Fore, Style, init
from extractor import extract_resume_text, extract_job_description
from analyzer import analyze

init(autoreset=True)


def print_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "       RESUME ANALYZER and  JOB MATCHER")
    print(Fore.CYAN + "=" * 60)


def print_section(title):
    print(Fore.YELLOW + f"\n{'=' * 10} {title} {'=' * 10}")


def print_skills_list(skills, color):
    if skills:
        for skill in skills:
            print(color + f"   • {skill}")
    else:
        print(Fore.WHITE + "   nothing found")


def print_score(score):
    if score >= 75:
        color = Fore.GREEN
        label = "excellent matcgh found!"
    elif score >= 50:
        color = Fore.YELLOW
        label = "good Match found — improve  few skill"
    elif score >= 25:
        color = Fore.MAGENTA
        label = "Ok!partial Match — work on the missing skill"
    else:
        color = Fore.RED
        label = "No.Low Match — very high skill gaps"

    print(color + f"\n   Match Score : {score}%")
    print(color + f"   Verdict     : {label}")


def get_resume_path():
    """asking teh user for resume path"""
    print(Fore.WHITE + "\n enter the path to your resume (.pdf or .txt)")
    print(Fore.WHITE + " Example: C:\\Users\\ASUS\\Desktop\\my_resume.txt")
    print(Fore.WHITE + " (or press Enter to use sample resume)\n")

    path = input(Fore.CYAN + " > ").strip()

    # If user presses Enter, use built-in sample resume
    if path == "":
        path = "sample_data\\sample_resume.txt"
        create_sample_resume(path)

    return path


def create_sample_resume(path):
    """Ccreating a sample resume if the user has no resume """
    os.makedirs("sample_data", exist_ok=True)
    sample = """
    trishka
     Python Developer
    Skills:
    Python, SQL, Git, REST API, Problem Solving,
    Communication, Teamwork, Data Structures, Linux

    Experience:
    2 years of Python development
    Database management using SQL and Oracle
    Built REST APIs using Flask

    Education:
    B.Tech Computer Science
    """
    with open(path, "w") as f:
        f.write(sample)
    print(Fore.YELLOW + " (Using built-in sample resume)\n")


def main():
    print_banner()

    
    resume_path = get_resume_path()
    resume_text = extract_resume_text(resume_path)

    if not resume_text:
        print(Fore.RED + " Could not read resume. check if the path is correct or not again.")
        return

    
    jd_path = "sample_data\\job_description.txt"
    job_text = extract_job_description(jd_path)

    if not job_text:
        print(Fore.RED + " Could not read job description.")
        return

    # Step 3: Run analysis
    print(Fore.WHITE + "\n Analyzing your resume...")
    results = analyze(resume_text, job_text)

   
    print_section("skills found in your ressume")
    print_skills_list(results["resume_skills"], Fore.WHITE)

    print_section("skills that are required in your job")
    print_skills_list(results["job_skills"], Fore.WHITE)

    print_section("skills that are matched")
    print_skills_list(results["matched_skills"], Fore.GREEN)

    print_section("skills that are missed")
    print_skills_list(results["missing_skills"], Fore.RED)

    print_section("MATCH SCORE")
    print_score(results["match_score"])

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.CYAN + "   Analysis Completed")
    print(Fore.CYAN + "=" * 60 + "\n")


if __name__ == "__main__":
    main()