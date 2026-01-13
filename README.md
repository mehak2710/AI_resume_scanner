# 🤖 AI Resume Scanner

An intelligent ATS-compliant resume analysis tool that helps job seekers optimize their resumes for Applicant Tracking Systems and increase interview callback rates.

## 📋 Overview

AI Resume Scanner leverages artificial intelligence to analyze resumes against job descriptions, providing actionable feedback on keyword optimization, formatting compliance, and content quality. The tool mimics how real ATS systems evaluate resumes, helping candidates pass initial screening filters.

## ✨ Key Features

- **ATS Compatibility Analysis** - Validates resume format, structure, and parsing reliability
- **Keyword Matching** - Compares resume content against job description requirements
- **Match Score Generation** - Provides percentage-based compatibility rating
- **Multiple Resume Adding** - Allows uploading and analyzing multiple resumes at once
- **Real-time Feedback** - Delivers instant improvement suggestions
- **Format Validation** - Checks for ATS-friendly formatting practices

## 🎯 KPIs & Success Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Match Score Accuracy | 85%+ | Alignment with actual ATS systems |
| Processing Time | <3 sec | Average resume analysis duration |
| Keyword Detection Rate | 90%+ | Successfully identified relevant keywords |
| User Satisfaction | 4.5/5 | Based on feedback and usability |
| Resume Pass Rate | +40% | Improvement in ATS screening success |

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip package manager
```

### Installation

```bash
# Clone the repository
git clone https://github.com/mehak2710/AI_resume_scanner.git

# Navigate to project directory
cd AI_resume_scanner

# Install dependencies
pip install -r requirements.txt
```

### Usage

```python
# Basic usage example
from ai_resume_scanner import ResumeScanner

scanner = ResumeScanner()
result = scanner.analyze(resume_path, job_description)
print(f"Match Score: {result.score}%")
```

## 🔧 Technology Stack

- **Python** - Core programming language
- **Natural Language Processing** - Text analysis and keyword extraction
- **Machine Learning** - Pattern recognition and scoring algorithms






