import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Config
# ----------------------------------
st.set_page_config(
    page_title="AI+ Mentoring Intelligence",
    layout="wide"
)

# ----------------------------------
# Professional SaaS Styling
# ----------------------------------
st.markdown("""
<style>

/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #e4ecf7);
}

/* Glass Header */
.glass-header {
    background: rgba(255,255,255,0.65);
    backdrop-filter: blur(12px);
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.4);
}

/* KPI Cards */
.kpi-card {
    background: #ffffff;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.06);
    text-align: center;
}

.kpi-title {
    font-size: 14px;
    color: #666;
}

.kpi-value {
    font-size: 28px;
    font-weight: 600;
    color: #000;
}

/* Content Box */
.content-box {
    background: #ffffff;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.section-title {
    font-size: 26px;
    font-weight: 600;
    color: #000;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("AI+ MI")
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

data = scores.merge(rec, on="student_id", how="left")

# Fix SRI after merge
if "SRI_x" in data.columns:
    data["SRI"] = data["SRI_x"]
    data.drop(columns=["SRI_x"], inplace=True)

if "SRI_y" in data.columns:
    data.drop(columns=["SRI_y"], inplace=True)

# Safety
if "SRI" not in data.columns:
    st.error("SRI column missing")
    st.stop()

# ----------------------------------
# PAGE 1: OVERVIEW
# ----------------------------------
if page == "Overview":

    st.markdown("""
    <div class="glass-header">
        <div class="section-title">HEPro AI+ Mentoring Intelligence Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    # KPI Values
    total_students = len(data)
    high_risk = (data["SRI"] < 50).sum()
    mentors = data["Assigned_Mentor"].nunique()
    issue_count = len(issues)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Total Students</div>
            <div class="kpi-value">{total_students}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">High Risk Students</div>
            <div class="kpi-value">{high_risk}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Mentors Assigned</div>
            <div class="kpi-value">{mentors}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Matching Issues</div>
            <div class="kpi-value">{issue_count}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig_cluster = px.pie(data, names="Cluster_Label", hole=0.5, title="Cluster Distribution")
        st.plotly_chart(fig_cluster, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig_sri = px.histogram(data, x="SRI", nbins=20, title="SRI Distribution")
        st.plotly_chart(fig_sri, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------
# PAGE 2: STUDENT ANALYSIS
# ----------------------------------
elif page == "Student Analysis":

    st.markdown("""
    <div class="glass-header">
        <div class="section-title">Student Insight Panel</div>
    </div>
    """, unsafe_allow_html=True)

    student_id = st.selectbox("Select Student", data["student_id"].unique())
    student = data[data["student_id"] == student_id].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("Scores")
        st.write({
            "APS": round(student["APS"], 2),
            "WWS": round(student["WWS"], 2),
            "PTMS": round(student["PTMS"], 2),
            "CRS": round(student["CRS"], 2),
            "SRI": round(student["SRI"], 2)
        })
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("System Decision")
        st.write({
            "Cluster": student["Cluster_Label"],
            "Assigned Mentor": student["Assigned_Mentor"],
            "Matching Score": student["Matching_Score"],
            "Intervention": student["Recommended_Intervention"],
            "Alert Status": student["Alert_Status"]
        })
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------
# PAGE 3: FEEDBACK
# ----------------------------------
elif page == "Feedback Monitoring":

    st.markdown("""
    <div class="glass-header">
        <div class="section-title">Feedback & Continuous Learning</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig1 = px.histogram(feedback, x="sri_improvement", nbins=20, title="SRI Improvement")
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig2 = px.pie(feedback, names="mentor_rating", hole=0.5, title="Mentor Ratings")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Matching Issues")
    st.dataframe(issues, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------
# PAGE 4: SYSTEM INFO
# ----------------------------------
elif page == "System Info":

    st.markdown("""
    <div class="glass-header">
        <div class="section-title">System Architecture</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="content-box">

    **Core Components**

    • Student Performance Scoring (APS, WWS, PTMS, CRS)  
    • Student Readiness Index (SRI)  
    • K-Means Behavioral Segmentation  
    • Cosine Similarity Mentor Matching  
    • Style Compatibility & Availability Weighting  
    • Capacity-Based Assignment  
    • Intervention Recommendation Engine  
    • Feedback-Based Continuous Learning  

    </div>
    """, unsafe_allow_html=True)
