import pandas as pd
import numpy as np
import os

def generate_feedback():
    print("Generating feedback data...")

    os.makedirs("feedback", exist_ok=True)

    df = pd.read_csv("outputs/student_mentor_recommendations.csv")

    np.random.seed(42)
    records = []

    for _, row in df.iterrows():
        student_id = row["student_id"]
        mentor = row["Assigned_Mentor"]
        sri_before = row["SRI"]
        cluster = row["Cluster_Label"]
        matching_score = row["Matching_Score"]

        # Improvement logic based on cluster
        if cluster == "At-Risk Students":
            improvement = np.random.randint(3, 12)
            sessions = np.random.randint(4, 8)
        elif cluster == "Career-Confused Students":
            improvement = np.random.randint(2, 8)
            sessions = np.random.randint(3, 6)
        else:
            improvement = np.random.randint(1, 5)
            sessions = np.random.randint(2, 4)

        sri_after = min(sri_before + improvement, 100)

        # Rating based on improvement + matching quality
        if improvement >= 8 and matching_score > 0.7:
            rating = 5
        elif improvement >= 5:
            rating = 4
        elif improvement >= 3:
            rating = 3
        else:
            rating = 2

        records.append({
            "student_id": student_id,
            "mentor_name": mentor,
            "cluster": cluster,
            "matching_score": round(matching_score, 3),
            "initial_sri": sri_before,
            "final_sri": sri_after,
            "sri_improvement": sri_after - sri_before,
            "mentor_rating": rating,
            "sessions_completed": sessions
        })

    feedback_df = pd.DataFrame(records)
    feedback_df.to_csv("feedback/mentor_feedback.csv", index=False)

    print("Feedback file created: feedback/mentor_feedback.csv")


def analyze_feedback():
    print("Analyzing feedback...")

    df = pd.read_csv("feedback/mentor_feedback.csv")

    issues = []

    for _, row in df.iterrows():
        if (
            row["sri_improvement"] < 3 or
            row["mentor_rating"] <= 2 or
            row["matching_score"] < 0.5
        ):
            issues.append({
                "student_id": row["student_id"],
                "mentor_name": row["mentor_name"],
                "cluster": row["cluster"],
                "matching_score": row["matching_score"],
                "sri_improvement": row["sri_improvement"],
                "mentor_rating": row["mentor_rating"],
                "issue": "Low effectiveness – review matching weights"
            })

    issues_df = pd.DataFrame(issues)
    issues_df.to_csv("feedback/matching_issues.csv", index=False)

    print("Issue file created: feedback/matching_issues.csv")


if __name__ == "__main__":
    generate_feedback()
    analyze_feedback()