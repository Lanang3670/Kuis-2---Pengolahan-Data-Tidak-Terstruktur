import cv2
import numpy as np

def apply_basic_edit(
    img,
    brightness,
    contrast,
    blur,
    negative,
    grayscale,
    sharpen,
    tint
):
    # Brightness & Contrast
    img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

    # Blur
    if blur > 0:
        img = cv2.GaussianBlur(img, (blur*2+1, blur*2+1), 0)

    # Negative
    if negative:
        img = cv2.bitwise_not(img)

    # Grayscale
    if grayscale:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Sharpen
    if sharpen:
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])
        img = cv2.filter2D(img, -1, kernel)

    # ===== TINT WARNA =====
    # tint: -100 (cold) → 0 → +100 (warm)
    if tint != 0:
        img = img.astype(np.int16)
        img[:, :, 0] -= tint   # Blue
        img[:, :, 2] += tint   # Red
        img = np.clip(img, 0, 255).astype(np.uint8)

    return img
