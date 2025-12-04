# PASSWORD FUNCTION REFERENCES

1. is_non_empty(password: str) > bool
   - Checks whether the password is a non-empty string.

2. has_min_length(password: str, min_length: int = 8) > bool
   - Verifies that the password meets a minimum length requirement.

3. contains_uppercase(password: str) > bool
   - Returns True if the password includes at least one uppercase letter.

4. contains_lowercase(password: str) > bool
   - Returns True if the password includes at least one lowercase letter.

5. contains_digit(password: str) > bool
   - Checks whether the password contains at least one digit.

6. contains_special_char(password: str) > bool
   - Detects whether the password contains any special punctuation character.

7. calculate_entropy(password: str) > float
   - Estimates the password’s entropy using character-set pools and password length.

8. check_password_strength(password: str) > str
   - Categorizes the password as Weak, Medium, Strong, or Invalid based on scoring rules.

9. count_character_types(password: str) > dict
   - Returns counts of uppercase, lowercase, digits, and special characters.

10. is_common_password(password: str, common_list: list = None) > bool
    - Checks whether the password is included in a list of common passwords.

11. mask_password(password: str) > str
    - Returns a masked version of the password (e.g., "******").

12. generate_strong_password(length: int = 12) > str
    - Generates a random strong password containing uppercase, lowercase, digits, and special characters.
    - Ensures output meets the criteria for a Strong password.

13. detect_repeated_patterns(password: str) > bool
    - Detects repeated sequences like "abcabc" or "1212".

14. advanced_password_evaluation(password: str) > dict
    - Returns a full evaluation summary including:
      * length
      * character-type counts
      * entropy
      * strength category
      * common-password check
      * repeated-pattern detection
      * masked password

15. __main__ test block
    - Runs a sample evaluation on multiple test passwords and prints a detailed breakdown.

Example:
if __name__ == "__main__":
    test_passwords = ["password123!", "Abc$1234", "aaAA11!!", "", "StrongPass#2025"]
    for pwd in test_passwords:
        print(f"Evaluating password: {pwd}")
        result = advanced_password_evaluation(pwd)
        for k, v in result.items():
            print(f"  {k}: {v}")
        print("-" * 50)
