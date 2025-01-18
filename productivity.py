from cryptography.fernet import Fernet
import pyautogui
import time
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Generate or load encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

generate_key()  # Run this once to generate the key
key = load_key()
cipher = Fernet(key)

def encrypt_text(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Example usage
note = "This is a secret message."
encrypted_note = encrypt_text(note)
print(f"🔒 Encrypted: {encrypted_note}")

decrypted_note = decrypt_text(encrypted_note)
print(f"🔓 Decrypted: {decrypted_note}")



def open_notepad():
    """
    Opens Notepad using system commands.
    """
    pyautogui.hotkey("win", "r")  # Open Run
    time.sleep(1)
    pyautogui.write("notepad")  # Type "notepad"
    pyautogui.press("enter")  # Press Enter
    time.sleep(2)
    pyautogui.write("Hello, this is your assistant!")  # Type a message
    pyautogui.press("enter")

open_notepad()


# Load credentials
SERVICE_ACCOUNT_FILE = "credentials.json"  # Downloaded from Google Cloud
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)

def get_events():
    """
    Fetches upcoming Google Calendar events.
    """
    events_result = service.events().list(calendarId='primary', maxResults=5).execute()
    events = events_result.get("items", [])
    if not events:
        return "No upcoming events found."
    
    event_list = []
    for event in events:
        event_list.append(f"{event['summary']} at {event.get('start', {}).get('dateTime', 'Unknown time')}")
    
    return "\n".join(event_list)

print("Upcoming Events:\n", get_events())

class ProductivityTracker:
    def __init__(self):
        self.tasks_completed = 0

    def complete_task(self):
        self.tasks_completed += 1
        print(f"✅ Task completed! Total: {self.tasks_completed}")
        self.reward_user()

    def reward_user(self):
        rewards = {5: "🎉 Great job! 5 tasks completed!", 10: "🏆 Amazing! 10 tasks done!", 20: "🔥 You're unstoppable!"}
        if self.tasks_completed in rewards:
            print(rewards[self.tasks_completed])

tracker = ProductivityTracker()

# Example usage
tracker.complete_task()  # Call this when a task is completed
tracker.complete_task()
tracker.complete_task()
tracker.complete_task()
tracker.complete_task()  # Should trigger a reward



