
# Usage examples and tutorials


# Example passwords to test
passwords = ["password123!", "Abc$1234", "StrongPass#2025", "aaAA11!!"]

# Tutorial 1: Check Password Strength
# Quickly categorize a password as Weak, Medium, or Strong
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password: {pwd} -> Strength: {strength}")

print("-" * 50)

# Tutorial 2: Full Password Evaluation
# Get a complete report including counts, entropy, common checks, and masked version
for pwd in passwords:
    print(f"Evaluating password: {pwd}")
    evaluation = advanced_password_evaluation(pwd)
    for key, value in evaluation.items():
        print(f"  {key}: {value}")
    print("-" * 50)

# Tutorial 3: Check for Common Passwords
# Identify passwords that are too common and insecure
for pwd in passwords:
    common = is_common_password(pwd)
    print(f"Password: {pwd} -> Is common: {common}")

print("-" * 50)

# Tutorial 4: Generate a Strong Password
# Create a new, strong password with letters, digits, and special characters
strong_pwd = generate_strong_password(12)
print(f"Generated strong password: {strong_pwd}")
