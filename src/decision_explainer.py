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

    profile = candidate.get("profile", {})

    title = profile.get("current_title", "Unknown Role")
    experience = profile.get("years_of_experience", 0)

    skills = [
        skill.lower()
        for skill in features.get("skills", [])
    ]

    reasons = []
    # Overall recommendation

    if final_score >= 85:
        reasons.append(
        "Excellent match for the Senior AI Engineer role"
    )
    elif final_score >= 70:
        reasons.append(
        "Strong match for the role"
    )
    elif final_score >= 55:
        reasons.append(
        "Moderate match with some skill gaps"
    )
    else:
        reasons.append(
        "Limited match for the target role"
    )

    # Role + Experience
    reasons.append(
        f"{experience} years of experience as {title}"
    )

    # Critical Skills
    matched_required = []

    for skill in REQUIRED_SKILLS:
        if any(skill in s for s in skills):
            matched_required.append(skill)
    if matched_required:
        reasons.append(
        f"Matched {len(matched_required)} critical AI skills including {', '.join(matched_required[:5])}"
    )
    else:
        reasons.append(
        "Few critical AI skills detected"
    )


    # Preferred Skills
    matched_preferred = []

    for skill in PREFERRED_SKILLS:
        if any(skill == s or skill in s for s in skills):
            if matched_preferred:
                reasons.append(
            f"Preferred skills: {', '.join(matched_preferred[:3])}"
        )
    # Experience relevance

    if 5 <= experience <= 9:
        reasons.append(
        "Experience matches the preferred hiring range"
    )
    elif experience > 9:
        reasons.append(
        "Experienced beyond the preferred range"
    )
    else:
        reasons.append(
        "Below the preferred experience range"
    )

    # Technical Profile
    if features.get("technical_score", 0) >= 80:
        reasons.append(
            "Strong technical background"
        )

    # Career Progression
    if features.get("career_score", 0) >= 80:
        reasons.append(
            "Career aligns well with AI engineering"
        )

    # Behaviour
    if behavior_score >= 70:
        reasons.append(
            "Strong recruiter engagement"
        )
    elif behavior_score >= 50:
        reasons.append(
        "Average recruiter engagement"
    )
    elif behavior_score < 40:
        reasons.append(
            "Low recruiter engagement"
        )

    # Consistency
    if consistency_score >= 80:
        reasons.append(
            "Profile information is highly consistent"
        )
    elif consistency_score < 50:
        reasons.append(
            "Some inconsistencies detected"
        )

    reasons.append(
    f"Final ranking score: {final_score}"
)

    return ". ".join(reasons[:8])
