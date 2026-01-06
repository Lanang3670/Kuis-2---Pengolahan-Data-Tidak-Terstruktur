import cv2
import numpy as np

def apply_filter(img, filter_name):
    if filter_name == "None":
        return img

    if filter_name == "Black & White":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    if filter_name == "Sepia":
        kernel = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])
        return cv2.transform(img, kernel)

    if filter_name == "Cool":
        img[:, :, 0] = np.clip(img[:, :, 0] + 40, 0, 255)
        return img

    if filter_name == "Warm":
        img[:, :, 2] = np.clip(img[:, :, 2] + 40, 0, 255)
        return img

    return img
