import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    layout="wide",
    page_icon="📊"
)

# ---------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }

    h1 {
        font-size: 60px !important;
        font-weight: 800 !important;
        color: #1f2937 !important;
    }

    h2 {
        font-size: 38px !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
    }

    h3 {
        font-size: 28px !important;
        font-weight: 600 !important;
        color: #374151 !important;
    }

    .stPlotlyChart {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("Warrap State Integrated Dashboard")

st.markdown("---")

# ---------------------------------------------------
# DATA
# ---------------------------------------------------

counties = [
    "Tonj North",
    "Tonj East",
    "Tonj South",
    "Gogrial West",
    "Gogrial East",
    "Twic"
]

hospital_data = {
    "County": counties,
    "Hospitals": [5, 4, 6, 5, 4, 6]
}

school_data = {
    "County": counties,
    "Schools": [5.5, 5.5, 5.5, 5.5, 5.5, 5.5]
}

hospital_df = pd.DataFrame(hospital_data)
school_df = pd.DataFrame(school_data)

# ---------------------------------------------------
# HOSPITAL DISTRIBUTION
# ---------------------------------------------------
st.header("Hospital Distribution")

st.subheader("Hospitals Across Counties")

hospital_colors = [
    "#0B66C3",
    "#76B0DE",
    "#FF232E",
    "#E8A0A1",
    "#33AD9B",
    "#73D991"
]

fig_pie = px.pie(
    hospital_df,
    names="County",
    values="Hospitals",
    color="County",
    color_discrete_sequence=hospital_colors
)

fig_pie.update_traces(
    textinfo='percent',
    textfont_size=18
)

fig_pie.update_layout(
    height=700,
    paper_bgcolor="#f5f5f5",
    plot_bgcolor="#f5f5f5",
    font=dict(size=18),
    legend=dict(
        font=dict(size=18)
    )
)

st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# SCHOOL DISTRIBUTION
# ---------------------------------------------------
st.header("Schools by County")

st.subheader("Education Distribution")

fig_bar = px.bar(
    school_df,
    x="County",
    y="Schools",
    color="County",
    color_discrete_sequence=hospital_colors
)

fig_bar.update_layout(
    height=700,
    paper_bgcolor="#f5f5f5",
    plot_bgcolor="#f5f5f5",
    font=dict(size=18),
    xaxis_title="County",
    yaxis_title="Schools",
    showlegend=True,
    legend_title="County"
)

fig_bar.update_xaxes(
    tickangle=-30
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Developed for Warrap State Integrated Information System")
