import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("📊 Warrap State Integrated Dashboard")
st.markdown("Interactive Development Intelligence System for Warrap State")

# ============================================================
# COUNTIES
# ============================================================

counties = [
    "Tonj North",
    "Tonj East",
    "Tonj South",
    "Gogrial West",
    "Gogrial East",
    "Twic County"
]

# ============================================================
# SAMPLE DATA GENERATION
# ============================================================

np.random.seed(42)

# GDP DATA

gdp_df = pd.DataFrame({
    "County": counties,
    "GDP_Million_USD": np.random.randint(100, 500, len(counties)),
    "Agriculture": np.random.randint(40, 90, len(counties)),
    "Trade": np.random.randint(10, 60, len(counties)),
    "Livestock": np.random.randint(30, 80, len(counties))
})

# EDUCATION DATA

education_df = pd.DataFrame({
    "County": counties,
    "Enrollment_Rate": np.random.randint(40, 95, len(counties)),
    "Literacy_Rate": np.random.randint(20, 80, len(counties)),
    "Schools": np.random.randint(20, 150, len(counties)),
    "Teachers": np.random.randint(50, 600, len(counties))
})

# HEALTH DATA

health_df = pd.DataFrame({
    "County": counties,
    "Health_Facilities": np.random.randint(5, 60, len(counties)),
    "Vaccination_Rate": np.random.randint(20, 95, len(counties)),
    "Maternal_Mortality": np.random.randint(200, 900, len(counties)),
    "Doctors": np.random.randint(2, 50, len(counties))
})

# CLIMATE DATA

climate_df = pd.DataFrame({
    "County": counties,
    "Rainfall_mm": np.random.randint(400, 1500, len(counties)),
    "Temperature_C": np.random.randint(24, 38, len(counties)),
    "Flood_Risk_Index": np.random.randint(1, 10, len(counties)),
    "Drought_Risk_Index": np.random.randint(1, 10, len(counties))
})

# ELECTION DATA

election_df = pd.DataFrame({
    "County": counties,
    "Registered_Voters": np.random.randint(20000, 150000, len(counties)),
    "Turnout_Percentage": np.random.randint(45, 90, len(counties)),
    "Youth_Voters": np.random.randint(5000, 70000, len(counties))
})

# POPULATION DATA

population_df = pd.DataFrame({
    "County": counties,
    "Population_2020": np.random.randint(50000, 300000, len(counties)),
    "Population_2025": np.random.randint(70000, 450000, len(counties)),
    "Growth_Rate": np.random.uniform(1.5, 5.5, len(counties)).round(2)
})

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

module = st.sidebar.radio(
    "Select Dashboard",
    [
        "Overview",
        "GDP Analysis",
        "Education",
        "Health",
        "Climate",
        "Elections",
        "Population Growth"
    ]
)

selected_county = st.sidebar.selectbox(
    "Select County",
    counties
)

# ============================================================
# OVERVIEW DASHBOARD
# ============================================================

if module == "Overview":

    st.subheader("📌 State-Level Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Counties", len(counties))
    col2.metric("Estimated Population", f"{population_df['Population_2025'].sum():,}")
    col3.metric("Total Schools", education_df['Schools'].sum())
    col4.metric("Health Facilities", health_df['Health_Facilities'].sum())

    st.markdown("---")

    fig = px.bar(
        population_df,
        x="County",
        y="Population_2025",
        color="County",
        title="Population by County"
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# GDP DASHBOARD
# ============================================================

elif module == "GDP Analysis":

    st.subheader("💰 GDP Analysis Dashboard")

    fig = px.bar(
        gdp_df,
        x="County",
        y="GDP_Million_USD",
        color="County",
        text="GDP_Million_USD",
        title="County GDP Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(
        gdp_df,
        names="County",
        values="Agriculture",
        title="Agriculture Contribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(gdp_df)

# ============================================================
# EDUCATION DASHBOARD
# ============================================================

elif module == "Education":

    st.subheader("🎓 Education Dashboard")

    fig = px.line(
        education_df,
        x="County",
        y="Enrollment_Rate",
        markers=True,
        title="Enrollment Rate by County"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        education_df,
        x="County",
        y="Schools",
        color="County",
        title="Schools Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(education_df)

# ============================================================
# HEALTH DASHBOARD
# ============================================================

elif module == "Health":

    st.subheader("🏥 Health Dashboard")

    fig = px.bar(
        health_df,
        x="County",
        y="Vaccination_Rate",
        color="County",
        title="Vaccination Coverage"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.scatter(
        health_df,
        x="Doctors",
        y="Health_Facilities",
        size="Vaccination_Rate",
        color="County",
        title="Health Capacity Analysis"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(health_df)

# ============================================================
# CLIMATE DASHBOARD
# ============================================================

elif module == "Climate":

    st.subheader("🌦 Climate Dashboard")

    fig = px.bar(
        climate_df,
        x="County",
        y="Rainfall_mm",
        color="County",
        title="Rainfall Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(
        climate_df,
        x="County",
        y="Temperature_C",
        markers=True,
        title="Temperature Trends"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(climate_df)

# ============================================================
# ELECTION DASHBOARD
# ============================================================

elif module == "Elections":

    st.subheader("🗳 Election Dashboard")

    fig = px.bar(
        election_df,
        x="County",
        y="Registered_Voters",
        color="County",
        title="Registered Voters"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(
        election_df,
        names="County",
        values="Youth_Voters",
        title="Youth Voter Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(election_df)

# ============================================================
# POPULATION DASHBOARD
# ============================================================

elif module == "Population Growth":

    st.subheader("📈 Population Growth Dashboard")

    fig = px.bar(
        population_df,
        x="County",
        y="Growth_Rate",
        color="County",
        title="Population Growth Rate"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.line(
        population_df,
        x="County",
        y="Population_2025",
        markers=True,
        title="Projected Population 2025"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(population_df)

# ============================================================
# POWER BI EXPORTS
# ============================================================

st.sidebar.markdown("---")

if st.sidebar.button("Export CSV Files"):

    os.makedirs("exports", exist_ok=True)

    gdp_df.to_csv("exports/gdp_data.csv", index=False)
    education_df.to_csv("exports/education_data.csv", index=False)
    health_df.to_csv("exports/health_data.csv", index=False)
    climate_df.to_csv("exports/climate_data.csv", index=False)
    election_df.to_csv("exports/election_data.csv", index=False)
    population_df.to_csv("exports/population_data.csv", index=False)

    st.sidebar.success("CSV files exported successfully!")

# ============================================================
# OPTIONAL SQLITE DATABASE
# ============================================================

use_database = st.sidebar.checkbox("Enable SQLite Database")

if use_database:

    conn = sqlite3.connect("warrap_dashboard.db")

    gdp_df.to_sql("gdp", conn, if_exists="replace", index=False)
    education_df.to_sql("education", conn, if_exists="replace", index=False)
    health_df.to_sql("health", conn, if_exists="replace", index=False)
    climate_df.to_sql("climate", conn, if_exists="replace", index=False)
    election_df.to_sql("elections", conn, if_exists="replace", index=False)
    population_df.to_sql("population", conn, if_exists="replace", index=False)

    st.sidebar.success("SQLite Database Connected")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.caption("Warrap State Integrated Dashboard • Built with Streamlit")
