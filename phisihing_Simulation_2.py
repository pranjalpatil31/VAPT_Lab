
print("===== PHISHING SIMULATION =====")

email = input("Enter sender email: ")
subject = input("Enter email subject: ")
link = input("Enter website link: ")

print("\n--- EMAIL DETAILS ---")
print("Sender:", email)
print("Subject:", subject)
print("Link:", link)

risk = 0

print("\n--- SECURITY CHECK ---")

if "@" in email and "." in email:
    print("Email Format: Valid")
else:
    print("Email Format: Invalid")
    risk += 1

if "https://" in link:
    print("Link Security: HTTPS detected")
else:
    print("Link Security: Unsafe protocol")
    risk += 1

keywords = ["urgent", "verify", "password", "blocked"]

for word in keywords:
    if word in subject.lower():
        print("Suspicious Word:", word)
        risk += 1

print("\n--- FINAL RESULT ---")

if risk >= 2:
    print("Risk Level: HIGH")
    print("Warning: Possible phishing email!")
    print("Do not click the link.")
elif risk == 1:
    print("Risk Level: MEDIUM")
    print("Verify before trusting.")
else:
    print("Risk Level: LOW")
    print("No basic warning detected.")

print("Total Risk Score:", risk)
print("Simulation Completed.")


# ===== PHISHING SIMULATION =====
# Enter sender email: abc@gmail.com
# Enter email subject: Account Blocked permanently
# Enter website link: http://abc.com

# --- EMAIL DETAILS ---
# Sender: abc@gmail.com
# Subject: Account Blocked permanently
# Link: http://abc.com

# --- SECURITY CHECK ---
# Email Format: Valid
# Link Security: Unsafe protocol
# Suspicious Word: blocked

# --- FINAL RESULT ---
# Risk Level: HIGH
# Warning: Possible phishing email!
# Total Risk Score: 2
# Simulation Completed.
