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

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #dce8f5 0%, #eef3fa 50%, #d8e8f7 100%);
}

.block-container {
    padding-top: 2rem;
}

/* Glass Header */
.glass-header {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius: 16px;
    padding: 22px 28px;
    margin-bottom: 24px;
    box-shadow: 0 4px 24px rgba(60,100,180,0.08), 0 1px 0 rgba(255,255,255,0.8) inset;
    border: 1px solid rgba(255,255,255,0.6);
}

.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 24px;
    font-weight: 400;
    color: #111827;
    margin: 0;
    letter-spacing: -0.3px;
}

/* KPI Cards */
.kpi-card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 20px 18px;
    border-radius: 14px;
    box-shadow: 0 2px 14px rgba(60,100,180,0.07);
    border: 1px solid rgba(255,255,255,0.7);
    text-align: center;
}

.kpi-label {
    font-size: 12px;
    font-weight: 500;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
}

.kpi-value {
    font-family: 'DM Serif Display', serif;
    font-size: 34px;
    color: #111827;
    line-height: 1;
}

/* Content Box */
.content-box {
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 14px;
    padding: 20px 22px;
    box-shadow: 0 2px 14px rgba(60,100,180,0.07);
    border: 1px solid rgba(255,255,255,0.65);
    margin-bottom: 16px;
}

/* Student Info Panels */
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 16px;
}

.info-panel {
    background: rgba(255,255,255,0.80);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 14px;
    padding: 22px 24px;
    box-shadow: 0 2px 14px rgba(60,100,180,0.07);
    border: 1px solid rgba(255,255,255,0.65);
}

.info-panel-title {
    font-size: 12px;
    font-weight: 600;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.9px;
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(0,0,0,0.06);
}

.score-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 9px 0;
    border-bottom: 1px solid rgba(0,0,0,0.04);
}

.score-row:last-child {
    border-bottom: none;
}

.score-key {
    font-size: 14px;
    color: #374151;
    font-weight: 500;
}

.score-val {
    font-size: 14px;
    font-weight: 600;
    color: #111827;
    background: rgba(59,130,246,0.07);
    padding: 3px 10px;
    border-radius: 6px;
}

.score-val.highlight {
    background: rgba(239,68,68,0.08);
    color: #b91c1c;
}

.badge {
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
    background: rgba(59,130,246,0.1);
    color: #1d4ed8;
}

.badge.alert {
    background: rgba(239,68,68,0.1);
    color: #b91c1c;
}

.badge.ok {
    background: rgba(34,197,94,0.1);
    color: #166534;
}

/* System Architecture */
.arch-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 4px;
}

.arch-card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 14px;
    padding: 20px 22px;
    box-shadow: 0 2px 12px rgba(60,100,180,0.07);
    border: 1px solid rgba(255,255,255,0.65);
}

.arch-card-title {
    font-size: 12px;
    font-weight: 600;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.9px;
    margin-bottom: 14px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(0,0,0,0.06);
}

.arch-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 7px 0;
    border-bottom: 1px solid rgba(0,0,0,0.04);
    font-size: 14px;
    color: #374151;
}

.arch-item:last-child {
    border-bottom: none;
}

.arch-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #3b82f6;
    margin-top: 5px;
    flex-shrink: 0;
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

if "SRI_x" in data.columns:
    data["SRI"] = data["SRI_x"]
    data.drop(columns=["SRI_x"], inplace=True)
if "SRI_y" in data.columns:
    data.drop(columns=["SRI_y"], inplace=True)
if "SRI" not in data.columns:
    st.error("SRI column missing")
    st.stop()

