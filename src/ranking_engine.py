from job_profile import JOB_PROFILE
from honeypot_detector import honeypot_penalty


def calculate_final_score(
    parsed_candidate,
    features,
    behavior_score,
    consistency_score
):

    score = 0

    skills = [s.lower() for s in features.get("skills", [])]

    title = features.get("current_title", "").lower()

    experience = features.get("years_of_experience", 0)

    career_history = features.get("career_history", [])
    penalty, _ = honeypot_penalty(parsed_candidate)

    # ----------------------------
    # 1. Current Title
    # ----------------------------
    preferred_titles = [
        t.lower()
        for t in JOB_PROFILE["preferred_titles"]
    ]

    if title in preferred_titles:
        score += 25

    # ----------------------------
    # 2. Must-have Skills
    # ----------------------------
    must_have = JOB_PROFILE["must_have_skills"]

    matched_required = sum(
        1
        for skill in must_have
        if skill.lower() in skills
    )

    score += min(matched_required * 3, 30)
    if matched_required >= 8:
        score += 5

    # ----------------------------
    # 3. Preferred Skills
    # ----------------------------
    preferred = JOB_PROFILE["preferred_skills"]

    matched_bonus = sum(
        1
        for skill in preferred
        if skill.lower() in skills
    )

    score += min(matched_bonus * 2, 10)

    # ----------------------------
    # 4. Experience
    # ----------------------------
    min_exp, max_exp = JOB_PROFILE["ideal_experience"]

    if min_exp <= experience <= max_exp:
        score += 15
    elif experience > max_exp:
        score += 10
    elif experience >= 3:
        score += 5

    # ----------------------------
    # 5. Consulting Background Penalty
    # ----------------------------
    consulting = JOB_PROFILE["consulting_companies"]

    for job in career_history:

        company = job.get("company", "").lower()

        if any(c in company for c in consulting):
            score -= 8
            break
    # ----------------------------
    # 6. Product Company Bonus
    # ----------------------------

    product_companies = [
        "google",
        "amazon",
        "microsoft",
        "meta",
        "apple",
        "netflix",
        "uber",
        "airbnb",
        "stripe",
        "atlassian"
    ]

    for job in career_history:

        company = job.get("company", "").lower()

        if any(p in company for p in product_companies):
            score += 5
            break

    # ----------------------------
    # 6. Irrelevant Current Title
    # ----------------------------
    penalty_titles = [
        t.lower()
        for t in JOB_PROFILE["penalty_titles"]
    ]

    if title in penalty_titles:
        score -= 10
    # ----------------------------
    # Experience + Skill Bonus
    # ----------------------------

    if experience >= 5 and matched_required >= 6:
        score += 5
    # ----------------------------
    # Retrieval AI Bonus
    # ----------------------------

    retrieval_skills = [
        "retrieval",
        "rag",
            "vector database",
        "pinecone",
        "weaviate",
        "qdrant",
        "milvus",
        "faiss",
        "elasticsearch",
        "opensearch"
    ]

    retrieval_matches = sum(
        1
        for skill in retrieval_skills
        if skill in skills
    )

    score += min(retrieval_matches * 2, 10)
    # ----------------------------
    # LLM Bonus
    # ----------------------------

    llm_skills = [
        "llm",
        "transformers",
        "embedding",
        "embeddings",
        "sentence transformers",
        "bge",
        "e5",
        "fine tuning",
        "lora",
        "qlora",
        "peft"
    ]

    llm_matches = sum(
        1
        for skill in llm_skills
        if skill in skills
    )

    score += min(llm_matches * 2, 10)
    # ----------------------------
    # 7. Behaviour
    # ----------------------------

    score += behavior_score * 0.5

    # ----------------------------
    # 8. Consistency
    # ----------------------------
    score += consistency_score * 0.3

   
    score -= penalty
    score = max(score, 0)
    score = min(score, 100)

    return round(score, 2)