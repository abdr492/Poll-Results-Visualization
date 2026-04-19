import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.express as px
import plotly.graph_objects as go

# 🔥 ADD HERE (ONLY ONCE)
premium_colors = ["#00FFD1", "#00BFFF", "#FF4B5C", "#FFD700", "#8A2BE2"]


def premium_chart(fig):
    fig.update_layout(
        plot_bgcolor="#0E1117",
        paper_bgcolor="#0E1117",
        font=dict(color="white"),
        title_font=dict(size=18, color="#00FFD1"),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        ),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Poll Insights Engine", layout="wide")

# ================================
# CUSTOM DARK THEME + CARDS
# ================================
st.markdown("""
<style>

/* ================= GLOBAL ================= */
body {
    background: linear-gradient(135deg, #0E1117, #111827);
    color: white;
}

.main {
    background-color: transparent;
}

/* ================= KPI CARDS ================= */
.card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
    text-align: center;
    transition: all 0.3s ease;
}

/* Hover effect */
.card:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 0 20px rgba(0,255,209,0.4);
}

/* KPI NUMBER */
.card h2 {
    font-size: 32px;
    font-weight: bold;
    background: linear-gradient(90deg, #00FFD1, #00BFFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* KPI LABEL */
.card p {
    color: #aaa;
    font-size: 14px;
}

/* ================= SIDEBAR ================= */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #0E1117);
}

/* Sidebar titles */
.sidebar-title {
    font-weight: bold;
    color: #00FFD1;
}

/* ================= MULTISELECT TAGS ================= */
span[data-baseweb="tag"] {
    background-color: #ff4b5c !important;
    color: white !important;
    border-radius: 8px !important;
    font-weight: bold;
}

/* ================= HEADINGS ================= */
h1, h2, h3 {
    color: #E5E7EB;
}

/* ================= SCROLLBAR ================= */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #00FFD1;
    border-radius: 10px;
}

/* ================= TABLE ================= */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.02);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================================
# LOAD DATA
# ================================
df = pd.read_csv("data/processed/cleaned_poll_data.csv")

# ================================
# SIDEBAR FILTERS
# ================================
st.sidebar.title("🔍 Insights Engine")

region = st.sidebar.multiselect("🌍 Region", df["Region"].unique(), default=df["Region"].unique())
age = st.sidebar.multiselect("🎂 Age Group", df["Age_Group"].unique(), default=df["Age_Group"].unique())

df = df[(df["Region"].isin(region)) & (df["Age_Group"].isin(age))]

# ================================
# HEADER
# ================================
st.title("🚀 Poll Insights Dashboard")

# ================================
# TABS (NO SCROLL UI)
# ================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🌍 Demographics",
    "💬 Feedback",
    "📄 Data"
])

# =========================================================
# 📊 TAB 1 — OVERVIEW
# =========================================================
with tab1:

    st.subheader("🏆 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4,gap="large")

    col1.markdown(f"""
    <div class='card'>
    <p>📊 Total Responses</p>
    <h2>{len(df)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class='card'>
    <p>⭐ Avg Satisfaction</p>
    <h2>{round(df['Satisfaction_Score'].mean(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class='card'>
    <p>💻 Top Tech</p>
    <h2>{df['Primary_Tech_Stack'].mode()[0]}</h2>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown(f"""
    <div class='card'>
    <p>🏠 Remote %</p>
    <h2>{round((df['Work_Setup_Preference']=='Remote').mean()*100,1)}%</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    colA, colB = st.columns(2)

    # BAR CHART
    with colA:
        st.subheader("📊 Tech vs Work Setup")
        fig = px.histogram(
        df,
        x="Primary_Tech_Stack",
        color="Work_Setup_Preference",
        barmode="group",
        color_discrete_sequence=premium_colors
        )

        fig.update_traces(
            marker_line_width=0,
            opacity=0.9
        )

        fig = premium_chart(fig)

        st.plotly_chart(fig, use_container_width=True)
        

    # GAUGE CHART
    with colB:
        st.subheader("⭐ Satisfaction Index")
        st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)

        avg = df["Satisfaction_Score"].mean()

        fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=avg,
        delta={'reference': 3},
        number={'font': {'color': "#00FFD1", 'size': 40}},
        title={'text': "Satisfaction Index", 'font': {'color': "white"}},
        gauge={
            'axis': {'range': [0, 5], 'tickcolor': "white"},
            'bar': {'color': "#00FFD1"},
            'bgcolor': "#1f1f2e",
            'steps': [
                {'range': [0, 2], 'color': "#FF4B5C"},
                {'range': [2, 4], 'color': "#FFD700"},
                {'range': [4, 5], 'color': "#00FF7F"}
            ]
            }
        ))

        fig_gauge.update_layout(
            paper_bgcolor="#0E1117",
            font=dict(color="white")
        )

        st.plotly_chart(fig_gauge, use_container_width=True)

# =========================================================
# 🌍 TAB 2 — DEMOGRAPHICS
# =========================================================
with tab2:

    st.subheader("🧬 Segment Analysis")

    col1, col2 = st.columns(2)

    # SUNBURST
    with col1:
        st.subheader("🌐 Audience Hierarchy")
        fig = px.sunburst(
        df,
        path=["Region", "Age_Group", "Work_Setup_Preference"],
        color_discrete_sequence=premium_colors
        )

        fig = premium_chart(fig)

        st.plotly_chart(fig, use_container_width=True)

    # VIOLIN
    with col2:
        st.subheader("🎻 Satisfaction by Occupation")
        fig = px.violin(
        df,
        x="Occupation",
        y="Satisfaction_Score",
        box=True,
        color="Occupation",
        color_discrete_sequence=premium_colors
        )

        fig = premium_chart(fig)

        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# 💬 TAB 3 — FEEDBACK
# =========================================================
with tab3:

    st.subheader("🧠 Feedback Intelligence")

    # SIMPLE SENTIMENT
    def sentiment(text):
        text = str(text).lower()
        if "great" in text or "excellent" in text:
            return "Positive"
        elif "poor" in text or "bad" in text:
            return "Negative"
        else:
            return "Neutral"

    df["Sentiment"] = df["Feedback"].apply(sentiment)

    col1, col2 = st.columns(2)

    # DONUT
    with col1:
        st.subheader("📊 Sentiment Distribution")
        fig = px.pie(
        df,
        names="Sentiment",
        hole=0.6,
        color_discrete_sequence=premium_colors
        )

        fig.update_traces(
            textinfo="percent+label",
            pull=[0.03]*len(df["Sentiment"].unique())
        )

        fig = premium_chart(fig)

        st.plotly_chart(fig, use_container_width=True)
    # LINE
    with col2:
        st.subheader("📈 Sentiment Trend")

        df["Date"] = pd.to_datetime(df["Date"])
        trend = df.groupby(["Date", "Sentiment"]).size().reset_index(name="Count")

        fig = px.line(
        trend,
        x="Date",
        y="Count",
        color="Sentiment",
        color_discrete_sequence=premium_colors
        )

        fig.update_traces(
            mode="lines+markers",
            line=dict(width=3),
            marker=dict(size=6)
        )

        fig = premium_chart(fig)

        st.plotly_chart(fig, use_container_width=True)

# ================================
# 📄 TAB 4 — DATA TABLE (UPGRADED)
# ================================
with tab4:

    st.subheader("📂 Filtered Dataset")

    # Create gradient styling
    styled_df = df.style.background_gradient(
        subset=["Satisfaction_Score"],   # column name
        cmap="magma"                   # color theme
    )

    st.dataframe(styled_df, use_container_width=True)