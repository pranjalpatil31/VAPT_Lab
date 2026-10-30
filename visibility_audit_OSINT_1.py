# pip install requests

import socket
import requests

org = input("Enter organization name: ")
domain = input("Enter official domain: ")

print("\n OSINT VISIBILITY AUDIT ")
print("Organization:", org)
print("Domain:", domain)

try:
    ip = socket.gethostbyname(domain)
    print("IP Address:", ip)
except:
    ip = None
    print("IP Address: Not found")

try:
    r = requests.get("https://" + domain, timeout=10)
    print("Website Status:", r.status_code)
except:
    print("Website Status: Unavailable")

print("\n--- PUBLIC FOOTPRINT ---")
print("Website:", "https://" + domain)

if ip:
    try:
        print("Hostname:", socket.gethostbyaddr(ip)[0])
    except:
        print("Hostname: Not found")

# Enter organization name: Vidyavardhini's College Of Engineering
# Enter official domain: vcet.edu.in

# --- OSINT VISIBILITY AUDIT ---
# Organization: Vidyavardhini's College Of Engineering
# Domain: vcet.edu.in
# IP Address: 173.254.89.26
# Website Status: 406

# --- PUBLIC FOOTPRINT ---
# Website: https://vcet.edu.in
# Hostname: box2289.bluehost.com