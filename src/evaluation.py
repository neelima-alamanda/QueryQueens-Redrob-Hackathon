import time


def validate_submission(results):
    ids = set()

    for candidate in results:
        if candidate["candidate_id"] in ids:
            return False
        ids.add(candidate["candidate_id"])

    return True


def runtime_test(start_time):
    end_time = time.time()
    print(f"Runtime: {end_time - start_time:.2f} seconds")


def rank_top100(results):
    return sorted(results, key=lambda x: x["score"], reverse=True)[:100]


def calculate_statistics(results):
    scores = [candidate["score"] for candidate in results]

    return {
        "total_candidates": len(results),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "average_score": sum(scores) / len(scores)
    }