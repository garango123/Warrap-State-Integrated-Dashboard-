import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    layout="wide",
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #1f2937 !important;
}

h2 {
    font-size: 28px !important;
    font-weight: 700 !important;
    color: #111827 !important;
    margin-top: 40px !important;
}

h3 {
    color: #374151 !important;
}

p, li {
    color: #4b5563 !important;
    font-size: 16px !important;
    line-height: 1.7 !important;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    text-align: center;
}

/* DataFrames */
[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #e5e7eb;
    background: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    padding: 10px;
}

/* Plotly charts */
.js-plotly-plot {
    background: white !important;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    border: 1px solid #e5e7eb;
}

/* Success box */
.success-box {
    background: #dff5e6;
    color: #1d7a3e;
    padding: 20px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("Warrap State Integrated Data Analytics Dashboard")

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
# POPULATION SECTION
# =========================================================

st.header("Population Overview")

st.metric(
    label="Estimated Population",
    value="1.5 Million"
)

st.info("""
Warrap State consists of six counties:
Twic, Tonj East, Tonj South, Tonj North,
Gogrial East, and Gogrial West.
""")

population_df = pd.DataFrame({
    "County": [
        "Tonj North",
        "Tonj East",
        "Tonj South",
        "Gogrial West",
        "Gogrial East",
        "Twic"
    ],
    "Population": [240000, 210000, 207000, 337000, 218000, 288000]
})

st.subheader("Population by County")

population_chart = px.bar(
    population_df,
    x="County",
    y="Population",
    color="County",
    text="Population"
)

population_chart.update_layout(
    height=500,
    showlegend=True
)

st.plotly_chart(population_chart, use_container_width=True)

# =========================================================
# HEALTHCARE SECTION
# =========================================================

st.header("Healthcare Infrastructure")

st.markdown("""
Greater Warrap State currently has 108 officially integrated primary healthcare facilities operating within the regional healthcare service network.
""")

col1, col2, col3 = st.columns(3)

col1.metric("PHCCs", "23")
col2.metric("PHCUs", "85")
col3.metric("Referral Hospitals", "4")

hospital_df = pd.DataFrame({
    "County": [
        "Tonj South",
        "Twic",
        "Tonj North",
        "Gogrial West",
        "Tonj East",
        "Gogrial East"
    ],
    "Hospitals": [6, 4, 5, 5, 4, 4]
})

# =========================================================
# REFERRAL HOSPITAL DIRECTORY
# =========================================================

st.subheader(" Referral Hospital Directory")

referral_hospitals_df = pd.DataFrame({
    "Hospital Name": [
        "Kuajok State Hospital",
        "Tonj Civil Hospital",
        "Turalei Hospital",
        "Marial Lou Hospital"
    ],
    "Town Location": [
        "Kuajok Town",
        "Tonj Town",
        "Turalei Town",
        "Marial Lou Payam"
    ],
    "County Location": [
        "Gogrial West County",
        "Tonj South County",
        "Twic County",
        "Tonj North County"
    ],
    "Regional Focus": [
        "Main capital hub for the state",
        "Main hub for the southern zone",
        "Handles the northern border areas",
        "Handles the northwestern interior"
    ]
})

st.dataframe(
    referral_hospitals_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# HEALTH FACILITY DIRECTORY
# =========================================================

st.header("Healthcare Facility Directory")

st.info("""
The table below contains officially integrated Primary Health Care Centres (PHCCs)
and Primary Health Care Units (PHCUs) across Warrap State.

Note: Some facilities are currently experiencing operational challenges due to
communal conflict and insecurity in certain areas. Functionality may vary
depending on security and funding conditions.
""")


facility_data = [
# TWIC COUNTY PHCCs
["Twic","PHCC","Ajak Kuac"],
["Twic","PHCC","Akok PHCC"],
["Twic","PHCC","Aweng"],
["Twic","PHCC","Magak PHCC"],
["Twic","PHCC","Majok Noon"],
["Twic","PHCC","Mayen Abun"],
["Twic","PHCC","Turalei PHCC"],
["Twic","PHCC","Wunrok PHCC"],

# TWIC COUNTY PHCUs
["Twic","PHCU","Ajong PHCU"],
["Twic","PHCU","Anyiel PHCU"],
["Twic","PHCU","Bulyom PHCU"],
["Twic","PHCU","Dhiau Agaal PHCU"],
["Twic","PHCU","Majak Pagai PHCU"],
["Twic","PHCU","Malou-Hol PHCU"],
["Twic","PHCU","Maper PHCU"],
["Twic","PHCU","Marial Maper PHCU"],
["Twic","PHCU","Molbang PHCU"],
["Twic","PHCU","Pandit PHCU"],
["Twic","PHCU","Pannyok PHCU"],
["Twic","PHCU","Titcok PHCU"],
["Twic","PHCU","Toch Noon PHCU"],
["Twic","PHCU","Tuele PHCU"],
["Twic","PHCU","Yiik Thon PHCU"],

# TONJ SOUTH PHCCs
["Tonj South","PHCC","Don Bosco PHCC"],
["Tonj South","PHCC","Thiet PHCC"],

# TONJ SOUTH PHCUs
["Tonj South","PHCU","Aguka PHCU"],
["Tonj South","PHCU","Angur PHCU"],
["Tonj South","PHCU","Jak PHCU"],
["Tonj South","PHCU","Kal Kuel PHCU"],
["Tonj South","PHCU","Mabior Yar PHCU"],
["Tonj South","PHCU","Malual Muok PHCU"],
["Tonj South","PHCU","Manyiel Thony PHCU"],
["Tonj South","PHCU","Panakdie PHCU"],
["Tonj South","PHCU","Pawel PHCU"],
["Tonj South","PHCU","Wanh Alel PHCU"],

# TONJ NORTH PHCCs
["Tonj North","PHCC","Akop PHCC"],
["Tonj North","PHCC","Alabek PHCC"],
["Tonj North","PHCC","Aliek PHCC"],
["Tonj North","PHCC","Warrap PHCC"],

# TONJ NORTH PHCUs
["Tonj North","PHCU","Akurbiok PHCU"],
["Tonj North","PHCU","Aporlang PHCU"],
["Tonj North","PHCU","Awul PHCU"],
["Tonj North","PHCU","Indeed Truth PHCU"],
["Tonj North","PHCU","Kirik PHCU"],
["Tonj North","PHCU","Lurcuk PHCU"],
["Tonj North","PHCU","Madhiath PHCU"],
["Tonj North","PHCU","Manlor PHCU"],
["Tonj North","PHCU","Marial Abuok PHCU"],
["Tonj North","PHCU","Marial Lou PHCU"],
["Tonj North","PHCU","Pabukchak PHCU"],
["Tonj North","PHCU","Pagakdit PHCU"],
["Tonj North","PHCU","Pagol PHCU"],
["Tonj North","PHCU","Pankot PHCU"],
["Tonj North","PHCU","Parasika PHCU"],
["Tonj North","PHCU","Room Tit PHCU"],
["Tonj North","PHCU","Rual Bet PHCU"],

# TONJ EAST PHCCs
["Tonj East","PHCC","Ngabagok PHCC"],
["Tonj East","PHCC","Romic PHCC"],

# TONJ EAST PHCUs
["Tonj East","PHCU","Aloor PHCU"],
["Tonj East","PHCU","Ananatak PHCU"],
["Tonj East","PHCU","Kachuat PHCU"],
["Tonj East","PHCU","Kuel Cok PHCU"],
["Tonj East","PHCU","Makuac PHCU"],
["Tonj East","PHCU","Mayen PHCU"],
["Tonj East","PHCU","Palal PHCU"],
["Tonj East","PHCU","Paliang PHCU"],
["Tonj East","PHCU","Rumabuth PHCU"],
["Tonj East","PHCU","Wunchuei PHCU"],
["Tonj East","PHCU","Wunlit PHCU"],

# GOGRIAL WEST PHCCs
["Gogrial West","PHCC","Ajiep PHCC"],
["Gogrial West","PHCC","Alek PHCC"],
["Gogrial West","PHCC","Gogrial PHCC"],
["Gogrial West","PHCC","Kuajok PHCC"],
["Gogrial West","PHCC","Prison PHCC"],

# GOGRIAL WEST PHCUs
["Gogrial West","PHCU","Adet PHCU"],
["Gogrial West","PHCU","Aget PHCU"],
["Gogrial West","PHCU","Akon PHCU"],
["Gogrial West","PHCU","Anguoth PHCU"],
["Gogrial West","PHCU","Atuk Kuel PHCU"],
["Gogrial West","PHCU","Keet PHCU"],
["Gogrial West","PHCU","Magat PHCU"],
["Gogrial West","PHCU","Maluil Ajak PHCU"],
["Gogrial West","PHCU","Mayen Gumel PHCU"],
["Gogrial West","PHCU","Mayen Pajok PHCU"],
["Gogrial West","PHCU","Mayom PHCU"],
["Gogrial West","PHCU","Mayom Totin PHCU"],
["Gogrial West","PHCU","Nyokthiang PHCU"],
["Gogrial West","PHCU","Pakor PHCU"],
["Gogrial West","PHCU","Paliet PHCU"],
["Gogrial West","PHCU","Panachier PHCU"],
["Gogrial West","PHCU","Paweng PHCU"],
["Gogrial West","PHCU","Peeth PHCU"],
["Gogrial West","PHCU","Thurnyior PHCU"],

# GOGRIAL EAST PHCCs
["Gogrial East","PHCC","Lietnhom PHCC"],
["Gogrial East","PHCC","Luonyaker PHCC"],

# GOGRIAL EAST PHCUs
["Gogrial East","PHCU","Ajogo PHCU"],
["Gogrial East","PHCU","Angeruger PHCU"],
["Gogrial East","PHCU","Awut Wut PHCU"],
["Gogrial East","PHCU","Majak Nyiuom PHCU"],
["Gogrial East","PHCU","Maliai PHCU"],
["Gogrial East","PHCU","Mangol PHCU"],
["Gogrial East","PHCU","Matiel PHCU"],
["Gogrial East","PHCU","Mayom Biong PHCU"],
["Gogrial East","PHCU","Mayom Chol PHCU"],
["Gogrial East","PHCU","Pinydit PHCU"],
["Gogrial East","PHCU","Ruot PHCU"],
["Gogrial East","PHCU","Wunakoc PHCU"],
["Gogrial East","PHCU","Yiikadoor PHCU"]
]

facility_df = pd.DataFrame(
    facility_data,
    columns=["County", "Facility Type", "Facility Name"]
)

facility_df = facility_df.sort_values(
    ["County", "Facility Type", "Facility Name"]
)

st.dataframe(
    facility_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("Healthcare Facility Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Total PHCCs", "23")
c2.metric("Total PHCUs", "85")
c3.metric("Grand Total Facilities", "108")

hospital_chart = px.pie(
    hospital_df,
    names="County",
    values="Hospitals",
    hole=0.3
)

hospital_chart.update_layout(height=500)

st.plotly_chart(hospital_chart, use_container_width=True)

# =========================================================
# EDUCATION SECTION
# =========================================================

st.header("Education Infrastructure")

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
    "TVET Centers": [1, 1, 0, 0, 1, 0],
    "Headquarters": [
        "Gogrial HQRS",
        "Turalei HQRS",
        "Lietnhom HQRS",
        "Warrap HQRS",
        "Tonj HQRS",
        "Romic HQRS"
    ]
})

st.dataframe(education_df, use_container_width=True)

st.subheader("Education Summary")

e1, e2, e3, e4 = st.columns(4)

e1.metric("Primary Schools", "1,286")
e2.metric("Secondary Schools", "86")
e3.metric("CEC Centers", "6")
e4.metric("TVET Centers", "3")

st.subheader("Schools by County")

school_chart = px.bar(
    education_df,
    x="County",
    y="Primary Schools",
    color="County",
    text="Primary Schools"
)

school_chart.update_layout(height=500)

st.plotly_chart(school_chart, use_container_width=True)

# =========================================================
# LIVESTOCK SECTION
# =========================================================

st.header("Livestock Economy")

st.markdown("""
Livestock represents the primary store of both cultural and economic wealth in Warrap State.
""")

st.metric(
    label="Estimated Cattle Population",
    value="7 Million Head"
)

livestock_df = pd.DataFrame({
    "Category": [
        "Cultural Wealth",
        "Dowry",
        "Emergency Reserve",
        "Food Security",
        "Economic Assets"
    ],
    "Importance": [30, 20, 15, 20, 15]
})

st.subheader("Livestock Importance")

livestock_chart = px.pie(
    livestock_df,
    names="Category",
    values="Importance"
)

livestock_chart.update_layout(height=500)

st.plotly_chart(livestock_chart, use_container_width=True)

# =========================================================
# AGRICULTURE SECTION
# =========================================================

st.header("Agricultural Production")

crop_df = pd.DataFrame({
    "Crop": [
        "Sorghum",
        "Groundnuts",
        "Maize",
        "Sesame",
        "Millet"
    ],
    "Production Index": [95, 80, 75, 60, 55]
})

st.subheader("Major Crop Production")

crop_chart = px.bar(
    crop_df,
    x="Crop",
    y="Production Index",
    color="Crop",
    text="Production Index"
)

crop_chart.update_layout(height=500)

st.plotly_chart(crop_chart, use_container_width=True)

# =========================================================
# CLIMATE SECTION
# =========================================================

st.header("Climate and System Stressors")

climate_df = pd.DataFrame({
    "Stress Factor": [
        "Flooding",
        "Disease",
        "Water Competition",
        "Crop Damage",
        "Grazing Pressure"
    ],
    "Impact Level": [90, 75, 65, 80, 70]
})

st.subheader("Climate Impact Levels")

climate_chart = px.line(
    climate_df,
    x="Stress Factor",
    y="Impact Level",
    markers=True
)

climate_chart.update_layout(height=500)

st.plotly_chart(climate_chart, use_container_width=True)

# =========================================================
# COUNTY OVERVIEW
# =========================================================

st.header("County Overview")

county_df = pd.DataFrame({
    "County": [
        "Gogrial West",
        "Twic",
        "Gogrial East",
        "Tonj North",
        "Tonj South",
        "Tonj East"
    ],
    "Key Economic Activities": [
        "Livestock, Farming",
        "Livestock, Groundnuts",
        "Agriculture, Livestock",
        "Livestock, Sorghum",
        "Agriculture, Trade",
        "Pastoralism, Farming"
    ]
})

st.dataframe(county_df, use_container_width=True)

# =========================================================
# SUCCESS BOX
# =========================================================

st.markdown("""
<div class="success-box">
Dashboard loaded successfully
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Data Sources:

Warrap State Government

Ministry of Health

Education sector field updates

Humanitarian and regional assessments
""")
