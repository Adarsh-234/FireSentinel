import rasterio
import numpy as np
from tensorflow.keras.models
import load_model
from PIL import image

def run_unet_prediction(tif_path,model_path):
      model =  load_model(model_path)

      with rasterio.open(tif_path)as src:
            img = src.read()
            img = np.moveaxis(img ,0 ,-1)

pil_img = Image.fromarray(img.astype(np.uint8))

pil_img_resized = pil_img.resize((256, 256) ,Image.BILINEAR)

img_resized = np.array(pil_img_resized)

img_resized = img_resized / 255.0

prediction = model.predict(np.expand_dims(img_resized , axis = 0))[0]

binary_mask = (prediction[:, :, 0] > 0.5).astype(np.uint8)

preview = Image.fromarray(binary_mask * 255)

return {"array":binary_mask , "preview": preview }
