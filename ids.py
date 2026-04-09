from scapy.all import sniff

ip_count = {}

def detect_packet(packet):
    if packet.haslayer("IP"):
        ip = packet["IP"].src

        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

        print(f"Packet from {ip} | Count: {ip_count[ip]}")

        if ip_count[ip] > 10:
            print(f"⚠️ ALERT: Possible attack from {ip}")

print("Starting IDS... Press Ctrl+C to stop")
sniff(prn=detect_packet, store=0)