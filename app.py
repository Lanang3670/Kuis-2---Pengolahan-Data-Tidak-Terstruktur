import streamlit as st
import cv2
import numpy as np
import io
from PIL import Image

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
        tint = st.sidebar.slider("Tint Warna (Cold ↔ Warm)", -100, 100, 0)

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
            sharpen,
            tint
        )

        edited_img = apply_filter(edited_img, filter_name)

        st.image(
            edited_img,
            channels="BGR",
            caption="Hasil Edit"
        )

        # ===== DOWNLOAD FOTO =====
        img_rgb = cv2.cvtColor(edited_img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)

        buf = io.BytesIO()
        pil_img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="⬇️ Download Foto",
            data=byte_im,
            file_name="hasil_edit.png",
            mime="image/png"
        )
