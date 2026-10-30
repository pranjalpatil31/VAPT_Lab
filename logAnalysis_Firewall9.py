from collections import Counter

print("===== SERVER LOG ANALYSIS =====")

# Sample server logs
logs = [
    "192.168.1.10 LOGIN SUCCESS",
    "192.168.1.20 LOGIN FAILED",
    "192.168.1.20 LOGIN FAILED",
    "192.168.1.20 LOGIN FAILED",
    "192.168.1.30 LOGIN SUCCESS",
    "10.0.0.5 LOGIN FAILED",
    "10.0.0.5 LOGIN FAILED",
    "192.168.1.40 LOGIN SUCCESS"
]

failed_ips = []

print("\n--- LOG DETAILS ---")

for log in logs:
    print(log)

    if "LOGIN FAILED" in log:
        ip = log.split()[0]
        failed_ips.append(ip)

# Count failed login attempts
counts = Counter(failed_ips)

print("\n--- ANOMALY DETECTION ---")

for ip, count in counts.items():
    if count >= 3:
        print("[ALERT] Suspicious activity from:", ip)
        print("Failed attempts:", count)

    elif count > 0:
        print("[WARNING] Failed login from:", ip)
        print("Failed attempts:", count)

# Final report
print("\n--- ANALYSIS REPORT ---")
print("Total log entries:", len(logs))
print("Failed login attempts:", len(failed_ips))
print("Unique suspicious IPs:",
      sum(1 for count in counts.values() if count >= 3))

print("\n===== ANALYSIS COMPLETED =====")

# ===== SERVER LOG ANALYSIS =====

# --- LOG DETAILS ---
# 192.168.1.10 LOGIN SUCCESS
# 192.168.1.20 LOGIN FAILED
# 192.168.1.20 LOGIN FAILED
# 192.168.1.20 LOGIN FAILED
# 192.168.1.30 LOGIN SUCCESS
# 10.0.0.5 LOGIN FAILED
# 10.0.0.5 LOGIN FAILED
# 192.168.1.40 LOGIN SUCCESS

# --- ANOMALY DETECTION ---
# [ALERT] Suspicious activity from: 192.168.1.20
# Failed attempts: 3
# [WARNING] Failed login from: 10.0.0.5
# Failed attempts: 2

# --- ANALYSIS REPORT ---
# Total log entries: 8
# Failed login attempts: 5
# Unique suspicious IPs: 1

# ===== ANALYSIS COMPLETED =====