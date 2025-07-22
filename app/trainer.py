import cv2
import numpy as np
from PIL import Image
import os

def train_model():
    data_path = 'data/face_data'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = []
    ids = []

    print("[INFO] Training model. Please wait...")

    for user_folder in os.listdir(data_path):
        user_id = int(user_folder.split("_")[0])  # Extract ID from folder name like 101_Mukesh
        user_path = os.path.join(data_path, user_folder)

        for image_name in os.listdir(user_path):
            image_path = os.path.join(user_path, image_name)
            gray_img = Image.open(image_path).convert('L')  # grayscale
            img_np = np.array(gray_img, 'uint8')

            detected_faces = detector.detectMultiScale(img_np)
            for (x, y, w, h) in detected_faces:
                faces.append(img_np[y:y + h, x:x + w])
                ids.append(user_id)

    if len(faces) == 0:
        return "[ERROR] No face data found. Please add users first."

    recognizer.train(faces, np.array(ids))
    os.makedirs("data/trained_model", exist_ok=True)
    recognizer.save('data/trained_model/trainer.yml')

    return "[INFO] Model training complete. Recognizer saved!"
