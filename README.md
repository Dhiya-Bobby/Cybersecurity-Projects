# 🔐 Cybersecurity Projects (Port Scanner + IDS)

This project is a collection of practical cybersecurity tools developed using Python. It includes a Port Scanner and a Real-Time Intrusion Detection System (IDS), demonstrating key concepts in network security and traffic analysis.

---

## 📌 Project Modules

### 🔍 1. Port Scanner with Banner Grabbing

A Python-based tool that scans open ports on a target system and identifies running services.

#### 🚀 Features
- Detects open ports on a target system
- Performs banner grabbing to identify services
- Uses TCP socket programming

#### ▶️ Usage
```bash
python cyber.py
📸 Example Output
[+] Port 22 is OPEN
    Service Info: SSH

[+] Port 80 is OPEN
    Service Info: HTTP
🚨 2. Intrusion Detection System (IDS)

A real-time network monitoring system that captures packets and detects suspicious activity using traffic patterns.

🚀 Features
Real-time packet sniffing
Detects abnormal traffic behavior
Generates alerts for potential threats
▶️ Usage
python ids.py
📸 Example Output
Packet from 192.168.x.x | Count: 10
⚠️ ALERT: Possible attack detected
🛠️ Technologies Used
Python
Socket Programming
Scapy (for packet sniffing)
⚙️ Requirements
Python 3.x

Scapy

pip install scapy
Npcap (required for Windows packet capture)
⚠️ Important Notes
Run IDS as Administrator
Ensure Npcap is installed
High network traffic may trigger alerts (basic detection logic)
Use only on authorized systems (ethical purposes only)
🚀 Future Improvements
Multithreaded port scanning
GUI-based interface
Advanced attack detection (DoS, SYN flood)
Logging and reporting system

 Author

Dhiya Bobby

