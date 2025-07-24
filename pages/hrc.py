import streamlit as st
import pandas as pd

st.header("Hot Rolled Coil (HRC) Forecast Analysis")

df_3m = pd.read_csv("data/hrc_pred_results_3M_till_Sep.csv")
# Plot actual vs. predictions
st.line_chart(df_3m[["ds", "actual", "horizon_0"]].set_index("ds"))

st.subheader("Forecast Accuracy Metrics")
st.dataframe(df_3m[["ds", "horizon_0", "horizon_0_mae", "horizon_0_mape"]])
