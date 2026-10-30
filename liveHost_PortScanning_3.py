import socket
import subprocess
import platform
import re

target = input("Enter target IP address: ")

# 1. Live Host Discovery
print("\n--- LIVE HOST DISCOVERY ---")

param = "-n" if platform.system().lower() == "windows" else "-c"

result = subprocess.run(
    ["ping", param, "1", target],
    capture_output=True, text=True
)

if result.returncode == 0:
    print(target, "is LIVE")
else:
    print(target, "did not respond to ping")

# 2. Port Scanning
print("\n--- PORT SCANNING ---")

ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if s.connect_ex((target, port)) == 0:
        print("Port", port, ": OPEN")

    s.close()

# 3. OS Fingerprinting
print("\n--- OS FINGERPRINTING ---")

try:
    output = subprocess.check_output(
        ["ping", param, "1", target],
        text=True,
        stderr=subprocess.DEVNULL
    )

    match = re.search(r"ttl[=:](\d+)", output, re.I)

    if match:
        ttl = int(match.group(1))
        print("TTL Value:", ttl)

        if ttl <= 64:
            print("Possible OS: Linux/Unix")
        elif ttl <= 128:
            print("Possible OS: Windows")
        else:
            print("Possible OS: Other Network Device")
    else:
        print("TTL information unavailable")

except Exception:
    print("OS fingerprinting unavailable")

print("\nScan Completed.")

# Enter target IP address: 192.168.1.1

# --- LIVE HOST DISCOVERY ---
# 192.168.1.1 did not respond to ping

# --- PORT SCANNING ---
# Port 25 : OPEN
# Port 110 : OPEN

# --- OS FINGERPRINTING ---
# OS fingerprinting unavailable

# Scan Completed.