#!/usr/bin/env python3
# Tunnel Manager - Cloudflare, SSH, Ngrok tunnels
# Author: xspeen

import subprocess
import threading
import time
import re
import os
import requests

class TunnelManager:
    def __init__(self, port=8080):
        self.port = port
        self.process = None
        self.public_url = None

    def start_cloudflare(self):
        """Start Cloudflare tunnel"""
        print("[*] Starting Cloudflare tunnel...")

        # Check if cloudflared is installed
        if not self._check_command('cloudflared'):
            print("[!] cloudflared not found. Installing...")
            self._install_cloudflared()

        try:
            self.process = subprocess.Popen(
                ['cloudflared', 'tunnel', '--url', f'http://localhost:{self.port}'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Wait for URL
            timeout = 30
            start_time = time.time()
            while time.time() - start_time < timeout:
                line = self.process.stderr.readline()
                if line:
                    match = re.search(r'https://[a-zA-Z0-9.-]+\.trycloudflare\.com', line)
                    if match:
                        self.public_url = match.group()
                        print(f"[+] Cloudflare tunnel active: {self.public_url}")
                        return self.public_url
                time.sleep(0.5)

            print("[!] Could not get Cloudflare URL")
            return None

        except Exception as e:
            print(f"[!] Cloudflare error: {e}")
            return None

    def start_ssh_serveo(self):
        """Start SSH tunnel via Serveo"""
        print("[*] Starting SSH tunnel via Serveo...")

        try:
            self.process = subprocess.Popen(
                ['ssh', '-R', '80:localhost:' + str(self.port), 'serveo.net'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Try to extract URL
            timeout = 20
            start_time = time.time()
            while time.time() - start_time < timeout:
                line = self.process.stderr.readline()
                if line:
                    match = re.search(r'https://[a-zA-Z0-9.-]+\.serveo\.net', line)
                    if match:
                        self.public_url = match.group()
                        print(f"[+] Serveo tunnel active: {self.public_url}")
                        return self.public_url
                time.sleep(0.5)

            print("[!] Could not get Serveo URL")
            return None

        except Exception as e:
            print(f"[!] SSH tunnel error: {e}")
            print("[!] Alternative: Run 'ssh -R 80:localhost:{self.port} serveo.net' manually")
            return None

    def start_ngrok(self, auth_token=None):
        """Start ngrok tunnel"""
        print("[*] Starting ngrok tunnel...")

        if auth_token:
            subprocess.run(['ngrok', 'config', 'add-authtoken', auth_token], capture_output=True)

        try:
            self.process = subprocess.Popen(
                ['ngrok', 'http', str(self.port), '--log=stdout'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Wait for tunnel to start
            time.sleep(3)

            # Get URL from ngrok API
            try:
                response = requests.get('http://localhost:4040/api/tunnels')
                if response.status_code == 200:
                    tunnels = response.json()
                    for tunnel in tunnels.get('tunnels', []):
                        if tunnel.get('proto') == 'https':
                            self.public_url = tunnel.get('public_url')
                            print(f"[+] ngrok tunnel active: {self.public_url}")
                            return self.public_url
            except:
                pass

            print("[!] Could not get ngrok URL")
            return None

        except Exception as e:
            print(f"[!] ngrok error: {e}")
            return None

    def start_localhost(self):
        """Just return local URL"""
        self.public_url = f"http://localhost:{self.port}"
        print(f"[+] Local server: {self.public_url}")
        return self.public_url

    def stop(self):
        """Stop the tunnel process"""
        if self.process:
            self.process.terminate()
            self.process = None
            print("[*] Tunnel stopped")

    def _check_command(self, cmd):
        """Check if command exists"""
        try:
            subprocess.run([cmd, '--version'], capture_output=True, check=True)
            return True
        except:
            return False

    def _install_cloudflared(self):
        """Install cloudflared based on OS"""
        import platform
        system = platform.system().lower()

        if system == 'linux':
            # Check for termux
            if os.path.exists('/data/data/com.termux/files/usr'):
                subprocess.run(['pkg', 'install', 'cloudflared', '-y'], capture_output=True)
            else:
                # Linux download
                url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
                subprocess.run(['wget', '-q', url, '-O', '/usr/local/bin/cloudflared'], capture_output=True)
                subprocess.run(['chmod', '+x', '/usr/local/bin/cloudflared'], capture_output=True)
        elif system == 'darwin':
            subprocess.run(['brew', 'install', 'cloudflared'], capture_output=True)
        else:
            print("[!] Please install cloudflared manually")
