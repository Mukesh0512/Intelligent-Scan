# face_detector.py
import face_recognition
import cv2

# Load an image with a face
image = face_recognition.load_image_file("app/test.jpg")

# Find all face locations
face_locations = face_recognition.face_locations(image)

print(f"Found {len(face_locations)} face(s) in the image.")

# Draw rectangles around faces using OpenCV (optional display)
for top, right, bottom, left in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Convert to BGR for OpenCV display
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow("Detected Faces", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
