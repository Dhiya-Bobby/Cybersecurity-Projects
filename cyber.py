import socket

target = input("Enter target (IP or domain): ")
ports = range(20, 100)

print(f"\nScanning target: {target}\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        
        try:
            banner = s.recv(1024).decode().strip()
            print(f"    Service Info: {banner}")
        except:
            print("    No banner available")
    
    s.close()