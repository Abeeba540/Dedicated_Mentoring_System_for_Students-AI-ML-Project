# 🎓 Dedicated Mentoring System for Students (HEPro AI+)

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)
![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Project](https://img.shields.io/badge/Type-End--to--End%20ML-blue)

## 🎯 Overview

**HEPro AI+** is an end-to-end AI system designed to identify student risks early and enable **personalized mentoring decisions** using data.

Traditional mentoring systems focus only on academic performance and are reactive. This project builds a **data-driven mentoring intelligence platform** that:

* Evaluates students across **academic, wellbeing, productivity, and career dimensions**
* Calculates a unified **Student Readiness Index (SRI)**
* Segments students using **K-Means clustering**
* Matches mentors using **cosine similarity**
* Generates **intervention recommendations**
* Tracks **post-mentoring improvement**
* Provides a **live interactive dashboard**

🌐 **Live Application**
[https://dedicatedmentoringsystemforstudents-ai-ml-project-hhw9jxeyqlfs.streamlit.app/](https://dedicatedmentoringsystemforstudents-ai-ml-project-hhw9jxeyqlfs.streamlit.app/)

---

## 🚀 Key Capabilities

* Multi-dimensional student evaluation
* Rule-based scoring system (APS, WWS, PTMS, CRS)
* Student Readiness Index (SRI)
* Risk classification (Green / Blue / Yellow / Red)
* Student segmentation using Machine Learning
* Cosine similarity-based mentor matching
* Capacity-aware mentor allocation
* Feedback loop for performance improvement
* Matching issue detection
* Streamlit decision-support dashboard

---

## 📊 System Performance

| Metric               | Value     |
| -------------------- | --------- |
| Students Analyzed    | 50        |
| Clusters             | 3         |
| At-Risk Students     | 19        |
| High Performers      | 16        |
| Career-Confused      | 15        |
| Matching Score Range | 0.9 – 1.2 |
| Deployment           | ✅ Live    |

---

## 🏗️ Project Structure

```
Dedicated_Mentoring_System/
│
├── app/
│   └── app.py                          # Streamlit dashboard
│
├── data/
│   ├── raw/
│   │   ├── students.csv                # Generated student dataset
│   │   └── mentors.csv                 # Mentor information
│   │
│   └── processed/
│       ├── students_with_scores.csv    # APS, WWS, PTMS, CRS, SRI
│       └── students_with_clusters.csv  # Cluster labels
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
│   └── feedback_loop.py
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
```

---

## 🔄 End-to-End Workflow

```
Student Data
    ↓
Feature Engineering
    ↓
Rule-Based Scoring (APS, WWS, PTMS, CRS)
    ↓
Student Readiness Index (SRI)
    ↓
K-Means Clustering (K = 3)
    ↓
Cosine Similarity Mentor Matching
    ↓
Intervention Recommendation
    ↓
Feedback Loop & Issue Detection
    ↓
Streamlit Dashboard
```

---

## 🧮 Scoring Framework

### Composite Scores

| Score | Description                    |
| ----- | ------------------------------ |
| APS   | Academic Performance           |
| WWS   | Wellness & Wellbeing           |
| PTMS  | Productivity & Time Management |
| CRS   | Career Readiness               |

### Student Readiness Index

```
SRI = 0.30*APS + 0.25*WWS + 0.20*PTMS + 0.25*CRS
```

### Risk Levels

| SRI   | Category                |
| ----- | ----------------------- |
| ≥ 75  | Green (High Performing) |
| 60–74 | Blue (Stable)           |
| 45–59 | Yellow (Needs Support)  |
| < 45  | Red (High Risk)         |

---

## 🤖 Machine Learning

### Student Segmentation

* Algorithm: **K-Means**
* K = 3
* Features: APS, WWS, PTMS, CRS, SRI
* Scaling: StandardScaler
<img width="436" height="256" alt="image" src="https://github.com/user-attachments/assets/9de6bc46-584c-4ab0-b2ac-f73f8ad9afd8" />

**Cluster Interpretation**

| Cluster         | Meaning                                 |
| --------------- | --------------------------------------- |
| At-Risk         | Low productivity / moderate wellbeing   |
| High Performers | Strong across all dimensions            |
| Career-Confused | Good academics but low career readiness |
<img width="442" height="256" alt="image" src="https://github.com/user-attachments/assets/b78d8ec9-f482-4d9d-a1c3-07c9a97090bf" />

---

## 🎯 Mentor Matching

### Method: Cosine Similarity

Student vector:

```
[APS, WWS, PTMS, CRS]
```

Mentor vectors represent expertise domains:

* Academic
* Wellness
* Career

### Final Matching Score

```
Cosine Similarity
+ Style Compatibility Bonus
+ Availability Weight
```

Constraints:

* Capacity control
* Load balancing

Output: `student_mentor_recommendations.csv`

---

## 🔁 Feedback System

**src/feedback_loop.py**

Purpose:

* Simulate post-mentoring improvement
* Calculate SRI change
* Record mentor ratings
* Detect poor matches

Flags cases where:

* SRI improvement < 3
* Mentor rating ≤ 2
* Matching score is low

Outputs:

* mentor_feedback.csv
* matching_issues.csv


---

## 📓 Notebooks (What & Why)

### Student_dataset_generation.ipynb

Generates synthetic student data to simulate real educational behavior. Used because real student data is sensitive.

### Patterns_identification.ipynb

Explores behavioral relationships such as stress vs productivity and academic vs career trends. Helps in feature understanding.

### Student_Scoring_System_(Rule_Based_Intelligence).ipynb

Implements rule-based formulas to calculate APS, WWS, PTMS, CRS and SRI. Produces processed scoring dataset.

### Mentor_Student_matching_logic.ipynb

Performs clustering, assigns cluster labels, and implements cosine similarity mentor matching.

---

## 📄 Documentation (docs folder)

| Document                | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| Project Report          | Complete system design and results       |
| Data Dictionary         | Field definitions                        |
| Scoring Logic           | Feature weights and thresholds           |
| Cluster Interpretation  | Behavioral meaning of clusters           |
| Dataset Behavior        | Justification for synthetic data realism |
| Matching System         | End-to-end matching workflow             |
| Cluster Recommendations | Intervention strategy per segment        |

These ensure **full explainability and auditability**.

---

## 🌐 Streamlit Dashboard

Modules:

**Overview**

* Total students
* Risk distribution
* Cluster distribution
* SRI histogram

**Student Analysis**

* Individual scores
* Cluster label
* Assigned mentor
* Matching score
* Intervention

**Feedback Monitoring**

* SRI improvement
* Mentor ratings
* Matching issues
<img width="2400" height="3800" alt="kxw4du99q6dto14" src="https://github.com/user-attachments/assets/6c01d12f-2d77-400f-b7fc-9b377aa63d83" />
---

## ⚙️ Technologies

| Category      | Tools         |
| ------------- | ------------- |
| Language      | Python        |
| Data          | Pandas, NumPy |
| ML            | Scikit-learn  |
| Visualization | Plotly        |
| Dashboard     | Streamlit     |

---

## 🚀 Quick Start

### 1. Clone Repository

```
git clone <your-repo-link>
cd Dedicated_Mentoring_System
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Application

```
streamlit run app/app.py
```

---

## ⚠️ Assumptions & Limitations

* Synthetic dataset
* Simulated feedback
* Fixed cluster size (K = 3)
* No real-time LMS integration

---

## 👩‍💻 Author

**Ummu Abeeba.S**


GitHub: [https://github.com/Abeeba540](https://github.com/Abeeba540)

---

## 📚 References

* Hands-On Machine Learning – Aurélien Géron
* Pattern Recognition and Machine Learning – Christopher Bishop
* Recommender Systems – Charu Aggarwal
* Educational Data Mining – Baker & Inventado
* HEPro AI Internship Materials

---

## 🏁 Project Status

| Phase                    | Status     |
| ------------------------ | ---------- |
| Dataset & Feature Design | ✅ Complete |
| Rule-Based Scoring       | ✅ Complete |
| Machine Learning         | ✅ Complete |
| Mentor Matching          | ✅ Complete |
| Feedback System          | ✅ Complete |
| Dashboard                | ✅ Live     |

**Overall Status:** ✅ End-to-End System Completed

