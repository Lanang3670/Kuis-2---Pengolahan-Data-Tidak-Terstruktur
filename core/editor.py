import cv2
import numpy as np

def apply_basic_edit(
    img,
    brightness,
    contrast,
    blur,
    negative,
    grayscale,
    sharpen
):
    img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

    if blur > 0:
        img = cv2.GaussianBlur(img, (blur*2+1, blur*2+1), 0)

    if negative:
        img = cv2.bitwise_not(img)

    if grayscale:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    if sharpen:
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)

    return img
