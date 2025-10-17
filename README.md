# WinFetch

A simple, dependency-free, Neofetch-like system information tool for Windows, written in pure Python.

## About The Project

WinFetch is a lightweight command-line script that displays essential system information alongside a customizable ASCII logo. It's designed for users who want a quick overview of their system specs directly in the terminal without installing any external Python libraries or complex software.

The entire script relies on built-in Windows command-line tools (`wmic` and `systeminfo`) and standard Python libraries, making it incredibly portable and easy to run.

## Features

- **Zero External Dependencies:** Runs on any modern Windows system with Python 3 installed. No `pip install` required!
- **Essential Information:** Displays key system specs at a glance:
  - User & Hostname
  - Operating System Version
  - CPU Model
  - GPU Model
  - System Uptime
  - Memory (RAM) Usage
- **Colorful Output:** Uses ANSI escape codes for a clean, color-coded display.
- **Lightweight & Fast:** Gets the information you need quickly without any overhead.
- **Easily Customizable:** Simple to change the ASCII logo and colors by editing the script directly.

## Requirements

- **Operating System:** Windows 7, 8, 10, or 11.
- **Python:** Python 3.x installed and added to your system's PATH.
- **Terminal:** A terminal that supports ANSI colors.
  - **Recommended:** Windows Terminal, PowerShell, Git Bash.
  - _Note: The legacy `cmd.exe` may not display colors correctly._

## Getting Started

### Installation

No installation is needed! Simply download or clone the script.

1.  **Download the script:**

    - Save the code into a file named `winfetch.py`.

    OR

2.  **Clone the repository (if it were in one):**
    ```bash
    git clone https://github.com/Krasper707/winfetch.git
    cd winfetch
    ```

### Usage

1.  Open your preferred terminal (e.g., Windows Terminal).
2.  Navigate to the directory where you saved `winfetch.py`.
    ```bash
    cd path\to\your\script
    ```
3.  Run the script using Python:
    ```bash
    python winfetch.py
    ```

## Customization

You can easily modify the script to your liking.

### Changing the Logo

1.  Open `winfetch.py` in a text editor.
2.  Find the `logo` list inside the `main()` function.
3.  Replace the strings in the list with your own ASCII art. Ensure each line of your art is a separate string in the list.

**Example:**

```python
# Before
logo = [
    "WW  WW  II  NN  NN",
    "WW  WW  II  NNN NN",
    "WW W WW II  NN NNN",
    " YYYY   II  NN  NN",
]

# After
logo = [
    "+-----------------+",
    "|   My Custom     |",
    "|      Logo       |",
    "+-----------------+",
]
```

### Changing the Colors

1.  Open `winfetch.py`.
2.  Find the color variables at the top of the display logic section:
    ```python
    C_BLUE = "\033[94m"
    C_CYAN = "\033[96m"
    C_RESET = "\033[0m"
    ```
3.  You can change these values using different [ANSI escape codes](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797) to match your terminal's theme. For example, `\033[91m` for red or `\033[92m` for green.

## How It Works

This script avoids complex Windows APIs and external libraries by acting as a wrapper for built-in system commands:

- **`wmic` (Windows Management Instrumentation Command-line):** Used to query detailed hardware information such as the OS caption, CPU name, GPU name, and memory stats. The script runs `wmic` in a subprocess and parses its text output.
- **`systeminfo`:** Used to find the "System Boot Time," which provides a simple way to display system uptime without complex calculations.

The `subprocess` module in Python executes these commands, captures their output, and a bit of string manipulation and regular expressions extract the exact information needed.

## License

Distributed under the MIT License. See `LICENSE` for more information.

