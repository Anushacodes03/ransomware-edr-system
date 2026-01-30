import os
import time
import psutil
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from entropy_checker import calculate_entropy

# =======================
# PATH SETUP
# =======================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "incident_log.txt")

# =======================
# CONFIGURATION
# =======================
TIME_WINDOW = 10
FILE_THRESHOLD = 9
ENTROPY_THRESHOLD = 4.0


class RansomwareDetector(FileSystemEventHandler):

    def __init__(self):
        self.events = deque()
        self.suspicious_mode = False

    def on_modified(self, event):
        if event.is_directory:
            return

        current_time = time.time()
        self.events.append(current_time)

        while self.events and current_time - self.events[0] > TIME_WINDOW:
            self.events.popleft()

        print(f"[MODIFIED] {event.src_path}")

        # Phase 4: Behavior detection
        if len(self.events) >= FILE_THRESHOLD:
            self.suspicious_mode = True
            print("\n⚠️ Suspicious activity detected")

        # Phase 5: Entropy check
        if self.suspicious_mode:
            entropy = calculate_entropy(event.src_path)
            print(f"Entropy: {entropy:.2f}")

            if entropy >= ENTROPY_THRESHOLD:
                self.respond_to_attack(event.src_path, entropy)

    # =======================
    # AUTO PROCESS KILL (SIMULATION)
    # =======================
    def simulate_process_kill(self):

        print("\n🧠 Identifying suspicious process...")

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                name = proc.info['name']

                if name and ("python" in name.lower() or ".exe" in name.lower()):
                    print(f"🚫 Suspicious Process Found: {name}")
                    print(f"PID: {proc.info['pid']}")
                    print("✅ Action: PROCESS TERMINATED (SIMULATION)")

                    with open(LOG_FILE, "a", encoding="utf-8") as log:
                        log.write(f"Process Detected: {name}\n")
                        log.write(f"PID: {proc.info['pid']}\n")
                        log.write("Action: PROCESS TERMINATED (SIMULATION)\n")

                    break

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    # =======================
    # RESPONSE
    # =======================
    def respond_to_attack(self, file_path, entropy):

        print("\n🔥🔥 RANSOMWARE CONFIRMED 🔥🔥")
        print(f"File: {file_path}")
        print(f"Entropy: {entropy:.2f}")
        print("Immediate response required!")

        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write("\n============================\n")
            log.write("RANSOMWARE INCIDENT DETECTED\n")
            log.write(f"Time: {time.ctime()}\n")
            log.write(f"File: {file_path}\n")
            log.write(f"Entropy: {entropy:.2f}\n")

        # 🚨 AUTO RESPONSE
        self.simulate_process_kill()


# =======================
# START MONITORING
# =======================
def start_monitoring(path):
    event_handler = RansomwareDetector()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("🛡️ Ransomware Detection Engine Started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    folder_to_monitor = r"C:\ransomware_test"
    start_monitoring(folder_to_monitor)
