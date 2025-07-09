import numpy as np
import cv2
import os

def simulate_fire_spread(binary_mask, hours):
    fire_map = binary_mask.copy()
    output_frames = []

    for step in range(hours):
        fire_map = spread_step(fire_map)
        frame = cv2.cvtColor(fire_map, cv2.COLOR_GRAY2BGR)
        output_frames.append(frame)

    out_path = f"../output/animations/simulation_{hours}h.gif"
    make_gif(output_frames, out_path)
    return out_path

def spread_step(mask):
    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])
    neighbors = cv2.filter2D(mask, -1, kernel)
    spread = (neighbors > 255).astype(np.uint8) * 255
    return np.clip(mask + spread, 0, 255)

def make_gif(frames, path):
    import imageio
    imageio.mimsave(path, frames, duration=0.5)