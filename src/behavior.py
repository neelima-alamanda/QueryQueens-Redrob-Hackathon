from datetime import datetime
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
        "profile_completeness_score",
        0
    )
    # Dataset stores this as a percentage (0–100).
    # Convert it to a 0–1 scale before applying the weight.
    score += round((profile / 100) * 15)
    

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

    # ----------------------------
    # Notice Period
    # ----------------------------

    notice = redrob_signals.get(
        "notice_period_days",
        90
    )

    if notice <= 30:
        score += 8
    elif notice <= 60:
        score += 6
    elif notice <= 90:
        score += 3
    else:
        score += 1

    # ----------------------------
    # Last Active
    # ----------------------------

    last_active = redrob_signals.get("last_active_date")

    if last_active:

        last_active = datetime.strptime(
            last_active,
            "%Y-%m-%d"
        )

        days = (
            datetime.now() - last_active
        ).days

        if days <= 7:
            score += 5
        elif days <= 30:
            score += 3
        elif days <= 90:
            score += 1
    

    search_appearance = redrob_signals.get(
        "search_appearance_30d",
        0
    )

    if search_appearance >= 50:
        score += 5
    elif search_appearance >= 20:
        score += 3

    # ----------------------------
    # Saved by Recruiters
    # ----------------------------

    saved = redrob_signals.get(
        "saved_by_recruiters_30d",
        0
    )

    if saved >= 20:
        score += 5
    elif saved >= 10:
        score += 3

    # ----------------------------
    # Offer Acceptance Rate
    # ----------------------------

    offer = redrob_signals.get(
        "offer_acceptance_rate",
        0
    )

    if offer >= 0.80:
        score += 6
    elif offer >= 0.60:
        score += 4
    elif offer >= 0.40:
        score += 2

    # ----------------------------
    # Skill Assessment Scores
    # ----------------------------

    assessments = redrob_signals.get(
        "skill_assessment_scores",
        {}
    )

    if assessments:

        average = (
            sum(assessments.values()) /
            len(assessments)
        )

        if average >= 80:
            score += 6
        elif average >= 60:
            score += 4
        elif average >= 40:
            score += 2
    # ----------------------------
    # Verified Profile
    # ----------------------------

    if redrob_signals.get("verified_email", False):
        score += 2

    if redrob_signals.get("verified_phone", False):
        score += 2

    if redrob_signals.get("linkedin_connected", False):
        score += 2
    score = max(score, 0)
    score = min(score, 100)

    return round(score, 2)