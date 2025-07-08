import rasterio
import numpy as np
from tensorflow.keras.models
import load_model
from PIL import image

def run_unet_prediction(tif_path,model_path):
      model =  load_model(model_path)

      with rasterio.open(tif_path)as src:
