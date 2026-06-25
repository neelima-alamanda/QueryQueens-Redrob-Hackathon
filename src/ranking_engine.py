from config import (
    TECHNICAL_WEIGHT,
    CAREER_WEIGHT,
    BEHAVIOR_WEIGHT,
    CONSISTENCY_WEIGHT,
)


def calculate_final_score(features, behavior_score, consistency_score):

    technical_score = features["technical_score"]

    career_score = features["career_score"]

    final_score = (
        technical_score * TECHNICAL_WEIGHT
        + career_score * CAREER_WEIGHT
        + behavior_score * BEHAVIOR_WEIGHT
        + consistency_score * CONSISTENCY_WEIGHT
    )

    return round(final_score, 2)