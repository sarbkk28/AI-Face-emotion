import streamlit as st
import cv2
import numpy as np

st.title("😊 AI Face Emotion Detection")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Image")

    # TEMP EMOTION OUTPUT (for demo)
    st.success("Emotion: Happy 😊")
