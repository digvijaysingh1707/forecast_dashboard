import streamlit as st
import pandas as pd

# Load prediction data
df_hrc = pd.read_csv("data/hrc_pred_results_3M_till_Sep.csv")

# Get last available non-NaN row (latest month with prediction)
last_row = df_hrc.dropna(subset=["horizon_0", "horizon_0_mape"]).iloc[-1]
month = pd.to_datetime(last_row["ds"]).strftime("%b-%y")
pred_price = last_row["horizon_0"]
mape = last_row["horizon_0_mape"]  # e.g., 3.39 for 3.39%

# Set up layout: single column for this widget (can be in a sidebar or any column structure you use)
st.markdown(f"### {month}")
adj_pct = st.slider(
    "Adjust by MAPE (%)",
    min_value=-float(mape),
    max_value=float(mape),
    value=0.0,
    step=0.01,
    help=f"Adjust predicted price by ±MAPE ({mape:.2f}%)",
)

# Calculate adjusted prediction
adj_pred = pred_price * (1 + adj_pct / 100)
st.metric(label="Adjusted Predicted HRC Price", value=f"₹{adj_pred:,.0f}")

# Optionally, show the base predicted price for transparency
st.caption(f"Base predicted price: ₹{pred_price:,.0f} (MAPE: {mape:.2f}%)")
