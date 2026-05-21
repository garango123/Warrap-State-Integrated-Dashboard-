import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Warrap State Dashboard",
    layout="wide"
)

# ---------------------------------
# TITLE
# ---------------------------------
st.title("Warrap State Integrated Dashboard")
st.markdown("Interactive county statistics for Warrap State")

# ---------------------------------
# LOAD DATA
# ---------------------------------
df = pd.read_csv("data/counties.csv")

# ---------------------------------
# SIDEBAR
# ---------------------------------
st.sidebar.header("County Filter")

county = st.sidebar.selectbox(
    "Choose County",
    ["All Counties"] + list(df["County"])
)

# ---------------------------------
# FILTER DATA
# ---------------------------------
if county == "All Counties":
    filtered_df = df
else:
    filtered_df = df[df["County"] == county]

# ---------------------------------
# METRICS
# ---------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Population",
    f"{filtered_df['Population'].sum():,}"
)

col2.metric(
    "Schools",
    f"{filtered_df['Schools'].sum():,}"
)

col3.metric(
    "Hospitals",
    f"{filtered_df['Hospitals'].sum():,}"
)

col4.metric(
    "GDP",
    f"{filtered_df['GDP'].sum():,}M"
)

# ---------------------------------
# BAR CHART
# ---------------------------------
st.subheader("Population by County")

fig_population = px.bar(
    filtered_df,
    x="County",
    y="Population",
    color="County",
    text_auto=True,
    title="County Population Comparison"
)

st.plotly_chart(fig_population, use_container_width=True)

# ---------------------------------
# EDUCATION CHART
# ---------------------------------
st.subheader("Schools by County")

fig_schools = px.bar(
    filtered_df,
    x="County",
    y="Schools",
    color="County",
    text_auto=True,
    title="Education Distribution"
)

st.plotly_chart(fig_schools, use_container_width=True)

# ---------------------------------
# HEALTH PIE CHART
# ---------------------------------
st.subheader("Hospital Distribution")

fig_hospital = px.pie(
    filtered_df,
    names="County",
    values="Hospitals",
    title="Hospitals Across Counties"
)

st.plotly_chart(fig_hospital, use_container_width=True)

# ---------------------------------
# DATA TABLE
# ---------------------------------
st.subheader("County Statistics Table")

st.dataframe(filtered_df, use_container_width=True)

# ---------------------------------
# FOOTER
# ---------------------------------
st.success("Dashboard loaded successfully")
