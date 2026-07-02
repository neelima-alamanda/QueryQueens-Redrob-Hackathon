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
    return sorted(
        results,
        key=lambda x: (-x["score"], x["candidate_id"])
    )[:100]


def calculate_statistics(results):
    scores = [candidate["score"] for candidate in results]

    return {
        "total_candidates": len(results),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "average_score": sum(scores) / len(scores)
    }
import csv

def generate_submission(results, output_file="QueryQueens.csv"):

    top100 = rank_top100(results)

    if not validate_submission(top100):
        raise ValueError("Duplicate candidate IDs found in submission.")

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Header required by the validator
        writer.writerow([
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ])

        for rank, candidate in enumerate(top100, start=1):

            writer.writerow([
                candidate["candidate_id"],
                rank,
                candidate["score"],
                candidate.get("reason", "")
            ])

    print(f"Submission saved to {output_file}")