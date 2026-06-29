# QueryQueens-Redrob-Hackathon

AI-powered candidate ranking system developed for the Redrob Data & AI Challenge.

## Project Overview

QueryQueens is an AI-powered candidate ranking system developed for the Redrob Data & AI Challenge. The system analyzes candidate profiles and intelligently ranks the most suitable candidates for a given job description.

Our solution combines feature extraction, behavioral signal analysis, semantic similarity matching, profile consistency validation, honeypot detection, and explainable AI to improve recruitment decisions beyond traditional keyword-based matching.

The system generates the Top 100 ranked candidates along with human-readable explanations, helping recruiters understand why each recommendation was made.

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/neelima-alamanda/QueryQueens-Redrob-Hackathon.git
cd QueryQueens-Redrob-Hackathon
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the Dataset

Place the provided `candidates.jsonl` dataset inside the `data/` directory.

> **Note:** The dataset is not included in this repository due to its large size.

### 4. Run the Ranking Engine

```bash
python src/main.py
```

This generates the ranked output file:

```
submission.csv
```

### 5. Launch the Web Dashboard (Optional Demo Interface)

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:7860
```

The dashboard allows users to:

- Upload the candidate dataset
- Run the ranking pipeline
- View the Top 100 candidates
- Download the generated ranking results

## Features

- AI-powered candidate ranking based on job description relevance
- Feature extraction from candidate profiles
- Behavioral signal analysis using recruiter engagement metrics
- Semantic similarity matching with Sentence Transformers
- Profile consistency validation
- Honeypot detection for suspicious candidate profiles
- Hybrid scoring by combining technical, behavioral, and semantic scores
- Explainable AI with human-readable ranking reasons
- Top 100 candidate recommendation generation
- Interactive web dashboard for candidate ranking and result visualization
- CSV download of ranked candidates
- Submission-ready metadata configuration including repository, compute environment, AI tool declaration, and reproducibility details through `submission_metadata.yaml`

## Project Structure

```
QueryQueens-Redrob-Hackathon/
│
├── data/
│   ├── candidate_schema.json
│   ├── job_description.docx
│   ├── redrob_signals_doc.docx
│   ├── sample_candidates.json
│   └── submission_spec.docx
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── src/
│   ├── parser.py
│   ├── features.py
│   ├── behavior.py
│   ├── consistency.py
│   ├── honeypot_detector.py
│   ├── semantic_matcher.py
│   ├── ranking_engine.py
│   ├── decision_explainer.py
│   ├── evaluation.py
│   ├── main.py
│   └── ...
│
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── submission_metadata.yaml
├── README.md
└── .gitignore
```

## Tech Stack

### Programming Language
- Python

### Backend
- Flask

### Machine Learning & AI
- Sentence Transformers
- Scikit-learn

### Data Processing
- Pandas
- NumPy

### Frontend
- HTML
- CSS
- JavaScript

### Version Control
- Git
- GitHub

## AI Ranking Pipeline

The ranking engine combines multiple independent scoring components to generate the final candidate ranking:

* Technical Feature Score
* Behavioral Signal Score
* Semantic Similarity Score
* Profile Consistency Score
* Honeypot Detection Penalty

These scores are combined using a weighted hybrid ranking strategy to produce the final ranking score. Each recommendation also includes a human-readable explanation describing the candidate's strengths and suitability for the job description.
The ranking pipeline is designed to run entirely on CPU without requiring GPU acceleration.

### Deployment

- Docker
- Hugging Face Spaces

## System Architecture

```
Candidate Dataset (.jsonl)
           │
           ▼
      Data Parsing
           │
           ▼
   Feature Extraction
           │
           ├── Technical Features
           ├── Behavioral Signals
           ├── Consistency Analysis
           ├── Honeypot Detection
           └── Semantic Similarity
                     │
                     ▼
             Hybrid Ranking Engine
                     │
                     ▼
          Explainable AI Generator
                     │
                     ▼
        Top 100 Ranked Candidates
                     │
                     ▼
     Flask Dashboard & CSV Download
```

## Output
The generated CSV follows the Redrob submission specification and contains the Top 100 ranked candidates with their ranking scores and human-readable explanations.

The system generates:

- Top 100 ranked candidates
- Candidate ranking score
- Human-readable explanation for every recommendation
- Submission-ready CSV file
- Interactive dashboard for ranking visualization and CSV download

## Team

**Team Name:** QueryQueens

| Member | Contribution |
|--------|--------------|
| Neelima Alamanda | Team Lead, Hybrid Ranking Engine & Semantic Ranking |
| Uma | Backend Development & Semantic Ranking |
| Phanisri | Frontend Development & Evaluation Module |
| Pavani | Parser, Feature Engineering & Candidate Intelligence |

## Future Improvements

- Support multiple job descriptions.
- Add recruiter dashboard with candidate filtering.
- Support configurable ranking weights for different hiring scenarios.
- Integrate LLM-assisted candidate insights for recruiter decision support.
- Support real-time candidate ranking through APIs.

> **Note:** During the first execution, the Sentence Transformer model may be downloaded and cached locally. Subsequent runs use the cached model for faster execution.
