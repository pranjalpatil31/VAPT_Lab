print("===== BLIND SQL INJECTION SIMULATION =====")

# Simulated database information
database = "dvwa"
users = {1: "admin", 2: "john", 3: "alice"}

# Step 1: Test user ID
user_id = input("\nEnter User ID: ")

try:
    user_id = int(user_id)

    # Step 2: Boolean-based testing
    print("\n--- BOOLEAN RESPONSE ---")

    if user_id in users:
        print("TRUE: User ID exists in database.")
    else:
        print("FALSE: User ID does not exist.")

    # Step 3: Extract database name
    print("\n--- DATABASE EXTRACTION ---")

    extracted = ""
    characters = "abcdefghijklmnopqrstuvwxyz"

    for position in range(len(database)):
        for char in characters:
            if database[position] == char:
                extracted += char
                print("Position", position + 1, ":", char)
                break

    # Step 4: Display information
    print("\n--- EXTRACTED INFORMATION ---")
    print("Database Name:", extracted)
    print("Table Name: users")
    print("Total Records:", len(users))

except ValueError:
    print("Please enter a valid numeric User ID.")

print("\n===== TEST COMPLETED =====")

# ===== BLIND SQL INJECTION SIMULATION =====

# Enter User ID: 4

# --- BOOLEAN RESPONSE ---
# FALSE: User ID does not exist.

# --- DATABASE EXTRACTION ---
# Position 1 : d
# Position 2 : v
# Position 3 : w
# Position 4 : a

# --- EXTRACTED INFORMATION ---
# Database Name: dvwa
# Table Name: users
# Total Records: 3

# ===== TEST COMPLETED =====
