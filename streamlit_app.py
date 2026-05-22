import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Warrap State Dashboard",
    page_icon="📊",
    layout="wide"
)

# ======================================================
# CUSTOM STYLING
# ======================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    font-family: 'Segoe UI';
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("📌 Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Population",
        "Healthcare",
        "Education",
        "Livestock",
        "Agriculture",
        "Climate"
    ]
)

# ======================================================
# HEADER
# ======================================================

st.title("📊 Warrap State Integrated Analytics Dashboard")

st.markdown("""
A professional regional analytics platform providing insights into:

- Population
- Healthcare
- Education
- Agriculture
- Livestock
- Climate Impacts
""")

st.markdown("---")

# ======================================================
# DATA
# ======================================================

population_df = pd.DataFrame({
    "County": [
        "Tonj North",
        "Tonj East",
        "Tonj South",
        "Gogrial West",
        "Gogrial East",
        "Twic"
    ],
    "Population": [
        250000,
        210000,
        230000,
        200000,
        190000,
        220000
    ]
})

hospital_df = pd.DataFrame({
    "County": [
        "Tonj South",
        "Twic",
        "Tonj North",
        "Gogrial West",
        "Tonj East",
        "Gogrial East"
    ],
    "Hospitals": [6, 6, 5, 5, 4, 4]
})

education_df = pd.DataFrame({
    "County": [
        "Tonj North",
        "Tonj East",
        "Tonj South",
        "Gogrial West",
        "Gogrial East",
        "Twic"
    ],
    "Schools": [
        209,
        131,
        109,
        315,
        234,
        288
    ]
})

# ======================================================
# OVERVIEW
# ======================================================

if section == "Overview":

    st.subheader("📍 State Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Population", "1.5M")
    c2.metric("Hospitals", "48")
    c3.metric("Schools", "1,286")
    c4.metric("Cattle", "3M")

    st.markdown("## County Population Comparison")

    fig = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population"
    )

    fig.update_layout(height=500)

    st.plotly_chart(fig, use_container_width=True)

# ======================================================
# POPULATION
# ======================================================

elif section == "Population":

    st.header("👥 Population Analytics")

    fig = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population"
    )

    st.plotly_chart(fig, use_container_width=True)

    pie = px.pie(
        population_df,
        names="County",
        values="Population",
        hole=0.4
    )

    st.plotly_chart(pie, use_container_width=True)

# ======================================================
# HEALTHCARE
# ======================================================

elif section == "Healthcare":

    st.header("🏥 Healthcare Infrastructure")

    h1, h2, h3 = st.columns(3)

    h1.metric("PHCCs", "21")
    h2.metric("PHCUs", "27")
    h3.metric("Referral Hospitals", "4")

    st.subheader("Hospital Distribution")

    pie = px.pie(
        hospital_df,
        names="County",
        values="Hospitals",
        color="County"
    )

    st.plotly_chart(pie, use_container_width=True)

    st.subheader("Referral Hospitals")

    hospitals = pd.DataFrame({
        "Hospital": [
            "Kuajok State Hospital",
            "Tonj Civil Hospital",
            "Turalei Hospital",
            "Marial Lou Hospital"
        ],
        "Town": [
            "Kuajok",
            "Tonj",
            "Turalei",
            "Marial Lou"
        ],
        "County": [
            "Gogrial West",
            "Tonj South",
            "Twic",
            "Tonj North"
        ]
    })

    st.dataframe(hospitals, use_container_width=True)

# ======================================================
# EDUCATION
# ======================================================

elif section == "Education":

    st.header("🎓 Education Infrastructure")

    school_chart = px.bar(
        education_df,
        x="County",
        y="Schools",
        color="County",
        text="Schools"
    )

    st.plotly_chart(school_chart, use_container_width=True)

    e1, e2, e3, e4 = st.columns(4)

    e1.metric("Primary Schools", "1,286")
    e2.metric("Secondary Schools", "86")
    e3.metric("CEC Centers", "6")
    e4.metric("TVET Centers", "3")

# ======================================================
# LIVESTOCK
# ======================================================

elif section == "Livestock":

    st.header("🐄 Livestock Economy")

    st.metric(
        "Estimated Cattle Population",
        "3 Million Head"
    )

    livestock_df = pd.DataFrame({
        "County": [
            "Twic",
            "Tonj North",
            "Gogrial West",
            "Tonj East",
            "Tonj South",
            "Gogrial East"
        ],
        "Cattle": [
            650000,
            540000,
            520000,
            470000,
            430000,
            390000
        ]
    })

    cattle_chart = px.bar(
        livestock_df,
        x="County",
        y="Cattle",
        color="County",
        text="Cattle"
    )

    st.plotly_chart(cattle_chart, use_container_width=True)

# ======================================================
# AGRICULTURE
# ======================================================

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
        "Production": [
            90,
            75,
            65,
            40,
            30
        ]
    })

    crop_chart = px.bar(
        crop_df,
        x="Crop",
        y="Production",
        color="Crop",
        text="Production"
    )

    st.plotly_chart(crop_chart, use_container_width=True)

    st.success("Women contribute approximately 90% of agricultural labor.")

# ======================================================
# CLIMATE
# ======================================================

elif section == "Climate":

    st.header("🌧 Climate Challenges")

    climate_df = pd.DataFrame({
        "Issue": [
            "Flooding",
            "Food Insecurity",
            "Livestock Disease",
            "Water Competition",
            "Crop Loss"
        ],
        "Impact": [
            95,
            90,
            75,
            65,
            85
        ]
    })

    climate_chart = px.line(
        climate_df,
        x="Issue",
        y="Impact",
        markers=True
    )

    st.plotly_chart(climate_chart, use_container_width=True)

# ======================================================
# MAP
# ======================================================

st.markdown("---")

st.subheader("🗺 Interactive County Map")

m = folium.Map(
    location=[7.5, 28.0],
    zoom_start=7
)

locations = [
    [7.7, 27.99, "Kuajok"],
    [7.27, 28.68, "Tonj"],
    [8.13, 28.47, "Turalei"]
]

for lat, lon, name in locations:
    folium.Marker(
        [lat, lon],
        tooltip=name
    ).add_to(m)

st_folium(m, width=1200)

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

st.caption("""
Data Sources:
- Warrap State Government
- Ministry of Health
- Education Sector Updates
- Regional Assessments
""")
