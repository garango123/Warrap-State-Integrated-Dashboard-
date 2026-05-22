import streamlit as st
import pandas as pd

st.set_page_config(
page_title="Warrap State Integrated Dashboard",
layout="wide"
)

=========================

HEADER

=========================

st.title("Warrap State Integrated Data Analytics Dashboard")

st.markdown("""
A comprehensive regional analytics platform providing insights into:

Population

Healthcare Infrastructure

Education Systems

Livestock Economy

Agriculture

Climate Impacts

County-Level Development Indicators
""")


=========================

POPULATION

=========================

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

=========================

HEALTHCARE SECTION

=========================

st.header("Healthcare Infrastructure")

st.markdown("""
Greater Warrap State currently has 48 officially integrated primary healthcare facilities operating within the regional healthcare service network.
""")

col1, col2, col3 = st.columns(3)

col1.metric("PHCCs", "21")
col2.metric("PHCUs", "27")
col3.metric("Referral Hospitals", "4")

st.subheader("Main Referral Hospitals")

hospital_df = pd.DataFrame({
"Hospital": [
"Kuajok State Hospital",
"Tonj Civil Hospital",
"Turalei Hospital",
"Marial Lou Hospital"
],
"Town": [
"Kuajok Town",
"Tonj Town",
"Turalei Town",
"Marial Lou Payam"
],
"County": [
"Gogrial West County",
"Tonj South County",
"Twic County",
"Tonj North County"
],
"Regional Role": [
"Main state referral hub",
"Southern regional referral center",
"Northern border referral coverage",
"Northwestern regional coverage"
]
})

st.dataframe(hospital_df, use_container_width=True)

=========================

EDUCATION SECTION

=========================

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
"Tomic HQRS"
]
})

st.dataframe(education_df, use_container_width=True)

st.subheader("Education Summary")

e1, e2, e3, e4 = st.columns(4)

e1.metric("Primary Schools", "1,286")
e2.metric("Secondary Schools", "86")
e3.metric("CEC Centers", "6")
e4.metric("TVET Centers", "3")

=========================

LIVESTOCK SECTION

=========================

st.header("Livestock Economy")

st.markdown("""
Livestock represents the primary store of both cultural and economic wealth in Warrap State.
""")

st.metric(
label="Estimated Cattle Population",
value="3 Million Head"
)

st.markdown("""

Livestock Importance

Source of cultural wealth

Dowry and marriage systems

Emergency financial reserve

Food security

Mobile economic assets


Seasonal Migration Patterns

Dry Season

Large cattle herds migrate toward Toic floodplains and swamp grazing areas in Gogrial and Twic.

Wet Season

Herds return to elevated settlement areas to avoid livestock diseases and support farming activities.
""")

=========================

AGRICULTURE SECTION

=========================

st.header("Agricultural Production")

st.markdown("""
Agriculture in Greater Warrap remains largely traditional,
rain-fed, and dependent on human labor.
""")

crop_df = pd.DataFrame({
"Crop": [
"Sorghum",
"Groundnuts",
"Millet",
"Sesame",
"Maize"
],
"Category": [
"Staple Crop",
"Cash Crop",
"Staple Crop",
"Intercrop",
"Household Crop"
],
"Description": [
"Dominant staple food crop",
"Major localized cash crop",
"Widely intercropped",
"Intercropped with sorghum",
"Consumed fresh near homes"
]
})

st.dataframe(crop_df, use_container_width=True)

st.markdown("""

Gender Roles in Agriculture

Women perform approximately 90% of active agricultural labor including:

Weeding

Harvesting

Crop processing


Men mainly engage in:

Livestock management

Heavy land clearing

Security activities
""")


=========================

CLIMATE & CHALLENGES

=========================

st.header("Climate and System Stressors")

st.markdown("""

Climate Shocks

Recurring flooding heavily affects:

Crop yields

Livestock survival

Household food security


Major livestock diseases include:

Anthrax

Rift Valley Fever


Resource-Based Conflict

Seasonal migration patterns occasionally trigger conflicts between:

Farmers

Pastoralist communities


Main causes include:

Crop trampling

Water competition

Grazing pressure
""")


=========================

COUNTY OVERVIEW

=========================

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

=========================

FOOTER

=========================

st.markdown("---")

st.caption("""
Data Sources:

Warrap State Government

Ministry of Health

Education sector field updates

Humanitarian and regional assessments
""")
Please, what can I put in the (requirements.txt) section in order to make this project or data analytics looks interactive, professional and engaging like these screenshots
