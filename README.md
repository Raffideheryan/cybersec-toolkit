# 🛠️ CyberSec Toolkit

A collection of small but powerful Python scripts (and one Ruby module) built for learning, practicing, and experimenting with cybersecurity techniques. From scanning networks to cracking hashes — everything you need to sharpen your offensive security skills in one place.

> ⚠️ **Educational use only.** Do **NOT** use these tools against any network, system, or application you do not own or have explicit permission to test.

---

## 📁 What's Inside?

| Script                         | Description                                                              |
|-------------------------------|--------------------------------------------------------------------------|
| `network_scanner.py`          | Scans local IP ranges and ports to find active hosts and services.      |
| `dir_enum.py`                 | Enumerates directories on a web server using a wordlist.                |
| `subdomain_finder.py`         | Brute-forces and discovers subdomains of a target domain.               |
| `ssh_bruteforce.py`           | Attempts SSH login using a list of passwords (via Paramiko).            |
| `hash_identifier.py`          | Identifies hash types based on their length and structure.              |
| `hash_cracker.py`             | Cracks known hashes using dictionary attacks (supports MD5).            |
| `log_analyzer.py`             | Parses logs and flags potentially suspicious activity.                  |
| `phishing_detector.py`        | Detects phishing emails based on keywords and suspicious links.         |
| `bruter.rb` (Metasploit)      | A custom Ruby Metasploit module template you can load and test.         |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. Some scripts may require extra libraries:

```bash
pip install requests paramiko

🔧 Usage
Each script can be run individually. Here are some examples:

Copy
Edit
# Scan the 192.168.1.x network
python3 network_scanner.py

# Run directory enumeration against a target
python3 dir_enum.py

# Brute-force SSH on a given host
python3 ssh_bruteforce.py
