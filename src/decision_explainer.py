def generate_explanation(
    candidate,
    features,
    behavior_score,
    consistency_score,
    final_score
):

    reasons = []

    profile = candidate["profile"]

    title = profile["current_title"]

    experience = profile["years_of_experience"]

    reasons.append(f"{experience} years of experience as {title}")

    if features["technical_score"] >= 80:
        reasons.append("Strong technical skill match")

    if features["career_score"] >= 80:
        reasons.append("Relevant career progression")

    if behavior_score >= 80:
        reasons.append("Positive behavioral signals")

    if consistency_score >= 80:
        reasons.append("Consistent professional profile")

    return ". ".join(reasons)