import cv2
import numpy as np

def extract_steg_message(image_path):
    try:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None or img.size == 0:
            raise ValueError("Image is empty or not readable.")

        binary_message = np.bitwise_and(img.flatten(), 1)
        byte_chunks = [
            binary_message[i:i + 8] for i in range(0, len(binary_message), 8)
        ]

        byte_list = []
        for byte in byte_chunks:
            byte_value = int("".join(map(str, byte)), 2)
            byte_list.append(byte_value)

        hidden_message = ''.join([f'{b:02x}' for b in byte_list])

        return hidden_message
    except Exception as e:
        print(f"Error extracting steg message: {e}")
        return None
