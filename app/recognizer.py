import cv2
import numpy as np
import os
from datetime import datetime
from app.attendance import mark_attendance

def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    model_path = 'data/trained_model/trainer.yml'

    if not os.path.exists(model_path):
        print("[ERROR] No trained model found. Please train the model first.")
        return "Trained model not found"

    recognizer.read(model_path)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    label_dict = {}
    for folder in os.listdir("data/face_data"):
        parts = folder.split('_')
        if len(parts) == 2:
            label_dict[int(parts[0])] = parts[1]

    cam = cv2.VideoCapture(0)

    print("[INFO] Starting face recognition. Press 'q' to exit.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[ERROR] Failed to grab frame from camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)

            if conf < 50:
                name = label_dict.get(id_, "Unknown")
                mark_attendance(id_, name)
                label = f"{name} ({int(conf)}%)"
                color = (0, 255, 0)
            else:
                label = "Unknown"
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Face Recognition - Intelligent Scan", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    return "Recognition Complete ✅"


