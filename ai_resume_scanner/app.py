import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Extract text from PDF ----------
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

# ---------- UI ----------
st.set_page_config(page_title="AI Resume Scanner", layout="centered")
st.title("📄 AI-Based Resume Scanner")
st.write("Upload multiple resumes and compare them with a job description")

# Upload resumes
resume_files = st.file_uploader(
    "Upload Resumes (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)

# Job description
job_desc = st.text_area("Paste Job Description")

# ---------- Scan ----------
if st.button("Scan Resumes"):
    if resume_files and job_desc:
        results = []

        for resume in resume_files:
            resume_text = extract_text(resume)

            documents = [resume_text, job_desc.lower()]

            # 🔹 Updated TF-IDF Vectorizer (as requested)
            vectorizer = TfidfVectorizer(
                stop_words="english",
                max_features=150
            )

            tfidf_matrix = vectorizer.fit_transform(documents)

            similarity = cosine_similarity(
                tfidf_matrix[0:1], tfidf_matrix[1:2]
            )[0][0]

            # 🔹 Match score out of 100 (normalized)
            raw_score = similarity * 100
            final_score = min(round(raw_score * 1.5, 2), 100)

            results.append({
                "Resume": resume.name,
                "Match Score (%)": final_score
            })

        # Sort resumes by score
        results = sorted(results, key=lambda x: x["Match Score (%)"], reverse=True)

        st.success("✅ Resume Scan Completed")
        st.subheader("📊 Resume Ranking")
        st.table(results)

    else:
        st.warning("⚠️ Please upload resumes and paste the job description")
