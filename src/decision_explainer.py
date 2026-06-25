REQUIRED_SKILLS = [
    "python",
    "embedding",
    "embeddings",
    "retrieval",
    "ranking",
    "llm",
    "transformer",
    "vector database",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "elasticsearch",
    "opensearch",
    "evaluation",
]

PREFERRED_SKILLS = [
    "lora",
    "qlora",
    "peft",
    "learning to rank",
    "xgboost",
    "recommendation",
    "hr tech",
    "recruitment",
    "distributed systems",
    "open source",
]


def generate_explanation(
    candidate,
    features,
    behavior_score,
    consistency_score,
    final_score,
):

    profile = candidate["profile"]

    title = profile.get("current_title", "Unknown Role")

    experience = profile.get("years_of_experience", 0)

    skills = [
        skill.lower()
        for skill in features.get("skills", [])
    ]

    reasons = []

    # Experience

    reasons.append(
        f"{experience} years of experience as {title}"
    )

    # Required Skills

    matched_required = []

    for skill in REQUIRED_SKILLS:
        if any(skill in s for s in skills):
            matched_required.append(skill)

    if matched_required:
        reasons.append(
            f"Matched {len(matched_required)} critical AI skills"
        )

    # Preferred Skills

    matched_preferred = []

    for skill in PREFERRED_SKILLS:
        if any(skill in s for s in skills):
            matched_preferred.append(skill)

    if matched_preferred:
        reasons.append(
            f"{len(matched_preferred)} preferred skills detected"
        )

    # Technical

    if features.get("technical_score", 0) >= 80:
        reasons.append("Strong technical profile")

    # Career

    if features.get("career_score", 0) >= 80:
        reasons.append("Relevant AI career progression")

    # Behaviour

    if behavior_score >= 70:
        reasons.append("Positive recruiter engagement")

    # Consistency

    if consistency_score >= 80:
        reasons.append("Highly consistent profile")

    reasons.append(f"Final Score: {final_score}")

    return ". ".join(reasons)