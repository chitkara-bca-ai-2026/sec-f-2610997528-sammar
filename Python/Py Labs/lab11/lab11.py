# Lab 11 - Online Account Registration

username = input("Enter your username: ")
password = input("Enter your password: ")

print("="*50)
print("      PASSWORD VALIDATION REPORT")
print("="*50)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print("\n--- Validation Rules ---")

# Rule 1: At least 8 characters
rule1 = len(password) >= 8
if rule1:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

# Rule 2: At least one digit
rule2 = False
for ch in password:
    if ch.isdigit():
        rule2 = True
        break

if rule2:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

# Rule 3: At least one uppercase letter
rule3 = False
for ch in password:
    if ch.isupper():
        rule3 = True
        break

if rule3:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

# Final Verdict
print("\n--- Result ---")
if rule1 and rule2 and rule3:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("="*50)