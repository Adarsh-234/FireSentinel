
import numpy as np
import rasterio
from tensorflow.keras.models import load_model

MODEL_PATH = "../models/unet_fire_model.h5"
model = load_model(MODEL_PATH)

def predict_fire(tif_file):
    with rasterio.open(tif_file) as src:
        img = src.read().astype(np.float32)
        img = np.moveaxis(img, 0, -1)
        img = img / 255.0

    pred = model.predict(np.expand_dims(img, axis=0))[0]
    binary_mask = (pred[:, :, 0] > 0.5).astype(np.uint8) * 255
    return binary_mask
