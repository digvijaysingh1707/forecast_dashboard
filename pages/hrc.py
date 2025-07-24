import streamlit as st
import pandas as pd

# Load CSV with HRC predictions
df = pd.read_csv("data/hrc_pred_results_3M_till_Sep.csv")

# Get the latest non-NaN horizon_0 predicted price and corresponding MAPE
latest_row = df.dropna(subset=["horizon_0", "horizon_0_mape"]).iloc[-1]
month_str = pd.to_datetime(latest_row["ds"]).strftime("%b-%Y")
base_pred = latest_row["horizon_0"]
mape = latest_row["horizon_0_mape"]

# Create a 3:1 column layout (main=graph, side=metric)
main_col, side_col = st.columns([3, 1])

with main_col:
    st.subheader("Hot Rolled Coil (HRC) Mumbai Price Forecast")
    st.line_chart(df.set_index("ds")[["actual", "horizon_0"]])

with side_col:
    st.markdown(f"##### {month_str}")
    adj_pct = st.slider(
        "Adjust by MAPE (%)",
        min_value=-float(mape),
        max_value=float(mape),
        value=0.0,
        step=0.01,
        help=f"Adjust +/- up to the model's MAPE ({mape:.2f}%)",
    )
    adj_pred = base_pred * (1 + adj_pct / 100)
    st.metric(label="Predicted Price", value=f"₹{adj_pred:,.0f}")
    st.caption(f"Base: ₹{base_pred:,.0f} <br>MAPE: {mape:.2f}%", unsafe_allow_html=True)
