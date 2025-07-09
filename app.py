import streamlit as st
from predict import predict_fire
from simulate import simulate_fire_spread
from visualize import show_gif

st.set_page_config(page_title="🔥 FireSentinel Dashboard", layout="wide")
st.title("🔥 FireSentinel Forest Fire Prediction & Simulation")

uploaded_file = st.file_uploader("Upload GeoTIFF Input Stack (.tif)", type=["tif"])
sim_hours = st.selectbox("Simulate spread over (hours):", [1, 2, 3, 6, 12])

if uploaded_file:
    st.success("Input received. Running model prediction...")
    pred_output = predict_fire(uploaded_file)
    st.image(pred_output, caption="Predicted Fire Zones")

    st.success("Running Cellular Automata Simulation...")
    sim_path = simulate_fire_spread(pred_output, sim_hours)
    show_gif(sim_path)