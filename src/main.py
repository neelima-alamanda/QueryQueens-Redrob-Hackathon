import json

from parser import parse_candidate
from features import extract_features
from behavior import behavior_score
from consistency import consistency_score
from ranking_engine import (
    calculate_final_score,
    calculate_hybrid_score
)
from decision_explainer import generate_explanation
from evaluation import generate_submission
from semantic_matcher import semantic_rerank
from config import (
    TOP_K,
    SEMANTIC_RERANK_LIMIT
)


def load_candidates(path):
    candidates = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            candidates.append(json.loads(line))

    return candidates


def main():

    # Load candidates
    candidates = load_candidates("data/candidates.jsonl")

    processed_candidates = []
    for candidate in candidates:

        parsed_candidate = parse_candidate(candidate)

        features = extract_features(parsed_candidate)

        behavior = behavior_score(
    parsed_candidate.get("redrob_signals", {})
)

        consistency = consistency_score(parsed_candidate)
        
       
        final_score = calculate_final_score(
    parsed_candidate,
    features,
    behavior,
    consistency
)

        explanation = generate_explanation(
            parsed_candidate,
            features,
            behavior,
            consistency,
            final_score
        )
        processed_candidates.append({
    "candidate_id": parsed_candidate["candidate_id"],

    "candidate": parsed_candidate,

    "score": final_score,

    "reason": explanation,

    "role": features.get("current_title", ""),

    "experience": features.get(
        "years_of_experience",
        0
    ),

    "skills": features.get(
        "skills",
        []
    ),

    "behavior": behavior,

    "consistency": consistency
})
    processed_candidates.sort(
        key=lambda x: (
            x["score"],
            x["candidate_id"]
        ),
        reverse=True
    )

    top_candidates = processed_candidates[
        :SEMANTIC_RERANK_LIMIT
    ]

    # ----------------------------------
    # Semantic Re-ranking (Batch)
    # ----------------------------------

    parsed_candidates = [
        candidate["candidate"]
        for candidate in top_candidates
    ]

    semantic_scores = semantic_rerank(
        parsed_candidates
    )

    for candidate, semantic_score in zip(
        top_candidates,
        semantic_scores
    ):

        candidate["score"] = calculate_hybrid_score(
            candidate["score"],
            semantic_score
        )

    # ----------------------------------
    # Final Ranking
    # ----------------------------------

    top_candidates.sort(
        key=lambda x: (
            x["score"],
            x["candidate_id"]
        ),
        reverse=True
    )

    generate_submission(
        top_candidates[:TOP_K]
    )


if __name__ == "__main__":
    main()