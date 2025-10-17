import subprocess
import os
import re

def get_wmic_output(command):
    """Runs a WMIC command and returns its cleaned output."""
    try:

        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
        result = subprocess.run(
            f"wmic {command}",
            capture_output=True,
            text=True,
            check=True,
            startupinfo=si
        )
        # WMIC output can be messy, split by lines and strip whitespace
        lines = [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]
        # The second line is usually the value we want
        return lines[1] if len(lines) > 1 else "N/A"
    except (subprocess.CalledProcessError, FileNotFoundError, IndexError):
        return "N/A"

def get_uptime():
    """Gets system uptime (less precise but no-deps way)."""
    try:
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
        output = subprocess.check_output(['systeminfo'], text=True, startupinfo=si)
        match = re.search(r"System Boot Time:\s+(.*)", output)
        if match:
            # This is a very basic representation of uptime
            return match.group(1).strip()
        return "N/A"
    except Exception:
        return "N/A"

def main():
    """Main function to gather and print system info."""
    logo = [
        "WW  WW  II  NN  NN",
        "WW  WW  II  NNN NN",
        "WW W WW II  NN NNN",
        " YYYY   II  NN  NN",
    ]
    
    user = os.getenv("USERNAME", "N/A")
    hostname = os.getenv("COMPUTERNAME", "N/A")

    info = {
        "User@Host": f"{user}@{hostname}",
        "OS": get_wmic_output("os get Caption"),
        "CPU": get_wmic_output("cpu get Name"),
        "GPU": get_wmic_output("path win32_videocontroller get name"),
        "Uptime": get_uptime(),
    }
    
    total_mem_kb = int(get_wmic_output("OS get TotalVisibleMemorySize"))
    free_mem_kb = int(get_wmic_output("OS get FreePhysicalMemory"))
    total_mem_gb = round(total_mem_kb / 1024 / 1024, 1)
    used_mem_gb = round((total_mem_kb - free_mem_kb) / 1024 / 1024, 1)
    info["Memory"] = f"{used_mem_gb}GB / {total_mem_gb}GB"

    C_BLUE = "\033[94m"
    C_CYAN = "\033[96m"
    C_RESET = "\033[0m"
    
    info_lines = [f"{C_CYAN}{key}:{C_RESET} {value}" for key, value in info.items()]
    max_lines = max(len(logo), len(info_lines))

    print("\n") 
    
    for i in range(max_lines):
        logo_line = logo[i] if i < len(logo) else ""
        info_line = info_lines[i] if i < len(info_lines) else ""
        
        print(f"{C_BLUE}{logo_line:<20}{C_RESET} {info_line}")
    print("\n")
if __name__ == "__main__":
    main()