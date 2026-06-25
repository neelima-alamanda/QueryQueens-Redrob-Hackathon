def extract_features(parsed_candidate):
    """
    Extract structured features from the parsed candidate.
    No scoring is done here.
    """

    profile = parsed_candidate["profile"]

    features = {}

    features["current_title"] = profile.get("current_title", "")

    features["years_of_experience"] = profile.get(
        "years_of_experience", 0
    )

    features["career_history"] = parsed_candidate["career_history"]

    features["skills"] = [
        skill.get("name", "")
        for skill in parsed_candidate["skills"]
    ]

    features["education"] = parsed_candidate["education"]

    features["certifications"] = parsed_candidate["certifications"]

    features["languages"] = parsed_candidate["languages"]

    features["redrob_signals"] = parsed_candidate["redrob_signals"]

    return features