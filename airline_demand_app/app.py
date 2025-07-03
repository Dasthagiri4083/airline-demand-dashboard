# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import load_data, process_data

# ✅ Page configuration
st.set_page_config(page_title="Airline Demand Dashboard", layout="wide")
st.title("✈️ Airline Booking Market Demand Dashboard")
st.markdown("Analyze airline booking trends, price changes, and demand patterns across destinations in Australia.")

# ✅ Load Data with spinner
with st.spinner('Loading data...'):
    data = load_data()

# ✅ Check for empty data
if data.empty:
    st.warning("No data available. Please check the data source.")
    st.stop()

# ✅ Filters
destination = st.selectbox("✈️ Select Destination", sorted(data["destination"].unique()))
filtered_data = data[data["destination"] == destination]

# ✅ Process Data
insights = process_data(filtered_data)

# ✅ Display Charts
st.subheader("📈 Demand Over Time")
fig1 = px.line(filtered_data, x="date", y="demand", title=f"Demand Trend for {destination}")
st.plotly_chart(fig1)

# ✅ Show Metrics
col1, col2 = st.columns(2)
with col1:
    most_popular_route = insights["popular_routes"].iloc[0]
    st.metric("Most Popular Route", f"{most_popular_route['origin']} → {most_popular_route['destination']}")
with col2:
    top_peak_day = insights["peak_days"].iloc[0]
    st.metric("Highest Demand Date", f"{top_peak_day['date']}")

# ✅ Show Tables
st.subheader("📊 Top 5 Popular Routes")
st.dataframe(insights["popular_routes"])

st.subheader("📅 Top 5 High-Demand Days")
st.dataframe(insights["peak_days"])
