"""
Structured representation of the Redrob AI Engineer Job Description.

This file converts the human-written JD into machine-readable rules.
The ranking engine will use these signals instead of relying on simple
keyword matching.
"""

JOB_PROFILE = {

    # ------------------------------------
    # Preferred Job Titles
    # ------------------------------------
    "preferred_titles": [
        "AI Engineer",
        "Machine Learning Engineer",
        "ML Engineer",
        "Applied Scientist",
        "Data Scientist",
        "NLP Engineer",
        "Search Engineer",
        "Recommendation Engineer",
        "Software Engineer",
        "Backend Engineer"
    ],

    # ------------------------------------
    # Strong Technical Skills
    # ------------------------------------
    "must_have_skills": [
        "python",
        "embeddings",
        "retrieval",
        "ranking",
        "vector database",
        "pinecone",
        "weaviate",
        "qdrant",
        "milvus",
        "faiss",
        "elasticsearch",
        "opensearch",
        "sentence transformers",
        "bge",
        "e5",
        "evaluation",
        "ndcg",
        "mrr",
        "map"
    ],

    # ------------------------------------
    # Bonus Skills
    # ------------------------------------
    "preferred_skills": [
        "llm",
        "rag",
        "langgraph",
        "transformers",
        "fine tuning",
        "lora",
        "qlora",
        "peft",
        "learning to rank",
        "xgboost",
        "a/b testing",
        "distributed systems",
        "recommendation system"
    ],

    # ------------------------------------
    # Preferred Industries
    # ------------------------------------
    "preferred_domains": [
        "product",
        "ai",
        "machine learning",
        "search",
        "recommendation",
        "hrtech",
        "marketplace"
    ],

    # ------------------------------------
    # Titles that should receive penalties
    # ------------------------------------
    "penalty_titles": [
        "marketing manager",
        "graphic designer",
        "civil engineer",
        "mechanical engineer",
        "customer support",
        "sales executive",
        "content writer",
        "hr manager",
        "accountant"
    ],

    # ------------------------------------
    # Consulting companies mentioned in JD
    # ------------------------------------
    "consulting_companies": [
        "tcs",
        "infosys",
        "wipro",
        "accenture",
        "cognizant",
        "capgemini"
    ],

    # ------------------------------------
    # Experience Range
    # ------------------------------------
    "ideal_experience": (5, 9),

    # ------------------------------------
    # Behaviour Expectations
    # ------------------------------------
    "behavior_expectations": {
        "minimum_response_rate": 0.30,
        "recent_activity_required": True,
        "open_to_work_preferred": True
    }

}