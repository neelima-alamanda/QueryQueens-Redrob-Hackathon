def calculate_behavior_score(redrob_signals):
    """
    Calculates a behavior score using Redrob behavioral signals.
    """

    score = 0

    if redrob_signals.get("open_to_work_flag"):
        score += 20

    score += min(
        redrob_signals.get("github_activity_score", 0),
        10
    )

    score += (
        redrob_signals.get("interview_completion_rate", 0) * 10
    )

    score += (
        redrob_signals.get("recruiter_response_rate", 0) * 15
    )

    score += (
        redrob_signals.get("profile_completeness", 0) * 10
    )

    return round(score, 2)