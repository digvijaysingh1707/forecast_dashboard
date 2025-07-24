import streamlit as st
import pandas as pd

st.set_page_config(page_title="Steel Commodities Dashboard", layout="wide")

# Header
st.image("assets/images/banner.jpeg", use_column_width=True)
st.title("ML Forecast Report for Steel Commodities")

# Executive Forecast Table
summary_df = pd.read_csv("data/steel_forecast_summary.csv")
st.subheader("Executive Summary: Monthly Price Forecast")
st.dataframe(summary_df)

st.page_link("pages/hrc.py", label="View HRC Forecast and Analysis →")
