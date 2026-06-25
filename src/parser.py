def parse_candidate(candidate):
    """
    Extract the important sections from a candidate profile.
    Returns a structured dictionary for the feature extraction module.
    """

    return {
        "candidate_id": candidate.get("candidate_id"),

        "profile": candidate.get("profile", {}),

        "career_history": candidate.get("career_history", []),

        "skills": candidate.get("skills", []),

        "education": candidate.get("education", []),

        "certifications": candidate.get("certifications", []),

        "languages": candidate.get("languages", []),

        "redrob_signals": candidate.get("redrob_signals", {})
    }