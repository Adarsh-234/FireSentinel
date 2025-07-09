import streamlit as st

def show_gif(gif_path):
    with open(gif_path, "rb") as f:
        gif = f.read()
    st.image(gif, caption="Fire Spread Simulation", use_column_width=True)