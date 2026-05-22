import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_aggrid import AgGrid, GridOptionsBuilder
import folium
from streamlit_folium import st_folium

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Warrap State Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 5px solid #1f77b4;
}

.sidebar .sidebar-content {
    background-color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

    st.title("Warrap Dashboard")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Overview",
            "Population",
            "Healthcare",
            "Education",
            "Livestock",
            "Agriculture",
            "Climate"
        ],
        icons=[
            "house",
            "people-fill",
            "hospital-fill",
            "book-fill",
            "globe",
            "tree-fill",
            "cloud-rain-heavy-fill"
        ],
        menu_icon="cast",
        default_index=0
    )

# =========================================================
# HEADER
# =========================================================

st.title("📊 Warrap State Integrated Data Analytics Dashboard")

st.markdown("""
### Real-Time Regional Development Analytics Platform

This dashboard provides integrated insights into:

- Population Distribution
- Healthcare Infrastructure
- Education Systems
- Livestock Economy
- Agriculture Production
- Climate Challenges
- County-Level Development Indicators
""")

st.markdown("---")

# =========================================================
# DATASETS
# =========================================================

population_df = pd.DataFrame({
    "County": [
        "Tonj North",
        "Tonj East",
        "Tonj South",
        "Gogrial West",
        "Gogrial East",
        "Twic"
    ],
    "Population": [250000, 210000, 230000, 200000, 190000, 220000]
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
    "Primary Schools": [209, 131, 109, 315, 234, 288]
})

# =========================================================
# OVERVIEW PAGE
# =========================================================

if selected == "Overview":

    st.subheader("📌 State Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Population", "1.5M")
    col2.metric("Hospitals", "48")
    col3.metric("Schools", "1,286")
    col4.metric("Cattle Population", "3M")

    style_metric_cards()

    st.markdown("## County Population Comparison")

    fig = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population",
        template="plotly_white"
    )

    fig.update_traces(
        texttemplate='%{text:.2s}',
        textposition='outside'
    )

    fig.update_layout(
        height=500,
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# POPULATION PAGE
# =========================================================

elif selected == "Population":

    st.header("👥 Population Analytics")

    total_population = population_df["Population"].sum()

    st.metric(
        "Estimated Regional Population",
        f"{total_population:,}"
    )

    fig = px.bar(
        population_df,
        x="County",
        y="Population",
        color="County",
        text="Population",
        template="plotly_white"
    )

    fig.update_layout(height=550)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Population Distribution")

    pie_fig = px.pie(
        population_df,
        names="County",
        values="Population",
        hole=0.45
    )

    st.plotly_chart(pie_fig, use_container_width=True)

# =========================================================
# HEALTHCARE PAGE
# =========================================================

elif selected == "Healthcare":

    st.header("🏥 Healthcare Infrastructure")

    c1, c2, c3 = st.columns(3)

    c1.metric("PHCCs", "21")
    c2.metric("PHCUs", "27")
    c3.metric("Referral Hospitals", "4")

    style_metric_cards()

    st.subheader("Hospital Distribution")

    pie = px.pie(
        hospital_df,
        names="County",
        values="Hospitals",
        color="County",
        hole=0.3
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

    gb = GridOptionsBuilder.from_dataframe(hospitals)
    gb.configure_pagination()
    gb.configure_side_bar()

    AgGrid(
        hospitals,
        gridOptions=gb.build(),
        fit_columns_on_grid_load=True
    )

# =========================================================
# EDUCATION PAGE
# =========================================================

elif selected == "Education":

    st.header("🎓 Education Infrastructure")

    st.subheader("Schools by County")

    school_fig = px.bar(
        education_df,
        x="County",
        y="Primary Schools",
        color="County",
        text="Primary Schools",
        template="plotly_white"
    )

    school_fig.update_layout(height=550)

    st.plotly_chart(school_fig, use_container_width=True)

    st.subheader("Education Summary")

    e1, e2, e3, e4 = st.columns(4)

    e1.metric("Primary Schools", "1,286")
    e2.metric("Secondary Schools", "86")
    e3.metric("CEC Centers", "6")
    e4.metric("TVET Centers", "3")

    style_metric_cards()

# =========================================================
# LIVESTOCK PAGE
# =========================================================

elif selected == "Livestock":

    st.header("🐄 Livestock Economy")

    st.metric(
        "Estimated Cattle Population",
        "3 Million Head"
    )

    style_metric_cards()

    livestock_data = pd.DataFrame({
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

    cattle_fig = px.bar(
        livestock_data,
        x="County",
        y="Cattle",
        color="County",
        text="Cattle",
        template="plotly_white"
    )

    st.plotly_chart(cattle_fig, use_container_width=True)

    st.info("""
    Livestock serves as:
    - Cultural wealth
    - Economic reserve
    - Food security source
    - Mobile asset system
    """)

# =========================================================
# AGRICULTURE PAGE
# =========================================================

elif selected == "Agriculture":

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

    crop_fig = px.bar(
        crop_df,
        x="Crop",
        y="Production",
        color="Crop",
        text="Production",
        template="plotly_white"
    )

    st.plotly_chart(crop_fig, use_container_width=True)

    st.success("""
    Women contribute approximately 90% of agricultural labor.
    """)

# =========================================================
# CLIMATE PAGE
# =========================================================

elif selected == "Climate":

    st.header("🌧 Climate & Environmental Challenges")

    climate_data = pd.DataFrame({
        "Issue": [
            "Flooding",
            "Crop Loss",
            "Livestock Disease",
            "Water Competition",
            "Food Insecurity"
        ],
        "Impact Level": [95, 85, 75, 65, 90]
    })

    climate_fig = px.line(
        climate_data,
        x="Issue",
        y="Impact Level",
        markers=True
    )

    st.plotly_chart(climate_fig, use_container_width=True)

    st.warning("""
    Major challenges affecting Warrap State include:
    - Seasonal flooding
    - Livestock disease outbreaks
    - Farmer-pastoralist conflicts
    - Water scarcity
    """)

# =========================================================
# MAP SECTION
# =========================================================

st.markdown("---")

st.subheader("🗺 Regional Interactive Map")

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

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Data Sources:
- Warrap State Government
- Ministry of Health
- Education Sector Updates
- Regional Humanitarian Assessments
""")
