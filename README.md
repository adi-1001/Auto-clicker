
# Auto Clicker

Auto Clicker is a lightweight Python-based tool that automates mouse clicks at desired screen positions. It supports both **left** and **right** clicks, and works alongside a helper program called **Coordinate Checker** to determine the exact coordinates for automation.

## Features

- Simulates **left** and **right** mouse clicks
- Clicks at custom screen coordinates
- Toggle clicking using hotkeys (`Ctrl + Alt + S`)
- Simple and customizable Python code
- Includes a **Coordinate Checker** tool

## Requirements

Before running Auto Clicker, install the required Python packages:

```bash
pip install -r requirements.txt
Without installing the requirements, the program may only perform alternate clicking and not full functionality.

CoordinateChecker
Use the CoordinateChecker.py script to find the coordinates of the position you want to click.

Usage:
Run the script:

Press Ctrl + Alt + S to start logging your cursor position.

Press Ctrl + Alt + S again to stop logging.

Use the printed coordinates in the CoordinateChecker.py script.

Usage Instructions
Clone or download the project.

Install dependencies:

pip install -r requirements.txt

Open the auto_clicker.py file.

Inside the code, change the following:

click_position = (x, y) — your desired coordinates

click_type = 'left' or 'right'

Run the script:

python auto_clicker.py

Start/stop clicking with Ctrl + Alt + S.

Customization
You can edit the following in the source code:

click_position — coordinates of where to click

click_type — 'left' or 'right'

Click interval or duration (if implemented)

Disclaimer
Use this tool responsibly. Some applications, especially games, may prohibit the use of auto clickers. The developer is not liable for any misuse or violation of terms of service.

---

Let me know if you'd like me to create the `requirements.txt` file or give you a zipped project structure!

