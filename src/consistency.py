def consistency_score(parsed_candidate):
    """
    Checks whether the candidate profile is internally consistent.
    """

    score = 0

    profile = parsed_candidate.get("profile", {})

    skills = [
        skill.get("name", "").lower()
        for skill in parsed_candidate.get("skills", [])
    ]

    career_history = parsed_candidate.get("career_history", [])

    education = parsed_candidate.get("education", [])

    title = profile.get("current_title", "").lower()

    experience = profile.get("years_of_experience", 0)

    

    # -------------------------
    # AI-related Title
    # -------------------------

    ai_titles = [
        "ai engineer",
        "machine learning engineer",
        "ml engineer",
        "data scientist",
        "nlp engineer",
        "search engineer",
        "backend engineer"
    ]
    important_skills = [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "retrieval",
        "ranking",
        "embedding",
        "llm",
        "vector database"
    ]


    title_is_ai = any(
        t in title
        for t in ai_titles
    )

    skill_overlap = any(
        skill in skills
        for skill in important_skills
    )

    if title_is_ai and skill_overlap:
        score += 20

    elif title_is_ai:
        score += 8
    

    # -------------------------
    # Relevant Skills
    # -------------------------

    matched = sum(
        1
        for skill in important_skills
        if skill in skills
    )

    score += min(matched * 3, 20)

    # -------------------------
    # Career History Exists
    # -------------------------

    if len(career_history) >= 2:
        score += 15
    elif len(career_history) == 1:
        score += 8

    # -------------------------
    # Education Exists
    # -------------------------

    if education:
        score += 10
    # -------------------------
    # Experience Consistency
    # -------------------------

    if experience >= 5 and len(career_history) >= 2:
        score += 10
    elif experience >= 3 and len(career_history) >= 1:
        score += 5

    # -------------------------
    # Profile Completeness
    # -------------------------

    if (
        profile.get("current_title")
        and profile.get("years_of_experience") is not None
        and skills
    ):
        score += 15
    # -------------------------
    # Career Title Matches Skills
    # -------------------------

    if title_is_ai and matched >= 4:
        score += 10
    # -------------------------
    # Missing Career Penalty
    # -------------------------

    if experience >= 5 and len(career_history) == 0:
        score -= 10

    score = max(score, 0)
    score = min(score, 100)

    return round(score, 2)