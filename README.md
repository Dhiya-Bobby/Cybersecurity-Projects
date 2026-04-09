# 🔐 Cybersecurity Projects (Port Scanner + IDS)

This project includes two cybersecurity tools built using Python:
- Port Scanner with Banner Grabbing  
- Intrusion Detection System (IDS)

---

## 📌 Project Modules

---

## 🔍 1. Port Scanner with Banner Grabbing

A Python-based tool that scans open ports on a target system and identifies running services.

### 🚀 Features
- Detects open ports
- Performs banner grabbing
- Uses TCP socket programming

### ▶️ Usage & Example Output

python cyber.py

Enter target (IP or domain): scanme.nmap.org

Scanning target: scanme.nmap.org

[+] Port 22 is OPEN
    Service Info: SSH-2.0-OpenSSH

[+] Port 80 is OPEN
    Service Info: HTTP


## 🚨 2. Intrusion Detection System (IDS)

A Python-based tool that monitors network traffic in real-time and detects suspicious activity based on traffic patterns.

### 🚀 Features
- Captures live network packets
- Detects abnormal traffic behavior
- Generates alerts for potential threats
- Uses Scapy for packet sniffing

### ▶️ Usage & Example Output

python ids.py

Starting IDS... Press Ctrl+C to stop

Packet from 192.168.29.246 | Count: 1
Packet from 192.168.29.246 | Count: 2
Packet from 192.168.29.246 | Count: 3
Packet from 192.168.29.246 | Count: 10

⚠️ ALERT: Possible attack from 192.168.29.246