# ----------------------------------
# PAGE 1: OVERVIEW
# ----------------------------------
if page == "Overview":

    st.markdown("""
    <div class="glass-header">
        <p class="section-title">HEPro AI+ Mentoring Intelligence Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    total_students = len(data)
    high_risk = int((data["SRI"] < 50).sum())
    mentors = int(data["Assigned_Mentor"].nunique())
    issue_count = len(issues)

    col1, col2, col3, col4 = st.columns(4)

    def kpi(col, label, value):
        col.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    kpi(col1, "Total Students", total_students)
    kpi(col2, "High Risk Students", high_risk)
    kpi(col3, "Mentors Assigned", mentors)
    kpi(col4, "Matching Issues", issue_count)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig_cluster = px.pie(data, names="Cluster_Label", hole=0.5, title="Cluster Distribution")
        fig_cluster.update_layout(margin=dict(t=40, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_cluster, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig_sri = px.histogram(data, x="SRI", nbins=20, title="SRI Distribution")
        fig_sri.update_layout(margin=dict(t=40, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_sri, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------
# PAGE 2: STUDENT ANALYSIS
# ----------------------------------
elif page == "Student Analysis":

    st.markdown("""
    <div class="glass-header">
        <p class="section-title">Student Insight Panel</p>
    </div>
    """, unsafe_allow_html=True)

    student_id = st.selectbox("Select Student", data["student_id"].unique())
    student = data[data["student_id"] == student_id].iloc[0]

    sri_val = round(student["SRI"], 2)
    alert = student["Alert_Status"]
    alert_badge_class = "alert" if str(alert).lower() not in ["none", "ok", "normal", ""] else "ok"

    scores_html = "".join([
        f'<div class="score-row"><span class="score-key">{k}</span>'
        f'<span class="score-val {"highlight" if k == "SRI" and sri_val < 50 else ""}">{round(student[k], 2)}</span></div>'
        for k in ["APS", "WWS", "PTMS", "CRS", "SRI"]
    ])

    decision_rows = [
        ("Cluster", student["Cluster_Label"], "badge"),
        ("Assigned Mentor", student["Assigned_Mentor"], "score-val"),
        ("Matching Score", round(student["Matching_Score"], 2), "score-val"),
        ("Intervention", student["Recommended_Intervention"], "score-val"),
        ("Alert Status", alert, f"badge {alert_badge_class}"),
    ]

    decision_html = "".join(
        f'<div class="score-row"><span class="score-key">{key}</span>'
        f'<span class="{cls}">{val}</span></div>'
        for key, val, cls in decision_rows
    )

    st.markdown(f"""
    <div class="info-grid">
        <div class="info-panel">
            <div class="info-panel-title">Performance Scores</div>
            {scores_html}
        </div>
        <div class="info-panel">
            <div class="info-panel-title">System Decision</div>
            {decision_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------
# PAGE 3: FEEDBACK
# ----------------------------------
elif page == "Feedback Monitoring":

    st.markdown("""
    <div class="glass-header">
        <p class="section-title">Feedback & Continuous Learning</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig1 = px.histogram(feedback, x="sri_improvement", nbins=20, title="SRI Improvement")
        fig1.update_layout(margin=dict(t=40, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        fig2 = px.pie(feedback, names="mentor_rating", hole=0.5, title="Mentor Ratings")
        fig2.update_layout(margin=dict(t=40, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
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
        <p class="section-title">System Architecture</p>
    </div>
    """, unsafe_allow_html=True)

    def arch_card(title, items):
        rows = "".join(
            f'<div class="arch-item"><div class="arch-dot"></div>{item}</div>'
            for item in items
        )
        return f'<div class="arch-card"><div class="arch-card-title">{title}</div>{rows}</div>'

    scoring_items = [
        "Academic Performance Score (APS)",
        "Wellbeing &amp; Welfare Score (WWS)",
        "Peer &amp; Tutor Match Score (PTMS)",
        "Course Readiness Score (CRS)",
        "Student Readiness Index (SRI)",
    ]
    segmentation_items = [
        "K-Means Behavioural Segmentation",
        "Cluster Label Assignment",
        "Dynamic Re-clustering on Feedback",
    ]
    matching_items = [
        "Cosine Similarity Mentor Matching",
        "Style Compatibility Weighting",
        "Mentor Availability Scoring",
        "Capacity-Based Assignment Logic",
    ]
    learning_items = [
        "Intervention Recommendation Engine",
        "Alert Status Classification",
        "Feedback-Based Continuous Learning",
        "Matching Issue Tracking &amp; Review",
    ]

    st.markdown(f"""
    <div class="arch-grid">
        {arch_card("Scoring Engine", scoring_items)}
        {arch_card("Segmentation", segmentation_items)}
        {arch_card("Mentor Matching", matching_items)}
        {arch_card("Intelligence &amp; Learning", learning_items)}
    </div>
    """, unsafe_allow_html=True)
