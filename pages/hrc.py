import streamlit as st
import pandas as pd

# Load HRC prediction data
df = pd.read_csv("data/hrc_pred_results_3M_till_Sep.csv")

# Get latest available prediction and MAPE
latest_row = df.dropna(subset=["horizon_0", "horizon_0_mape"]).iloc[-1]
month_str = pd.to_datetime(latest_row["ds"]).strftime("%b-%Y")
base_pred = latest_row["horizon_0"]
mape = latest_row["horizon_0_mape"]

# Layout: 3:1 columns
main_col, side_col = st.columns([3, 1])

with main_col:
    st.subheader("Hot Rolled Coil (HRC) Mumbai Price Forecast")
    st.line_chart(df.set_index("ds")[["actual", "horizon_0"]])

with side_col:
    st.markdown(f"##### {month_str}")
    st.metric(label="Predicted Price", value=f"₹{base_pred:,.0f}")

    adj_pct = st.slider(
        "Adjust by MAPE (%)",
        min_value=-float(mape),
        max_value=float(mape),
        value=0.0,
        step=0.01,
        help=f"Adjust +/- up to the model's MAPE ({mape:.2f}%)",
    )
    adj_pred = base_pred * (1 + adj_pct / 100)
    st.markdown(f"**Adjusted Predicted Price:** ₹{adj_pred:,.0f}")
    st.caption(f"Base: ₹{base_pred:,.0f} &nbsp;&nbsp;|&nbsp; MAPE: {mape:.2f}%")
