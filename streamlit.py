import streamlit as st
from utils.predict import run_unet_prediction
from utils.utils import run_fire_simulation

import os
st.set_page_config(page_title="🔥fireSentinal",layout="wide")
st.title("🔥fireSentinal")
st.markdown("predict and visualize fire spread using satellite imagery and fire simulation models")

#upload_section
uploaded_file = st.file_uploader("📤 Upload GeoTIFF Raster Input", type=["tif", "tiff"])
model_path = "model/unet_model.h5"

if uploaded_file is not None:
    with open("data/input.tif","wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

        
