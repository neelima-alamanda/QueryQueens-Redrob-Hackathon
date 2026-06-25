def parse_candidate(candidate):
    """
    Parse a candidate profile and extract structured
    information for downstream ranking modules.
    """

    profile = candidate.get("profile", {})

    career_history = candidate.get("career_history", [])

    skills = candidate.get("skills", [])

    education = candidate.get("education", [])

    certifications = candidate.get("certifications", [])

    languages = candidate.get("languages", [])

    redrob_signals = candidate.get("redrob_signals", {})

    # ------------------------------------
    # Combine all text for semantic checks
    # ------------------------------------

    searchable_text = []

    searchable_text.append(
        profile.get("current_title", "")
    )

    for job in career_history:
        searchable_text.append(
            job.get("title", "")
        )
        searchable_text.append(
            job.get("description", "")
        )

    for skill in skills:
        searchable_text.append(
            skill.get("name", "")
        )

    text = " ".join(searchable_text).lower()

    # ------------------------------------
    # AI Profile
    # ------------------------------------

    ai_profile = {

        # Core AI
        "worked_on_embeddings":
            "embedding" in text,

        "worked_on_retrieval":
            "retrieval" in text
            or "search" in text,

        "worked_on_ranking":
            "ranking" in text
            or "recommendation" in text,

        "worked_on_llm":
            any(word in text for word in [
                "llm",
                "gpt",
                "transformer",
                "bert",
                "llama"
            ]),

        "worked_on_vector_db":
            any(db in text for db in [
                "pinecone",
                "faiss",
                "weaviate",
                "qdrant",
                "milvus",
                "elasticsearch",
                "opensearch"
            ]),

        # Production Engineering
        "product_engineering":
            any(word in text for word in [
                "production",
                "deployed",
                "deployment",
                "real-time",
                "users",
                "scalable",
                "scale",
                "pipeline"
            ]),

        # Evaluation Frameworks
        "evaluation_framework":
            any(word in text for word in [
                "ndcg",
                "mrr",
                "map",
                "precision",
                "recall",
                "ab test",
                "a/b",
                "offline evaluation"
            ]),

        # Fine-tuning
        "fine_tuning":
            any(word in text for word in [
                "lora",
                "qlora",
                "peft",
                "fine tuning",
                "finetuning"
            ]),

        # Learning To Rank
        "learning_to_rank":
            any(word in text for word in [
                "xgboost",
                "lightgbm",
                "learning to rank",
                "ltr"
            ]),

        # HR Domain
        "hr_domain":
            any(word in text for word in [
                "recruitment",
                "hiring",
                "talent",
                "ats",
                "hr"
            ]),

        # Open Source
        "open_source":
            any(word in text for word in [
                "github",
                "open source",
                "contributor"
            ]),

        # Distributed Systems
        "distributed_systems":
            any(word in text for word in [
                "kubernetes",
                "docker",
                "distributed",
                "microservice",
                "spark"
            ]),

        # Startup Signals
        "startup_experience":
            "startup" in text,

        # Research
        "research_background":
            "research" in text,

        # Recommendation/Search
        "recommendation_system":
            "recommendation" in text,

        "search_engine":
            "search engine" in text,

        # Consulting Companies
        "consulting_background":
            any(company in text for company in [
                "tcs",
                "infosys",
                "wipro",
                "accenture",
                "cognizant",
                "capgemini"
            ])
    }
    return {

        "candidate_id": candidate.get("candidate_id"),

        "profile": profile,

        "career_history": career_history,

        "skills": skills,

        "education": education,

        "certifications": certifications,

        "languages": languages,

        "redrob_signals": redrob_signals,

        "ai_profile": ai_profile
    }