import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image

st.title("😊 AI Face Emotion Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)

    result = DeepFace.analyze(img_array, actions=['emotion'])
    emotion = result[0]['dominant_emotion']

    st.success(f"Detected Emotion: {emotion}")