import pyautogui
import time
import threading
import keyboard
import pystray
from PIL import Image, ImageDraw
from datetime import datetime

# Configuration
click_sequence = [
    {"point": (48, 16), "button": "right"},
    {"point": (68, 57), "button": "left"},
    # {"point": (1034, 825), "button": "left"},
    # {"point": (1519, 905), "button": "left"},
]

CLICK_DELAY = 0.1
LOOP_DELAY = 0.5

running = False
stop_event = threading.Event()

def log_event(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")

def perform_click_sequence():
    for step in click_sequence:
        x, y = step["point"]
        btn = step["button"]
        if btn == "right":
            pyautogui.rightClick(x=x, y=y)
            log_event(f"Right-clicked at ({x}, {y})")
        else:
            pyautogui.click(x=x, y=y)
            log_event(f"Left-clicked at ({x}, {y})")
        time.sleep(CLICK_DELAY)

def automation_loop():
    log_event("Automation starting in 5 seconds...")
    time.sleep(LOOP_DELAY)
    while not stop_event.is_set():
        perform_click_sequence()
        time.sleep(LOOP_DELAY)

def toggle_automation():
    global running
    if not running:
        log_event("Automation started. Press Ctrl + Alt + S again to stop.")
        running = True
        stop_event.clear()
        threading.Thread(target=automation_loop, daemon=True).start()
    else:
        running = False
        stop_event.set()
        log_event("Automation stopped.")

# Register keyboard shortcut
keyboard.add_hotkey('ctrl+alt+s', toggle_automation)

# --- System Tray Section ---

def create_image():
    """Generate a simple icon for the tray"""
    img = Image.new('RGB', (64, 64), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rectangle((16, 16, 48, 48), fill=(0, 120, 215))
    return img

def on_tray_start(icon, item):
    toggle_automation()

def on_tray_stop(icon, item):
    global running
    running = False
    stop_event.set()
    log_event("Automation manually stopped from tray.")

def on_tray_exit(icon, item):
    global running
    running = False
    stop_event.set()
    icon.stop()
    log_event("Application exited.")

icon = pystray.Icon(
    "TapAutomation",
    create_image(),
    "Click Automation Tool",
    menu=pystray.Menu(
        pystray.MenuItem("Start / Stop (Ctrl+Alt+S)", on_tray_start),
        pystray.MenuItem("Stop Now", on_tray_stop),
        pystray.MenuItem("Exit", on_tray_exit)
    )
)

def run_tray():
    log_event("System ready. Use system tray or Ctrl+Alt+S.")
    icon.run()

if __name__ == "__main__":
    run_tray()
