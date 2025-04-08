import cv2
import face_recognition

class NovaVision:
    def __init__(self):
        self.known_faces = self._load_known_faces()

    def recognize_face(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            return "👋 Welcome back, Commander."
        return "⚠️ Unauthorized access detected!"