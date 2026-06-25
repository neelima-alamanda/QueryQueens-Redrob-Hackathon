def behavior_score(redrob_signals):
    """
    Recruiter-oriented behavior scoring.

    Measures whether a candidate is
    actually worth reaching out to,
    not just technically strong.
    """

    score = 0

    # ----------------------------
    # Open To Work
    # ----------------------------

    if redrob_signals.get("open_to_work_flag", False):
        score += 30
    else:
        score += 5

    # ----------------------------
    # Recruiter Response Rate
    # ----------------------------

    response = redrob_signals.get(
        "recruiter_response_rate",
        0
    )

    if response >= 0.90:
        score += 25
    elif response >= 0.70:
        score += 20
    elif response >= 0.50:
        score += 15
    elif response >= 0.30:
        score += 8
    else:
        score += 2

    # ----------------------------
    # Interview Completion
    # ----------------------------

    interview = redrob_signals.get(
        "interview_completion_rate",
        0
    )

    if interview >= 0.90:
        score += 20
    elif interview >= 0.70:
        score += 15
    elif interview >= 0.50:
        score += 10
    else:
        score += 4

    # ----------------------------
    # Profile Completeness
    # ----------------------------

    profile = redrob_signals.get(
        "profile_completeness",
        0
    )

    score += round(profile * 15)

    # ----------------------------
    # GitHub Activity
    # ----------------------------

    github = redrob_signals.get(
        "github_activity_score",
        0
    )

    open_to_work = redrob_signals.get(
        "open_to_work_flag",
        False
    )

    if open_to_work:

        if github >= 9:
            score += 10

        elif github >= 7:
            score += 8

        elif github >= 5:
            score += 6

        elif github >= 3:
            score += 4

        else:
            score += 2

    else:
        # GitHub matters less if the candidate
        # is not actively looking.
        if github >= 9:
            score += 4
        elif github >= 7:
            score += 3
        else:
            score += 1
    score = max(score, 0)
    score = min(score, 100)

    return round(score, 2)