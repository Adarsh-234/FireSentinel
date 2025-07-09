# 🔥 FireSentinel – Forest Fire Prediction and Simulation

FireSentinel is an AI-powered project that predicts and simulates the spread of forest fires using U-NET (deep learning) and Cellular Automata. It includes a user-friendly Streamlit dashboard for uploading satellite GeoTIFF images and visualizing animated fire spread over time.

---

## 🚀 Features

- 📍 **Fire Risk Prediction** using U-NET
- 🔥 **Fire Spread Simulation** using Cellular Automata
- 🖼️ **Animated Output** (.GIF)
- 🌐 **Streamlit Dashboard** for real-time interaction
- 🌍 Works with 30m resolution raster data (GeoTIFF)

---

## 🧠 Tech Stack

- **Python 3.10**
- **TensorFlow / Keras**
- **NumPy, Rasterio, Pillow, OpenCV**
- **Streamlit** for the web dashboard
- **Data Sources**: Bhuvan, Bhoonidhi, IMD, VIIRS-SNPP

---

## 📁 Project Structure

FireSentinel/
├── app.py # Streamlit dashboard
├── requirements.txt # Python dependencies
├── model/
│ └── unet_model.h5 # Trained U-NET model
├── data/
│ └── input.tif # Uploaded GeoTIFF raster
├── output/
│ └── fire_simulation.gif # Simulated fire spread animation
└── utils/
├── predict.py # U-NET prediction logic
└── simulate.py # Cellular Automata simulation
