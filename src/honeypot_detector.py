from datetime import datetime
def honeypot_penalty(parsed_candidate):
    """
    Detect suspicious/inconsistent candidate profiles.
    Returns:
        penalty (int)
        reasons (list)
    """

    penalty = 0
    reasons = []

    profile = parsed_candidate.get("profile", {})
    skills = parsed_candidate.get("skills", [])
    career_history = parsed_candidate.get("career_history", [])
    education = parsed_candidate.get("education", [])

    title = profile.get("current_title", "").lower()
    experience = profile.get("years_of_experience", 0)

    skill_names = []

    for skill in skills:
        if isinstance(skill, dict):
            skill_names.append(skill.get("name", "").lower())
        else:
            skill_names.append(str(skill).lower())

    ai_titles = [
        "ai engineer",
        "machine learning engineer",
        "ml engineer",
        "data scientist",
        "nlp engineer",
        "search engineer",
        "backend engineer"
    ]

    ai_skills = [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "retrieval",
        "ranking",
        "embedding",
        "llm",
        "vector database",
        "faiss",
        "milvus",
        "pinecone",
        "weaviate",
        "qdrant",
        "lora",
        "qlora",
        "peft",
    ]

    matched_ai = sum(
        1 for skill in ai_skills
        if skill in skill_names
    )

    # Rule 1
    if experience >= 8 and len(career_history) == 0:
        penalty += 15
        reasons.append("Missing career history")

    elif experience >= 5 and len(career_history) == 0:
        penalty += 10
        reasons.append("Missing career history")

    # Rule 2
    matched_ratio = matched_ai / max(len(ai_skills), 1)

    if any(t in title for t in ai_titles):

        if matched_ratio < 0.20:
            penalty += 10
            reasons.append("Very weak AI profile")

        elif matched_ratio < 0.40:
            penalty += 5
            reasons.append("Limited AI skills")

    # Rule 3
    senior_titles = [
        "principal",
        "staff",
        "lead",
        "architect",
        "head",
        "director"
    ]

    if any(t in title for t in senior_titles) and experience < 4:
        penalty += 10
        reasons.append("Senior title with insufficient experience")

    # Rule 4
    if experience >= 8 and not education:
        penalty += 5
        reasons.append("High experience but no education")

    # Rule 5
    if experience <= 3 and len(career_history) >= 5:
        penalty += 8
        reasons.append("Too many companies for experience")

    # Rule 6
    if len(skill_names) >= 30:
        penalty += 6
        reasons.append("Possible skill stuffing")

    elif experience <= 2 and len(skill_names) >= 20:
        penalty += 8
        reasons.append("Too many skills for experience")

    # Rule 7
    companies = []

    for job in career_history:

        company = job.get("company", "").lower()

        if company and company in companies:
            penalty += 5
            reasons.append("Duplicate company history")
            break

        companies.append(company)

    # Rule 8
    titles = []

    for job in career_history:

        job_title = job.get("title", "").lower()

        if job_title in titles:
            penalty += 4
            reasons.append("Repeated job titles")
            break

        titles.append(job_title)

    # Rule 9
    summary = profile.get("summary", "")

    if len(summary.strip()) == 0 and len(skill_names) < 3:
        penalty += 6
        reasons.append("Incomplete profile")

    #Rule 10
    signals = parsed_candidate.get("redrob_signals", {})

    if (
        signals.get("open_to_work_flag", False)
        and signals.get("notice_period_days", 0) > 120
    ):
        penalty += 4
        reasons.append("Open to work with long notice period")

    response = signals.get(
        "recruiter_response_rate",
        0
    )

    if response < 0.10:
        penalty += 4
        reasons.append("Very low recruiter response")
    last_active = signals.get("last_active_date")

    if last_active:

        days = (
            datetime.now() -
            datetime.strptime(
                last_active,
                "%Y-%m-%d"
            )
        ).days

        if days > 180:
            penalty += 3
            reasons.append("Profile inactive for a long time")
    return penalty, reasons
