from job_description_loader import load_job_description
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")
JOB_DESCRIPTION = load_job_description()

JOB_EMBEDDING = model.encode(
    JOB_DESCRIPTION,
    convert_to_numpy=True
)


def build_candidate_text(candidate):

    parts = []

    profile = candidate.get("profile", {})

    parts.append(profile.get("headline", ""))
    parts.append(profile.get("summary", ""))
    parts.append(profile.get("current_title", ""))

    for job in candidate.get("career_history", []):
        parts.append(job.get("title", ""))
        parts.append(job.get("company", ""))
        parts.append(job.get("description", ""))

    for skill in candidate.get("skills", []):
        if isinstance(skill, dict):
            parts.append(skill.get("name", ""))

    for cert in candidate.get("certifications", []):
        if isinstance(cert, dict):
            parts.append(cert.get("name", ""))

    for edu in candidate.get("education", []):
        if isinstance(edu, dict):
            parts.append(edu.get("degree", ""))
            parts.append(edu.get("field_of_study", ""))

    return " ".join(parts)


def semantic_rerank(parsed_candidates):

    candidate_texts = [
        build_candidate_text(candidate)
        for candidate in parsed_candidates
    ]

    candidate_embeddings = model.encode(
        candidate_texts,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        [JOB_EMBEDDING],
        candidate_embeddings
    )[0]

    return similarities.tolist()