import socket

target = input("Enter target IP address: ")

print("       BASIC PENETRATION TEST")

# 1. Host Discovery
print("\n--- HOST DISCOVERY ---")

try:
    socket.inet_aton(target)
    print("Valid IP address:", target)
except socket.error:
    print("Invalid IP address.")
    exit()

# 2. Port Scanning
print("\n--- PORT SCANNING ---")

ports = [21, 22, 23, 25, 53, 80, 139, 443, 445, 3306, 8080]
open_ports = []

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            print("Port", port, ": OPEN")
            open_ports.append(port)

    except socket.error:
        pass

    finally:
        s.close()

# 3. Basic Service Analysis
print("\n--- SERVICE ANALYSIS ---")

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    8080: "HTTP Alternative"
}

for port in open_ports:
    print(services.get(port, "Unknown"), "service detected on port", port)

# 4. Final Report
print("       PENETRATION TEST REPORT")

print("Target IP:", target)
print("Open Ports:", open_ports)
print("Total Open Ports:", len(open_ports))

if open_ports:
    print("Result: Open services detected.")
else:
    print("Result: No tested ports are open or reachable.")

print("          TEST COMPLETED")

# Enter target IP address: 192.168.1.2
#        BASIC PENETRATION TEST

# --- HOST DISCOVERY ---
# Valid IP address: 192.168.1.2

# --- PORT SCANNING ---
# Port 25 : OPEN

# --- SERVICE ANALYSIS ---
# SMTP service detected on port 25
#        PENETRATION TEST REPORT
# Target IP: 192.168.1.2
# Open Ports: [25]
# Total Open Ports: 1
# Result: Open services detected.
#           TEST COMPLETED