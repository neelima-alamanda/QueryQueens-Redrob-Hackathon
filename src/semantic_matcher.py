from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_semantic_similarity(job_text, candidate_text):
    """
    Returns semantic similarity score between
    job description and candidate profile.
    """

    # Generate embeddings
    job_embedding = model.encode(job_text)
    candidate_embedding = model.encode(candidate_text)

    # Calculate cosine similarity
    similarity = cosine_similarity(
        [job_embedding],
        [candidate_embedding]
    )[0][0]

    return float(similarity)
def build_candidate_text(candidate):
    """
    Converts parsed candidate data into a single text string
    for semantic similarity comparison.
    """

    parts = []

    # Profile information
    profile = candidate.get("profile", {})
    parts.append(profile.get("headline", ""))
    parts.append(profile.get("summary", ""))
    parts.append(profile.get("current_role", ""))

    # Career history
    career_history = candidate.get("career_history", [])
    for job in career_history:
        if isinstance(job, dict):
            parts.append(job.get("title", ""))
            parts.append(job.get("company", ""))
            parts.append(job.get("description", ""))

    # Skills
    parts.extend(candidate.get("skills", []))

    # Certifications
    parts.extend(candidate.get("certifications", []))

    # Education
    education = candidate.get("education", [])
    for edu in education:
        if isinstance(edu, dict):
            parts.append(edu.get("degree", ""))
            parts.append(edu.get("field", ""))

    # Languages
    parts.extend(candidate.get("languages", []))

    return " ".join(str(item) for item in parts if item)