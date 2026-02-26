🎓 Dedicated Mentoring System for Students (HEPro AI+)
AI-Driven Student Intelligence for Early Risk Detection & Personalized Mentor Allocation
📌 Project Overview

Educational institutions often struggle to identify students who need support at the right time. Traditional mentoring systems rely on manual monitoring and do not consider multiple behavioral factors.

This project builds an AI-powered mentoring intelligence system that:

Evaluates students across academic, wellbeing, productivity, and career dimensions

Calculates a Student Readiness Index (SRI)

Segments students using K-Means clustering

Assigns mentors using cosine similarity

Provides intervention recommendations

Tracks feedback and improvement

Offers a live Streamlit dashboard

🔗 Live App
https://dedicatedmentoringsystemforstudents-ai-ml-project-hhw9jxeyqlfs.streamlit.app/

🧠 Key Features

Multi-dimensional student evaluation

Rule-based scoring system (APS, WWS, PTMS, CRS)

Student Readiness Index (SRI)

Behavioral segmentation using Machine Learning

Cosine similarity-based mentor matching

Intervention recommendation engine

Feedback monitoring & matching issue detection

Interactive Streamlit dashboard

📂 Project Structure
Dedicated Mentoring System for Students
│
├── app/
│   └── app.py                      # Streamlit dashboard application
│
├── data/
│   ├── raw/
│   │   ├── students.csv            # Raw student dataset
│   │   └── mentors.csv             # Mentor information dataset
│   │
│   └── processed/
│       ├── students_with_scores.csv
│       └── students_with_clusters.csv
│
├── notebooks/
│   ├── Student_dataset_generation.ipynb
│   ├── Patterns_identification.ipynb
│   ├── Student_Scoring_System_(Rule_Based_Intelligence).ipynb
│   └── Mentor_Student_matching_logic.ipynb
│
├── outputs/
│   └── student_mentor_recommendations.csv
│
├── feedback/
│   ├── mentor_feedback.csv
│   └── matching_issues.csv
│
├── src/
│   └── feedback_loop.py            # Continuous learning logic
│
├── docs/
│   ├── HEPro AIML Internship Project Report.pdf
│   ├── Data Dictionary.pdf
│   ├── Scoring Logic and Thresholds.pdf
│   ├── Cluster interpretation document.pdf
│   ├── How_the_Dataset_Reflects_Real_Student_behavior.pdf
│   ├── Mentor_Matching & Intervention Recommendation System.pdf
│   └── Recommendation for each cluster type.pdf
│
├── requirements.txt
└── README.md
🔄 End-to-End Workflow

Generate student dataset

Identify behavioral patterns

Calculate performance scores

Compute Student Readiness Index (SRI)

Segment students using K-Means

Match mentors using cosine similarity

Recommend interventions

Track feedback and improvement

Visualize everything in Streamlit

📊 Dataset Description
Student Data

Includes:

GPA, attendance, assignments

Stress level, sleep hours, mental wellbeing

Productivity, distractions

Career clarity, skill readiness

Engagement score

Mentor Data

Includes:

Expertise domain (Academic / Wellness / Career)

Mentoring style

Availability

Capacity

Synthetic data is generated to simulate realistic student behavior patterns.

📓 Notebooks Explanation
1. Student_dataset_generation.ipynb

Purpose

Generate synthetic dataset of 50 students

Why used

Real student data is sensitive

Allows realistic simulation for ML development

What it does

Creates academic, wellbeing, productivity, and career attributes

Saves students.csv

2. Patterns_identification.ipynb

Purpose

Identify important behavioral patterns

Why used

Understand relationships before modeling

Patterns identified

High stress + low productivity

Low GPA + high engagement

Strong academics but low career clarity

This supports feature design and cluster interpretation.

3. Student_Scoring_System_(Rule_Based_Intelligence).ipynb

Purpose

Convert raw data into meaningful performance scores

Scores calculated

Score	Meaning
APS	Academic Performance
WWS	Wellness & Wellbeing
PTMS	Productivity
CRS	Career Readiness

Final Metric

SRI = 0.30*APS + 0.25*WWS + 0.20*PTMS + 0.25*CRS

Also classifies students into:

Green

Blue

Yellow

Red

Output: students_with_scores.csv

4. Mentor_Student_matching_logic.ipynb

Purpose

Segment students

Assign mentors

Steps

StandardScaler applied

K-Means (K=3) clustering

Cluster labels:

At-Risk Students

High Performers

Career-Confused

Cosine Similarity Matching

Student vector:

[APS, WWS, PTMS, CRS]

Mentor vectors based on domain expertise.

Final Score

Similarity + Style Bonus + Availability Weight

Output:
student_mentor_recommendations.csv

🔁 Feedback System
feedback_loop.py

Purpose

Simulate post-mentoring improvement

What it does

Calculates SRI improvement

Records mentor ratings

Flags issues when:

Low improvement

Low rating

Poor match

Outputs:

mentor_feedback.csv

matching_issues.csv

This enables continuous system learning.

📄 Documentation (docs folder)
Document	Purpose
Project Report	Complete system explanation
Data Dictionary	Field definitions
Scoring Logic	Weight calculations and thresholds
Cluster Interpretation	Meaning of each cluster
Dataset Behavior	Why data reflects real students
Mentor Matching System	Matching workflow
Cluster Recommendations	Intervention strategy per cluster

These documents support transparency and explainability.

🌐 Streamlit Dashboard

app.py

Modules:

Overview

Total students

Risk distribution

Cluster distribution

SRI histogram

Student Analysis

Individual scores

Cluster

Assigned mentor

Intervention

Risk status

Feedback Monitoring

SRI improvement

Mentor ratings

Matching issues

System Info

End-to-end architecture

⚙️ Technologies Used

Python

Pandas, NumPy

Scikit-learn

Plotly

Streamlit

🚀 How to Run Locally
1. Clone Repository
git clone <your-repo-link>
cd Dedicated-Mentoring-System
2. Install Requirements
pip install -r requirements.txt
3. Run Dashboard
streamlit run app/app.py
📈 Machine Learning Summary
Component	Method
Scaling	StandardScaler
Clustering	K-Means (K=3)
Matching	Cosine Similarity
Decision	Rule-based
Learning	Feedback loop
⚠️ Limitations

Synthetic dataset

Simulated feedback

Fixed cluster count

No real-time LMS integration

👩‍💻 Author

Ummu Abeeba.S

Project Status: Completed
Deployment: Live on Streamlit
