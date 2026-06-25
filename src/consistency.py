def consistency_score(candidate):

    score = 100

    profile = candidate["profile"]

    title = profile["current_title"].lower()

    experience = profile["years_of_experience"]

    skills = [
        skill["name"].lower()
        for skill in candidate["skills"]
    ]

    if "engineer" in title and experience < 1:
        score -= 25

    if "machine learning" in title and "python" not in skills:
        score -= 20

    if "data scientist" in title and "python" not in skills:
        score -= 20

    if "backend" in title and "sql" not in skills:
        score -= 15

    if experience > 12 and len(skills) < 5:
        score -= 15

    return max(score, 0)