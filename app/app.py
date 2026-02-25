import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Config
# ----------------------------------
st.set_page_config(
    page_title="HEPro AI+ Dashboard",
    layout="wide",
    page_icon="🎓"
)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("HEPro AI+")
page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Student Analysis", "Feedback Monitoring", "System Info"]
)

# ----------------------------------
# Load Data
# ----------------------------------
@st.cache_data
def load_data():
    scores = pd.read_csv("data/processed/students_with_scores.csv")
    rec = pd.read_csv("outputs/student_mentor_recommendations.csv")
    feedback = pd.read_csv("feedback/mentor_feedback.csv")
    issues = pd.read_csv("feedback/matching_issues.csv")
    return scores, rec, feedback, issues

scores, rec, feedback, issues = load_data()
data = scores.merge(rec, on="student_id")

# ----------------------------------
# PAGE 1: OVERVIEW
# ----------------------------------
if page == "Overview":

    st.title("📊 HEPro AI+ Mentoring Intelligence")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", len(data))
    col2.metric("High Risk (SRI < 50)", (data["SRI"] < 50).sum())
    col3.metric("Mentors Assigned", data["Assigned_Mentor"].nunique())
    col4.metric("Matching Issues", len(issues))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig_cluster = px.pie(
            data,
            names="Cluster_Label",
            title="Cluster Distribution",
            hole=0.5
        )
        st.plotly_chart(fig_cluster, use_container_width=True)

    with col2:
        fig_sri = px.histogram(
            data,
            x="SRI",
            nbins=20,
            title="SRI Distribution"
        )
        st.plotly_chart(fig_sri, use_container_width=True)

# ----------------------------------
# PAGE 2: STUDENT ANALYSIS
# ----------------------------------
elif page == "Student Analysis":

    st.title("🔍 Student Insight Panel")

    student_id = st.selectbox("Select Student", data["student_id"].unique())
    student = data[data["student_id"] == student_id].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Scores")
        st.write({
            "APS": round(student["APS"], 2),
            "WWS": round(student["WWS"], 2),
            "PTMS": round(student["PTMS"], 2),
            "CRS": round(student["CRS"], 2),
            "SRI": round(student["SRI"], 2)
        })

    with col2:
        st.subheader("System Decision")
        st.write({
            "Cluster": student["Cluster_Label"],
            "Assigned Mentor": student["Assigned_Mentor"],
            "Matching Score": student["Matching_Score"],
            "Intervention": student["Recommended_Intervention"],
            "Alert": student["Alert_Status"]
        })

# ----------------------------------
# PAGE 3: FEEDBACK
# ----------------------------------
elif page == "Feedback Monitoring":

    st.title("🔁 Feedback & Learning")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.histogram(
            feedback,
            x="sri_improvement",
            nbins=20,
            title="SRI Improvement"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.pie(
            feedback,
            names="mentor_rating",
            title="Mentor Ratings",
            hole=0.5
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("⚠ Matching Issues")
    st.dataframe(issues, use_container_width=True)

# ----------------------------------
# PAGE 4: SYSTEM INFO
# ----------------------------------
elif page == "System Info":

    st.title("ℹ System Architecture")

    st.markdown("""
    **HEPro AI+ Features**
    - Rule-Based Student Scoring (APS, WWS, PTMS, CRS)
    - Student Readiness Index (SRI)
    - K-Means Clustering
    - Cosine Similarity Mentor Matching
    - Style Compatibility & Availability Weighting
    - Capacity Constraints
    - Intervention Recommendation Engine
    - Feedback-Based Continuous Learning
    """)