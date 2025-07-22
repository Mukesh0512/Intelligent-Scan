import cv2
import os

def capture_faces(user_id, user_name):
    # Directory to store captured face data
    face_dir = f"data/face_data/{user_id}_{user_name}"
    os.makedirs(face_dir, exist_ok=True)

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print("[INFO] Starting face capture...")
    count = 0

    while True:
        ret, img = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y + h, x:x + w]
            img_path = os.path.join(face_dir, f"{str(count)}.jpg")
            cv2.imwrite(img_path, face_img)

            # Draw rectangle on face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Capturing Faces [Press Q to Exit]', img)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
            break

    print("[INFO] Face capture completed.")
    cam.release()
    cv2.destroyAllWindows()

    return "success"
