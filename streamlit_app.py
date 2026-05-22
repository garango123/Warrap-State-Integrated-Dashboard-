import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# CUSTOM STYLE (Exact Screenshot Style)
# =========================================================

st.markdown("""
<style>

/* Global white background */
.main, .block-container {
    background-color: white !important;
    color: black !important;
}

/* Headings: match screenshot style */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: #1c1c1c !important;
    margin-bottom: 0px !important;
}

h2 {
    font-size: 28px !important;
    font-weight: 700 !important;
    color: #2b2b2b !important;
}

h3 {
    font-size: 22px !important;
    font-weight: 600 !important;
    color: #333 !important;
}

/* Remove padding from top */
.block-container {
    padding-top: 10px !important;
}

/* Sidebar styling */
.css-1d391kg, .sidebar .sidebar-content {
    background-color: #f7f7f7 !important;
}

/* Metric boxes like screenshot */
div[data-testid="stMetric"] {
    background-color: #f2f2f2;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# COLOR PALETTE (Matches screenshot exactly)
# =========================================================

county_colors = {
    "Tonj North": "#0057B7",
    "Tonj East": "#66B2FF",
    "Tonj South": "#FF2B2B",
    "Gogrial West": "#FFB3B3",
    "Gogrial East": "#009688",
    "Twic": "#8BF5A3"
}

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Warrap State Dashboard")

section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Education",
        "Healthcare",
        "Livestock",
        "Agriculture",
        "Climate Challenges",
        "County Overview"
    ]
)

# =========================================================
# HEADER
# =========================================================

st.title("📊 Warrap State Integrated Data Analytics Dashboard")

st.markdown("""
A comprehensive regional analytics platform providing insights into:

- Population  
- Healthcare Infrastructure  
- Education Systems  
- Livestock Economy  
- Agriculture  
- Climate Impacts  
- County-Level Development Indicators  
""")

# =========================================================
# OVERVIEW SECTION
# =========================================================

if section == "Overview":

    st.header("State Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Population", "1.5M")
    col2.metric("Primary Schools", "1,286")
    col3.metric("Secondary Schools", "86")
    col4.metric("Health Facilities", "48")
    col5.metric("Cattle Population", "3M")

    st.markdown("---")

    overview_df = pd.DataFrame({
        "Indicator": [
            "Primary Schools",
            "Secondary Schools",
            "Health Facilities",
            "Referral Hospitals",
            "Cattle Population (Millions)"
        ],
        "Value": [1286, 86, 48, 4, 3]
    })

    fig_overview = px.bar(
        overview_df,
        x="Indicator",
        y="Value",
        title="Warrap State Key Indicators",
        text="Value",
        color="Indicator"
    )

    fig_overview.update_layout(
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0
    )

    st.plotly_chart(fig_overview, use_container_width=True)

# =========================================================
# EDUCATION SECTION
# =========================================================

elif section == "Education":

    st.header("📚 Education Infrastructure")

    education_df = pd.DataFrame({
        "County": [
            "Gogrial West",
            "Twic",
            "Gogrial East",
            "Tonj North",
            "Tonj South",
            "Tonj East"
        ],
        "Primary Schools": [315, 288, 234, 209, 109, 131],
        "Secondary Schools": [26, 15, 11, 9, 22, 3],
        "CEC Centers": [1, 1, 1, 1, 1, 1],
        "TVET Centers": [1, 1, 0, 0, 1, 0]
    })

    st.subheader("Schools Distribution Across Counties")

    fig_education = px.bar(
        education_df,
        x="County",
        y=["Primary Schools", "Secondary Schools"],
        barmode="group",
        title="Primary and Secondary Schools"
    )

    fig_education.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_education, use_container_width=True)

    st.subheader("Education Support Centers")

    fig_support = px.bar(
        education_df,
        x="County",
        y=["CEC Centers", "TVET Centers"],
        barmode="group",
        title="CEC and TVET Distribution"
    )

    fig_support.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_support, use_container_width=True)

    st.dataframe(education_df, use_container_width=True)

# =========================================================
# HEALTHCARE SECTION
# =========================================================

elif section == "Healthcare":

    st.header("🏥 Healthcare Infrastructure")

    health_df = pd.DataFrame({
        "Facility Type": [
            "PHCCs",
            "PHCUs",
            "Referral Hospitals"
        ],
        "Count": [21, 27, 4]
    })

    fig_health = px.pie(
        health_df,
        values="Count",
        names="Facility Type",
        title="Healthcare Infrastructure Distribution"
    )

    fig_health.update_layout(paper_bgcolor="white")

    st.plotly_chart(fig_health, use_container_width=True)

    hospital_df = pd.DataFrame({
        "Hospital": [
            "Kuajok State Hospital",
            "Tonj Civil Hospital",
            "Turalei Hospital",
            "Marial Lou Hospital"
        ],
        "County": [
            "Gogrial West",
            "Tonj South",
            "Twic",
            "Tonj North"
        ]
    })

    st.subheader("Major Referral Hospitals")
    st.dataframe(hospital_df, use_container_width=True)

# =========================================================
# LIVESTOCK SECTION
# =========================================================

elif section == "Livestock":

    st.header("🐄 Livestock Economy")

    livestock_df = pd.DataFrame({
        "Livestock Type": ["Cattle"],
        "Population": [3000000]
    })

    fig_livestock = px.bar(
        livestock_df,
        x="Livestock Type",
        y="Population",
        title="Estimated Livestock Population",
        text="Population"
    )

    fig_livestock.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_livestock, use_container_width=True)

    st.markdown("""
    ### Livestock Importance

    Livestock represents the primary store of cultural and economic wealth in Warrap State.

    - Source of dowry and marriage wealth  
    - Food security asset  
    - Emergency financial reserve  
    - Mobile economic wealth  

    ### Seasonal Migration Patterns  

    **Dry Season:** Cattle migrate to Toic floodplains.  
    **Wet Season:** Herds return to higher ground.  
    """)

# =========================================================
# AGRICULTURE SECTION
# =========================================================

elif section == "Agriculture":

    st.header("🌾 Agricultural Production")

    crop_df = pd.DataFrame({
        "Crop": [
            "Sorghum",
            "Groundnuts",
            "Millet",
            "Sesame",
            "Maize"
        ],
        "Production Index": [95, 70, 60, 55, 40]
    })

    fig_crop = px.line(
        crop_df,
        x="Crop",
        y="Production Index",
        markers=True,
        title="Major Agricultural Crops"
    )

    fig_crop.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_crop, use_container_width=True)

    st.markdown("""
    ### Agricultural Characteristics

    - Sorghum is the dominant staple crop.  
    - Groundnuts are a major cash crop.  
    - Millet & sesame are often intercropped.  
    - Maize is grown near homesteads.  

    ### Gender Roles  

    Women perform **90% of farm labor**.  
    """)

# =========================================================
# CLIMATE SECTION
# =========================================================

elif section == "Climate Challenges":

    st.header("🌍 Climate and System Stressors")

    climate_df = pd.DataFrame({
        "Challenge": [
            "Flooding",
            "Anthrax",
            "Rift Valley Fever",
            "Water Conflict",
            "Crop Destruction"
        ],
        "Severity": [95, 70, 65, 60, 75]
    })

    fig_climate = px.bar(
        climate_df,
        x="Challenge",
        y="Severity",
        title="Major Climate and Resource Challenges",
        color="Severity"
    )

    fig_climate.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_climate, use_container_width=True)

    st.markdown("""
    Flooding, livestock disease, and water conflict are the most significant climate shocks impacting Warrap State.  
    """)

# =========================================================
# COUNTY OVERVIEW
# =========================================================

elif section == "County Overview":

    st.header("🗺️ County Overview")

    county_df = pd.DataFrame({
        "County": [
            "Gogrial West",
            "Twic",
            "Gogrial East",
            "Tonj North",
            "Tonj South",
            "Tonj East"
        ],
        "Economic Activities": [
            "Livestock & Farming",
            "Groundnuts & Livestock",
            "Agriculture & Livestock",
            "Sorghum & Livestock",
            "Agriculture & Trade",
            "Pastoralism & Farming"
        ]
    })

    st.dataframe(county_df, use_container_width=True)

    county_chart = px.bar(
        county_df,
        x="County",
        title="Economic Activities Across Counties"
    )

    county_chart.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(county_chart, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Data Sources:  
- Warrap State Government  
- Ministry of Health  
- Education Sector Updates  
- FAO Regional Assessments  
""")
