import re

print("===== PASSWORD AUDITING TOOL =====")

passwords = []

# Enter passwords for auditing
n = int(input("Enter number of passwords to audit: "))

for i in range(n):
    password = input(f"\nEnter password {i + 1}: ")
    passwords.append(password)

print("\n===== PASSWORD AUDIT REPORT =====")

for i, password in enumerate(passwords, 1):

    score = 0
    issues = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        issues.append("Too short")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Missing uppercase letter")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("Missing lowercase letter")

    # Check digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("Missing number")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        issues.append("Missing special character")

    print(f"\nPassword {i}: {password}")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MEDIUM")
    else:
        print("Strength: STRONG")

    if issues:
        print("Suggestions:", ", ".join(issues))

print("\n===== AUDIT COMPLETED =====")

# Enter number of passwords to audit: 3

# Enter password 1: abc

# Enter password 2: vcet

# Enter password 3: vcet@123

# ===== PASSWORD AUDIT REPORT =====

# Password 1: abc
# Strength: WEAK
# Suggestions: Too short, Missing uppercase letter, Missing number, Missing special character

# Password 2: vcet
# Strength: WEAK
# Suggestions: Too short, Missing uppercase letter, Missing number, Missing special character

# Password 3: vcet@123
# Strength: MEDIUM
# Suggestions: Missing uppercase letter

# ===== AUDIT COMPLETED =====