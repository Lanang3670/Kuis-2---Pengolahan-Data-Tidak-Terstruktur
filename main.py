import streamlit as st
from app import main

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
st.set_page_config(page_title="Photo Editor Pro", page_icon="📸", layout="centered")
st.title("📸 Web Photo Editor Pro")
st.write("Untuk memenuhi kuis 2")

uploaded_file = st.file_uploader("Upload Foto", type=["jpg", "png", "jpeg"])

# ===== FILTER FUNCTION =====
def apply_filter(img, filter_name):
    if filter_name == "None":
        return img

    if filter_name == "Vintage":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(img, kernel)

    if filter_name == "Cool":
        img[:, :, 0] = np.clip(img[:, :, 0] + 40, 0, 255)
        return img

    if filter_name == "Warm":
        img[:, :, 2] = np.clip(img[:, :, 2] + 40, 0, 255)
        return img

    if filter_name == "Dramatic":
        return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

    if filter_name == "Black & White":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    if filter_name == "Sepia":
        kernel = np.array([[0.393, 0.769, 0.189],
                           [0.349, 0.686, 0.168],
                           [0.272, 0.534, 0.131]])
        return cv2.transform(img, kernel)

    if filter_name == "Cyberpunk":
        img[:,:,0] = np.clip(img[:,:,0] * 1.2, 0, 255)
        img[:,:,2] = np.clip(img[:,:,2] * 1.3, 0, 255)
        return img

    return img

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original", use_column_width=True)

    st.sidebar.header("🛠 Editing Tools")
    

    # BASIC
    brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast = st.sidebar.slider("Contrast", 1.0, 3.0, 1.0)
    blur = st.sidebar.slider("Blur", 0, 20, 0)
    negative = st.sidebar.checkbox("Negative")
    grayscale = st.sidebar.checkbox("Grayscale")
    sharpen = st.sidebar.checkbox("Sharpen")

    # FILTER
    st.sidebar.header("🎨 Filters")
    filter_name = st.sidebar.selectbox("Choose Filter",
        ["None", "Vintage", "Cool", "Warm", "Dramatic", "Black & White", "Sepia", "Cyberpunk"]
    )

    # Apply Filter
    img = apply_filter(img, filter_name)

    # Apply basic edits
    if grayscale:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    if brightness != 0:
        img = cv2.convertScaleAbs(img, alpha=1, beta=brightness)

    if contrast != 1:
        img = cv2.convertScaleAbs(img, alpha=contrast, beta=0)

    if blur > 0:
        img = cv2.GaussianBlur(img, (blur*2+1, blur*2+1), 0)

    if negative:
        img = cv2.bitwise_not(img)

    if sharpen:
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        img = cv2.filter2D(img, -1, kernel)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    edited = Image.fromarray(img)

    with col2:
        st.image(edited, caption="Edited", use_column_width=True)
     st.sidebar.header ("Convolutin Filter")
     conv = st.sidebar.selectbox("filter Type")

    st.download_button("📥 Download Image", edited.tobytes(), "edited.png")
>>>>>>> c754aab (main)
