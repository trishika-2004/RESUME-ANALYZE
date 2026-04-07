
import PyPDF2
import os

def extract_from_pdf(file_path):
    """extracted the  text from a PDFresume"""
    text = ""
    try:
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text


def extract_from_txt(file_path):
    """extracted the  text from  plain textresume"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return ""


def extract_resume_text(file_path):
    """auuto-detected file type and extracted the text"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return ""

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_from_pdf(file_path)
    elif ext == ".txt":
        return extract_from_txt(file_path)
    else:
        print("UNnsupported file type Please use PDF or txt.")
        return ""


def extract_job_description(file_path):
    """read the job descruotion of the files"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading job description: {e}")
        return ""