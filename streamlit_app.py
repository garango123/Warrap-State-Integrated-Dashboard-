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
# CUSTOM STYLE
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: #4CAF50;
}

.stMetric {
    background-color: #1c1f26;
    padding: 10px;
    border-radius: 10px;
}

.css-1d391kg {
    background-color: #161a23;
}
</style>
""", unsafe_allow_html=True)

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
        text="Value"
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

    st.plotly_chart(fig_education, use_container_width=True)

    st.subheader("Education Support Centers")

    fig_support = px.bar(
        education_df,
        x="County",
        y=["CEC Centers", "TVET Centers"],
        barmode="group",
        title="CEC and TVET Distribution"
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

    st.plotly_chart(fig_livestock, use_container_width=True)

    st.markdown("""
    ### Livestock Importance

    Livestock represents the primary store of cultural and economic wealth in Warrap State.

    - Source of dowry and marriage wealth
    - Food security asset
    - Emergency financial reserve
    - Mobile economic wealth

    ### Seasonal Migration Patterns

    #### Dry Season
    Large cattle herds migrate toward Toic floodplains and swamp grazing areas.

    #### Wet Season
    Herds return to elevated settlement areas to avoid livestock diseases and support agriculture.
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

    st.plotly_chart(fig_crop, use_container_width=True)

    st.markdown("""
    ### Agricultural Characteristics

    - Sorghum is the dominant staple crop across all six counties.
    - Groundnuts are major cash crops especially in Twic and Gogrial.
    - Millet and sesame are commonly intercropped.
    - Maize is grown near homesteads for fresh consumption.

    ### Gender Roles

    Women perform nearly 90% of active agricultural labor:
    - Weeding
    - Harvesting
    - Crop processing

    Men mainly engage in:
    - Livestock management
    - Land clearing
    - Security activities
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
        color="Severity",
        title="Major Climate and Resource Challenges"
    )

    st.plotly_chart(fig_climate, use_container_width=True)

    st.markdown("""
    ### Climate Shocks

    Recurring flooding heavily affects:
    - Crop yields
    - Livestock survival
    - Household food security

    ### Major Livestock Diseases
    - Anthrax
    - Rift Valley Fever

    ### Resource-Based Conflict

    Seasonal migration occasionally creates localized tensions over:
    - Water access
    - Grazing land
    - Crop trampling
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
