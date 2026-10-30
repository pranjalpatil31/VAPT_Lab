import subprocess

print("NETWORK TRAFFIC ANALYSIS")

result = subprocess.run(
    ["netstat", "-n"],
    capture_output=True, text=True
)

print("\n--- ACTIVE NETWORK CONNECTIONS ---\n")
print("Protocol   Local Address       Remote Address      State")
print("-" * 55)

for line in result.stdout.splitlines():
    parts = line.split()

    if len(parts) >= 4 and parts[0] == "TCP":
        print(f"{parts[0]:10} {parts[1]:20} "
              f"{parts[2]:20} {parts[3]}")

print("\n--- TRAFFIC ANALYSIS ---")

http_found = False
https_found = False

for line in result.stdout.splitlines():
    if line.strip().startswith("TCP"):
        parts = line.split()

        if len(parts) >= 4:
            remote = parts[2]

            if remote.endswith(":80"):
                print("[!] Possible HTTP connection:", remote)
                http_found = True

            elif remote.endswith(":443"):
                print("[+] Possible HTTPS connection:", remote)
                https_found = True

if not http_found:
    print("No HTTP connections found.")

if not https_found:
    print("No HTTPS connections found.")

print("\n" + "=" * 55)
print("          ANALYSIS COMPLETED")
print("=" * 55)
print("Note: Connection ports do not prove data encryption.")


# NETWORK TRAFFIC ANALYSIS

# --- ACTIVE NETWORK CONNECTIONS ---

# Protocol   Local Address       Remote Address      State
# -------------------------------------------------------
# TCP        127.0.0.1:5141       127.0.0.1:63155      ESTABLISHED
# TCP        127.0.0.1:49677      127.0.0.1:49678      ESTABLISHED
# TCP        192.168.0.101:49735  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:49898  48.218.107.61:443    ESTABLISHED
# TCP        192.168.0.101:50108  172.64.148.235:443   ESTABLISHED
# TCP        192.168.0.101:50301  104.18.39.21:443     ESTABLISHED
# TCP        192.168.0.101:52239  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:52904  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:53186  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:53401  172.64.148.235:443   ESTABLISHED
# TCP        192.168.0.101:63570  103.31.145.161:443   ESTABLISHED
# TCP        192.168.0.101:64141  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:64287  172.64.148.235:443   ESTABLISHED
# TCP        192.168.0.101:64588  104.18.32.47:443     ESTABLISHED
# TCP        192.168.0.101:64589  20.42.73.29:443      TIME_WAIT
# TCP        192.168.0.101:64614  192.168.0.1:53       TIME_WAIT
# TCP        192.168.0.101:64857  4.213.25.242:443     ESTABLISHED
# TCP        192.168.0.101:65369  192.168.0.1:53       TIME_WAIT

# --- TRAFFIC ANALYSIS ---
# [+] Possible HTTPS connection: 4.213.25.242:443
# [+] Possible HTTPS connection: 48.218.107.61:443
# [+] Possible HTTPS connection: 172.64.148.235:443
# [+] Possible HTTPS connection: 104.18.39.21:443
# [+] Possible HTTPS connection: 172.64.148.235:443
# [+] Possible HTTPS connection: 103.31.145.161:443
# [+] Possible HTTPS connection: 172.64.148.235:443
# [+] Possible HTTPS connection: 104.18.32.47:443
# [+] Possible HTTPS connection: 20.42.73.29:443
# [+] Possible HTTPS connection: 4.213.25.242:443

# =======================================================
#           ANALYSIS COMPLETED
# =======================================================
# Note: Connection ports do not prove data encryption.