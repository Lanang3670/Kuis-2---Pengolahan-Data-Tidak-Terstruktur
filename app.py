import streamlit as st
import cv2
import numpy as np

from core.editor import apply_basic_edit
from core.filters import apply_filter


def main():
    st.title("📸 Aplikasi Edit Foto Sederhana")

    uploaded_file = st.file_uploader(
        "Upload gambar",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()),
            dtype=np.uint8
        )
        img = cv2.imdecode(file_bytes, 1)

        st.image(img, channels="BGR", caption="Gambar Asli")

        st.sidebar.header("Pengaturan Edit")

        brightness = st.sidebar.slider("Brightness", -100, 100, 0)
        contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
        blur = st.sidebar.slider("Blur", 0, 10, 0)
        negative = st.sidebar.checkbox("Negative")
        grayscale = st.sidebar.checkbox("Grayscale")
        sharpen = st.sidebar.checkbox("Sharpen")

        filter_name = st.sidebar.selectbox(
            "Filter",
            ["None", "Black & White", "Sepia", "Cool", "Warm"]
        )

        edited_img = apply_basic_edit(
            img,
            brightness,
            contrast,
            blur,
            negative,
            grayscale,
            sharpen
        )

        edited_img = apply_filter(edited_img, filter_name)

        st.image(
            edited_img,
            channels="BGR",
            caption="Hasil Edit"
        )
