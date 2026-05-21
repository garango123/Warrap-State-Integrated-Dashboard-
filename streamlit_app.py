import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    layout="wide"
)

st.title("Warrap State Integrated Dashboard")

st.markdown("""
Welcome to the interactive dashboard for Warrap State, South Sudan.
""")

# Sample metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Population", "2.1M")

with col2:
    st.metric("GDP Growth", "4.5%")

with col3:
    st.metric("Literacy Rate", "37%")

# Sample chart
data = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024],
    "GDP": [2.1, 2.4, 2.8, 3.0, 3.5]
})

st.line_chart(data.set_index("Year"))

st.success("Dashboard is running successfully!")
