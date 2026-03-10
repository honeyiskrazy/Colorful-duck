import streamlit as st
from PIL import Image
import numpy as np

st.title("🦆 Duck Color Tinter")

heart_colors = {
    "❤️ Red":        (255, 0,   0),
    "🧡 Orange":     (255, 165, 0),
    "💛 Yellow":     (255, 255, 0),
    "💚 Green":      (0,   200, 0),
    "🩵 Light Blue": (100, 210, 255),
    "💙 Blue":       (0,   0,   255),
}

choice = st.radio("Pick a heart color:", list(heart_colors.keys()), horizontal=True)

img = Image.open("colorful_duck.png").convert("RGB")
r, g, b = heart_colors[choice]

arr = np.array(img).astype(float)
arr[..., 0] = np.clip(arr[..., 0] * r / 255, 0, 255)
arr[..., 1] = np.clip(arr[..., 1] * g / 255, 0, 255)
arr[..., 2] = np.clip(arr[..., 2] * b / 255, 0, 255)

result = Image.fromarray(arr.astype(np.uint8))
st.image(result, caption=f"{choice} Duck", use_column_width=True)
