# # import re
# # import docx2txt
# # import PyPDF2

# # def extract_text(file_path):
# #     """Extract raw text from .pdf or .docx resumes."""
# #     text = ""
# #     if file_path.endswith(".pdf"):
# #         with open(file_path, "rb") as f:
# #             reader = PyPDF2.PdfReader(f)
# #             for page in reader.pages:
# #                 text += page.extract_text() or ""
# #     elif file_path.endswith(".docx"):
# #         text = docx2txt.process(file_path)
# #     return text.strip()

# # def analyze_resume(text):
# #     """Simple keyword-based analysis."""
# #     skills = [
# #         "Python", "Java", "C++", "Machine Learning", "Deep Learning",
# #         "Data Analysis", "SQL", "HTML", "CSS", "JavaScript",
# #         "Flask", "Django", "React", "AWS"
# #     ]

# #     found = [s for s in skills if re.search(rf"\b{s}\b", text, re.I)]
# #     experience = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)', text, re.I)
# #     exp_val = max(map(int, experience)) if experience else 0

# #     return {
# #         "skills_found": found,
# #         "experience": exp_val,
# #         "summary": f"Skills: {', '.join(found) if found else 'None found'} | Experience: {exp_val} years"
# #     }


# # import re
# # import docx2txt
# # from PyPDF2 import PdfReader

# # def extract_text(file_path):
# #     """Extract raw text from .pdf or .docx resumes."""
# #     text = ""
# #     try:
# #         if file_path.lower().endswith(".pdf"):
# #             with open(file_path, "rb") as f:
# #                 reader = PdfReader(f)
# #                 for page in reader.pages:
# #                     page_text = page.extract_text()
# #                     if page_text:
# #                         text += page_text

# #         elif file_path.lower().endswith(".docx"):
# #             text = docx2txt.process(file_path)

# #         else:
# #             raise Exception("Unsupported file type. Please upload a PDF or DOCX resume.")

# #         text = text.strip()
# #         if not text:
# #             raise Exception("No readable text could be extracted from the resume.")

# #         return text

# #     except Exception as e:
# #         raise Exception(f"Error extracting text: {e}")


# # def analyze_resume(text):
# #     """Simple keyword-based analysis."""
# #     skills = [
# #         "Python", "Java", "C++", "Machine Learning", "Deep Learning",
# #         "Data Analysis", "SQL", "HTML", "CSS", "JavaScript",
# #         "Flask", "Django", "React", "AWS"
# #     ]

# #     # Find skills mentioned in resume (case-insensitive)
# #     found = [s for s in skills if re.search(rf"\b{s}\b", text, re.I)]

# #     # Extract experience numbers like "3 years", "2+ yrs"
# #     experience = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)', text, re.I)
# #     exp_val = max(map(int, experience)) if experience else 0

# #     # Prepare summary
# #     summary = f"Skills: {', '.join(found) if found else 'None found'} | Experience: {exp_val} years"

# #     return {
# #         "skills_found": found,
# #         "experience": exp_val,
# #         "summary": summary
# #     }


# import re
# import docx2txt
# from PyPDF2 import PdfReader


# def extract_text(file_path):
#     """Extract text content from PDF or DOCX resumes."""
#     text = ""
#     try:
#         if file_path.lower().endswith(".pdf"):
#             with open(file_path, "rb") as f:
#                 reader = PdfReader(f)
#                 for page in reader.pages:
#                     page_text = page.extract_text()
#                     if page_text:
#                         text += page_text

#         elif file_path.lower().endswith(".docx"):
#             text = docx2txt.process(file_path)

#         else:
#             raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

#         text = text.strip()
#         if not text:
#             raise ValueError("No readable text could be extracted from the resume.")

#         return text

#     except Exception as e:
#         raise Exception(f"Error extracting text from file: {e}")


# def analyze_resume(text):
#     """Analyze resume text for skills, experience, and suggest potential roles."""
#     # ✅ Common technical skills
#     skills_list = [
#         "Python", "Java", "C++", "C#", "SQL", "JavaScript",
#         "HTML", "CSS", "React", "Node.js", "Flask", "Django",
#         "Machine Learning", "Deep Learning", "Data Science", "Data Analysis",
#         "AWS", "Azure", "Docker", "Git"
#     ]

#     # ✅ Identify skills present in resume
#     found_skills = [skill for skill in skills_list if re.search(rf"\b{re.escape(skill)}\b", text, re.I)]

#     # ✅ Extract experience (e.g., "3 years", "2+ yrs", etc.)
#     experience_matches = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)', text, re.I)
#     experience_val = max(map(int, experience_matches)) if experience_matches else 0

#     # ✅ Suggest potential roles based on skills
#     suggested_roles = []
#     if any(skill in found_skills for skill in ["Machine Learning", "Deep Learning", "Data Science"]):
#         suggested_roles.append("AI/ML Engineer")
#     if any(skill in found_skills for skill in ["Flask", "Django", "Node.js"]):
#         suggested_roles.append("Backend Developer")
#     if any(skill in found_skills for skill in ["React", "JavaScript", "HTML", "CSS"]):
#         suggested_roles.append("Frontend Developer")
#     if any(skill in found_skills for skill in ["SQL", "Data Analysis"]):
#         suggested_roles.append("Data Analyst")
#     if any(skill in found_skills for skill in ["AWS", "Azure", "Docker"]):
#         suggested_roles.append("Cloud Engineer")

#     # ✅ Build summary for display
#     summary = (
#         f"Skills: {', '.join(found_skills) if found_skills else 'None detected'} | "
#         f"Experience: {experience_val} years | "
#         f"Suggested Roles: {', '.join(suggested_roles) if suggested_roles else 'None'}"
#     )

#     # ✅ Return consistent dictionary for app.py
#     return {
#         "skills": ", ".join(found_skills) if found_skills else "Not detected",
#         "experience": experience_val,
#         "suggested_roles": ", ".join(suggested_roles) if suggested_roles else "None",
#         "summary": summary
#     }


import re
import docx2txt
import PyPDF2


def extract_text(file_path):
    """Extract raw text from .pdf or .docx resumes."""
    text = ""
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    return text.strip()


def analyze_resume(text):
    """Keyword-based analysis with suggested roles."""
    skills = [
        "Python", "Java", "C++", "Machine Learning", "Deep Learning",
        "Data Analysis", "SQL", "HTML", "CSS", "JavaScript",
        "Flask", "Django", "React", "AWS"
    ]

    # Detect skills
    found = [s for s in skills if re.search(rf"\b{s}\b", text, re.I)]

    # Extract experience years
    experience = re.findall(r'(\d+)\+?\s*(?:years?|yrs?)', text, re.I)
    exp_val = max(map(int, experience)) if experience else 0

    # Suggested roles logic
    suggestions = []
    if "Machine Learning" in found or "Deep Learning" in found:
        suggestions.append("Data Scientist")
    if "Flask" in found or "Django" in found:
        suggestions.append("Backend Developer")
    if "React" in found or "JavaScript" in found:
        suggestions.append("Frontend Developer")
    if "SQL" in found and "Python" in found:
        suggestions.append("Data Analyst")

    # Final dictionary returned to Flask
    return {
        "skills_found": found,
        "experience": exp_val,
        "summary": f"Skills: {', '.join(found) if found else 'None found'} | Experience: {exp_val} years",
        "suggested_roles": ', '.join(suggestions) if suggestions else "Not enough data"
    }
