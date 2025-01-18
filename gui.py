import customtkinter as ctk
import cv2
import {% load mediapipe_tags %} as mp
import psutil
import os
import threading
import time

# Initialize GUI Theme
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

# Face Recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascades_frontalface_default.xml")

# Hand Gesture Recognition
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Security & Monitoring
AUTHORIZED_USERS = ["user1", "admin"]  

# GUI App
class DesktopAssistant(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis Desktop Assistant")
        self.geometry("600x500")

        # Title Label
        self.label = ctk.CTkLabel(self, text="Aquarius AI Assistant", font=("Robot", 24, "bold"))
        self.label.pack(pady=20)

        # Animated Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self, width=250)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Buttons with hover effects
        self.monitor_btn = ctk.CTkButton(self, text="🖥 Monitor System", command=self.monitor_system, width=250, font=("Arial", 14), fg_color="#1E90FF", hover_color="#4169E1")
        self.monitor_btn.pack(pady=10)

        self.recognize_btn = ctk.CTkButton(self, text="📷 Face & Gesture Recognition", command=self.recognize_face_and_gestures, width=250, font=("Arial", 14), fg_color="#32CD32", hover_color="#228B22")
        self.recognize_btn.pack(pady=10)

        self.security_btn = ctk.CTkButton(self, text="🔒 Security Check", command=self.detect_unauthorized_access, width=250, font=("Arial", 14), fg_color="#FF4500", hover_color="#B22222")
        self.security_btn.pack(pady=10)

        self.quit_btn = ctk.CTkButton(self, text="❌ Exit", command=self.quit, width=250, fg_color="red", font=("Arial", 14, "bold"))
        self.quit_btn.pack(pady=20)

    def animate_progress(self):
        for i in range(100):
            time.sleep(0.02)
            self.progress_bar.set(i / 100)
        self.progress_bar.set(0)

    def monitor_system(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        battery = psutil.sensors_battery()

        report = f"""
        🔥 CPU Usage: {cpu_usage}%
        🏗 Memory Usage: {memory.percent}%
        🔋 Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}
        """
        ctk.CTkMessagebox(title="System Monitoring", message=report)

        # Run progress animation
        threading.Thread(target=self.animate_progress).start()

    def detect_unauthorized_access(self):
        users = os.popen("who").read()
        unauthorized_users = [user for user in users.split("\n") if user and user.split()[0] not in AUTHORIZED_USERS]

        if unauthorized_users:
            ctk.CTkMessagebox(title="⚠️ Security Alert", message="Unauthorized Access Detected!")
            os.system("shutdown -l")
        else:
            ctk.CTkMessagebox(title="✅ Security Check", message="System Secure. No Unauthorized Users.")

    def recognize_face_and_gestures(self):
        thread = threading.Thread(target=self._run_face_and_gesture_recognition)
        thread.start()

    def _run_face_and_gesture_recognition(self):
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Face & Gesture Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

# Run GUI
if __name__ == "__main__":
    app = DesktopAssistant()
    app.mainloop()
