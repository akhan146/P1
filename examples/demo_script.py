# DEMO SCRIPT – KEY FUNCTIONS

import sys
import os

# Get absolute path to project root (P1)
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.library_name import (
    check_password_strength,
    advanced_password_evaluation,
    generate_strong_password,
    is_common_password
)


# Example passwords to demo
demo_passwords = ["password123!", "Abc$1234", "StrongPass#2025", "aaAA11!!"]

print("=== PASSWORD DEMO ===\n")

# 1. Check Strength
print("1. Checking Password Strength:")
for pwd in demo_passwords:
    print(f"  {pwd} -> {check_password_strength(pwd)}")
print("-" * 50)

# 2. Full Evaluation
print("2. Advanced Password Evaluation:")
for pwd in demo_passwords:
    eval_result = advanced_password_evaluation(pwd)
    print(f"  Password: {pwd}")
    print(f"    Strength: {eval_result['strength']}")
    print(f"    Entropy: {eval_result['entropy']} bits")
    print(f"    Is common: {eval_result['is_common']}")
    print(f"    Masked: {eval_result['masked']}")
print("-" * 50)

# 3. Check for Common Passwords
print("3. Common Password Check:")
for pwd in demo_passwords:
    print(f"  {pwd} -> Is common: {is_common_password(pwd)}")
print("-" * 50)

# 4. Generate a Strong Password
print("4. Generate a Strong Password:")
new_pwd = generate_strong_password(12)
print(f"  Generated password: {new_pwd}")
print(f"  Evaluation: {advanced_password_evaluation(new_pwd)['strength']}")
print("-" * 50)
