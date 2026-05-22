# ============================================================
# WARRAP STATE INTEGRATED ANALYTICS DASHBOARD
# Modern Styled Version
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Warrap State Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS STYLING
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

h1 {
    font-size: 52px !important;
    font-weight: 800 !important;
    color: #111827;
}

h2, h3 {
    color: #111827;
    font-weight: 700;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
    text-align: center;
}

div[data-testid="stPlotlyChart"] {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
    margin-bottom: 30px;
}

section[data-testid="stSidebar"] {
    background-color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# TITLE
# ============================================================

st.title("Warrap State Integrated Analytics Dashboard")

st.markdown("""
### County-Level Analytics for Population, Education, Health, and Infrastructure
""")

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Dashboard Navigation")

section = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Population",
        "Education",
        "Health"
    ]
)

# ============================================================
# DATA
# ============================================================

counties = [
    "Tonj North",
    "Tonj East",
    "Tonj South",
    "Gogrial West",
    "Gogrial East",
    "Twic"
]

population = [250000, 210000, 230000, 200000, 190000, 220000]

schools = [5, 5, 5, 5, 5, 5]

hospitals = [6, 4, 6, 5, 4, 5]

# ============================================================
# OVERVIEW SECTION
# ============================================================

if section == "Overview":

    st.header("Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Population", "1.3M")

    with col2:
        st.metric("Total Schools", "30")

    with col3:
        st.metric("Total Hospitals", "30")

    # Population DataFrame
    population_df = pd.DataFrame({
        "County": counties,
        "Population": population
    })

    # Population Chart
    fig_population = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population",
        title="County Population Comparison",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig_population.update_layout(
        template="plotly_white",
        height=600,
        title_font_size=28,
        font=dict(size=18),
        xaxis_title="County",
        yaxis_title="Population",
        showlegend=True
    )

    fig_population.update_traces(
        textposition="inside"
    )

    st.plotly_chart(fig_population, use_container_width=True)

# ============================================================
# POPULATION SECTION
# ============================================================

elif section == "Population":

    st.header("Population by County")

    population_df = pd.DataFrame({
        "County": counties,
        "Population": population
    })

    fig_population = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population",
        title="County Population Comparison",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig_population.update_layout(
        template="plotly_white",
        height=650,
        title_font_size=30,
        font=dict(size=18),
        xaxis_title="County",
        yaxis_title="Population"
    )

    fig_population.update_traces(
        textposition="inside"
    )

    st.plotly_chart(fig_population, use_container_width=True)

# ============================================================
# EDUCATION SECTION
# ============================================================

elif section == "Education":

    st.header("Schools by County")

    schools_df = pd.DataFrame({
        "County": counties,
        "Schools": schools
    })

    fig_schools = px.bar(
        schools_df,
        x="County",
        y="Schools",
        color="County",
        title="Education Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig_schools.update_layout(
        template="plotly_white",
        height=650,
        title_font_size=30,
        font=dict(size=18),
        xaxis_title="County",
        yaxis_title="Schools"
    )

    st.plotly_chart(fig_schools, use_container_width=True)

# ============================================================
# HEALTH SECTION
# ============================================================

elif section == "Health":

    st.header("Hospital Distribution")

    hospital_df = pd.DataFrame({
        "County": counties,
        "Hospitals": hospitals
    })

    fig_hospital = px.pie(
        hospital_df,
        names="County",
        values="Hospitals",
        title="Hospitals Across Counties",
        hole=0.25,
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig_hospital.update_layout(
        template="plotly_white",
        height=700,
        title_font_size=30,
        font=dict(size=18)
    )

    st.plotly_chart(fig_hospital, use_container_width=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
<center>
Developed for Warrap State Integrated Analytics Dashboard
</center>
""", unsafe_allow_html=True)
