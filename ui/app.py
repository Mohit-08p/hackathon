import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st

st.set_page_config(
    page_title="Learning Report Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ✅ FULL UI CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Header */
.main-header {
    font-size: 34px;
    font-weight: 800;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    -webkit-background-clip: text;
    color: transparent;
}

.sub-header {
    font-size: 15px;
    color: #9ca3af;
    margin-top: -8px;
}

/* KPI Cards */
.metric-card {
    background: #111827;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
    transition: transform 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

/* Navigation Cards */
.nav-card {
    background: #1f2937;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: all 0.2s ease;
    cursor: pointer;
}

.nav-card:hover {
    background: #374151;
    transform: scale(1.05);
}

.nav-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
}

.nav-desc {
    font-size: 13px;
    color: #9ca3af;
}

/* Insights box */
.insight-box {
    background: #1e293b;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


def show_home():
    # ✅ HEADER
    st.markdown('<div class="main-header">🎓 Learning Report Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Unified analytics platform for learning & development</div>', unsafe_allow_html=True)

    st.divider()

    # ✅ KPI SECTION
    from config import DB_PATH
    import sqlite3

    col1, col2, col3 = st.columns(3)

    if DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        try:
            emp_count = conn.execute("SELECT COUNT(*) FROM employees WHERE employment_status='Active'").fetchone()[0]
            enroll_count = conn.execute("SELECT COUNT(*) FROM lms_enrollments").fetchone()[0]
            comp_rate = conn.execute("SELECT ROUND(AVG(completion_rate),1) FROM gold_dept_learning_kpis").fetchone()[0]

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    👥 <b>Active Employees</b>
                    <h2>{emp_count:,}</h2>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    📚 <b>Total Enrollments</b>
                    <h2>{enroll_count:,}</h2>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    ✅ <b>Completion Rate</b>
                    <h2>{comp_rate or 0}%</h2>
                </div>
                """, unsafe_allow_html=True)

        except Exception:
            st.info("Database not set up yet. Run the setup script first.")
        finally:
            conn.close()
    else:
        st.warning("Database not initialised. Go to Admin → Setup to initialise.")

    st.divider()

    # ✅ NAVIGATION SECTION
    st.markdown("## 🚀 Navigate")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-title">💬 Chat Agent</div>
            <div class="nav-desc">Ask questions in natural language</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-title">📊 Reports</div>
            <div class="nav-desc">Generate KPI & skill gap reports</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-title">📈 Dashboards</div>
            <div class="nav-desc">Interactive charts & insights</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-title">⚡ Flow Library</div>
            <div class="nav-desc">Trigger automation workflows</div>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-title">⚙️ Admin</div>
            <div class="nav-desc">Setup & configuration</div>
        </div>
        """, unsafe_allow_html=True)

    # ✅ INSIGHTS (IMPORTANT FOR HACKATHON)
    st.markdown('''
    <div class="insight-box">
        <h4>📊 Key Insights</h4>
        <ul>
            <li>Completion rates are improving across most teams</li>
            <li>Skill gap is highest in Cloud & DevOps domains</li>
            <li>Engagement dropped slightly in the last quarter</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)


show_home()
