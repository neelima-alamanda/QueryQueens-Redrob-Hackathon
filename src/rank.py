import json
AI_TITLES = {
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "nlp engineer",
    "recommendation systems engineer",
    "search engineer"
}
RELATED_TECH_TITLES = {
    "java developer",
    ".net developer",
    "devops engineer",
    "cloud engineer",
    "full stack developer",
    "qa engineer",
    "mobile developer"
}
AI_SKILLS = {
    "python", "nlp", "llm", "fine-tuning llms",
    "milvus", "lora", "rag", "embeddings",
    "vector database", "retrieval", "ranking",
    "flask", "bentoml"
}
GOOD_TITLES = {
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "data scientist",
    "nlp engineer",
    "search engineer",
    "recommendation systems engineer",
    "backend engineer",
    "data engineer",
    "software engineer"
}

BAD_TITLES = {
    "accountant",
    "graphic designer",
    "hr manager",
    "human resources manager",
    "sales executive",
    "marketing manager",
    "operations manager",
    "business analyst"
}
def generate_reason(candidate):

    reasons = []

    title = candidate["profile"]["current_title"]
    exp = candidate["profile"]["years_of_experience"]

    reasons.append(f"{exp} years experience")

    if candidate["redrob_signals"]["open_to_work_flag"]:
        reasons.append("open to work")

    if title.lower() in AI_TITLES:
        reasons.append("relevant AI-focused role")

    elif title.lower() in RELATED_TECH_TITLES:
        reasons.append("strong technical background")

    elif title.lower() in GOOD_TITLES:
        reasons.append("relevant engineering background")

    return ", ".join(reasons)
def inspect_candidate(candidate):

    print("\n" + "=" * 60)

    print("Candidate ID:", candidate["candidate_id"])
    print("Title:", candidate["profile"]["current_title"])
    print("Experience:", candidate["profile"]["years_of_experience"])

    print("\nTop Skills:")

    for skill in candidate["skills"][:10]:
        print("-", skill["name"])
def calculate_score(candidate):

    score = 0

    # Current Title
    title = candidate["profile"]["current_title"].lower()

    if title in AI_TITLES:
        score += 30

    elif title in GOOD_TITLES:
        score += 20

    elif title in RELATED_TECH_TITLES:
        score += 10

    elif title in BAD_TITLES:
        score -= 20
    # Experience Score
    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 20
    elif 3 <= exp < 5:
        score += 12
    elif exp > 9:
        score += 15

    # Skills Score
    skills = candidate["skills"]

    for skill in skills:
        name = skill["name"].lower()

        if name in AI_SKILLS:
            score += 3

    # Open To Work
    if candidate["redrob_signals"]["open_to_work_flag"]:
        score += 10

    # GitHub Activity
    github_score = candidate["redrob_signals"]["github_activity_score"]
    score += min(github_score, 10)

    # Interview Completion
    score += candidate["redrob_signals"]["interview_completion_rate"] * 10
    career_text = ""

    for job in candidate["career_history"]:
        career_text += job["title"].lower() + " "
        career_text += job["description"].lower() + " "

    AI_KEYWORDS = [
        "retrieval",
        "ranking",
        "recommendation",
        "search",
        "embedding",
        "vector",
        "nlp",
        "machine learning",
        "llm"
    ]

    for keyword in AI_KEYWORDS:
        if keyword in career_text:
            score += 3
    return round(score, 2)


with open("data/sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)
print("\nALL CURRENT TITLES\n")

titles = {}

for candidate in candidates:
    title = candidate["profile"]["current_title"]

    titles[title] = titles.get(title, 0) + 1

for title, count in sorted(titles.items()):
    print(f"{title}: {count}")
results = []

for candidate in candidates:
    score = calculate_score(candidate)

    results.append({
    "candidate_id": candidate["candidate_id"],
    "score": score,
    "title": candidate["profile"]["current_title"],
    "experience": candidate["profile"]["years_of_experience"],
    "reason": generate_reason(candidate)
    })  

results.sort(key=lambda x: x["score"], reverse=True)
top_ids = [x["candidate_id"] for x in results[:5]]

for candidate in candidates:
    if candidate["candidate_id"] in top_ids:
        inspect_candidate(candidate)

print("\nTOP 10 CANDIDATES\n")

for rank, candidate in enumerate(results[:10], start=1):
    print(
    f"{rank}. {candidate['candidate_id']} | "
    f"{candidate['title']} | "
    f"{candidate['experience']} yrs | "
    f"Score: {candidate['score']} | "
    f"{candidate['reason']}"
    )