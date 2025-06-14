from pathlib import Path

def is_suspicious(line):
    """Check if a log line is suspicious."""
    suspicious_keywords = ("404", "Failed password")
    return any(keyword in line for keyword in suspicious_keywords)

def analyze_log(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as log_file:
            for line_num, line in enumerate(log_file, start=1):
                if is_suspicious(line):
                    print(f"[!] Suspicious (line {line_num}): {line.strip()}")
    except FileNotFoundError:
        print(f"[!] Log file not found: {file_path}")
    except PermissionError:
        print(f"[!] Permission denied: {file_path}")

if __name__ == "__main__":
    log_input = input("[*] Enter the path to the log file: ").strip()
    log_path = Path(log_input)
    analyze_log(log_path)
