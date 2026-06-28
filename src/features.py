def extract_features(parsed_candidate):
    """
    Extract structured candidate features.
    This module ONLY extracts information.
    No scoring happens here.
    """

    profile = parsed_candidate.get("profile", {})

    # ---------- Skills ----------
    skills = [
        skill.get("name", "").strip()
        for skill in parsed_candidate.get("skills", [])
    ]

    normalized_skills = [
        skill.lower()
        for skill in skills
    ]

    # ---------- Features ----------
    features = {

        # Basic Profile
        "current_title": profile.get(
            "current_title",
            ""
        ),

        "years_of_experience": profile.get(
            "years_of_experience",
            0
        ),

        # Skills
        "skills": skills,
        "normalized_skills": normalized_skills,
        "skill_count": len(skills),

        # Career
        "career_history": parsed_candidate.get(
            "career_history",
            []
        ),

        "career_count": len(
            parsed_candidate.get(
                "career_history",
                []
            )
        ),
        # AI Profile extracted by parser
        "ai_profile": parsed_candidate.get(
            "ai_profile",
            {}
        ),

        # Education
        "education": parsed_candidate.get(
            "education",
            []
        ),

        # Certifications
        "certifications": parsed_candidate.get(
            "certifications",
            []
        ),

        "certification_count": len(
            parsed_candidate.get(
                "certifications",
                []
            )
        ),

        # Languages
        "languages": parsed_candidate.get(
            "languages",
            []
        ),

        # Behaviour
        "redrob_signals": parsed_candidate.get(
            "redrob_signals",
            {}
        ),
        # Filled later by ranking engine
        "technical_score": 0,

        "career_score": 0,

        "critical_skill_matches": 0,

        "preferred_skill_matches": 0

    }

    return features