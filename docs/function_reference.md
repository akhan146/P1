# PASSWORD FUNCTION REFERENCES

1. is_non_empty(password: str) > bool
   - Checks whether the password is a non-empty string.
   - Raises TypeError if input is not a string.
   - Returns True if password has at least one character.

2. has_min_length(password: str, min_length: int = 8) > bool
   - Verifies that the password meets a minimum length requirement.
   - Default minimum length is 8 characters.
   - Raises TypeError if password is not a string or min_length is not an integer.

3. contains_uppercase(password: str) > bool
   - Returns True if the password contains at least one uppercase letter (A-Z).
   - Raises TypeError if input is not a string.

4. contains_lowercase(password: str) > bool
   - Returns True if the password contains at least one lowercase letter (a-z).
   - Raises TypeError if input is not a string.

5. contains_digit(password: str) > bool
   - Checks whether the password contains at least one digit (0-9).
   - Raises TypeError if input is not a string.

6. contains_special_char(password: str) > bool
   - Detects whether the password contains any special character (punctuation symbols like !, @, #, etc.).
   - Raises TypeError if input is not a string.

7. calculate_entropy(password: str) > float
   - Estimates the password’s entropy based on character sets (lowercase, uppercase, digits, special characters).
   - Returns a float representing the approximate strength in bits.
   - Raises TypeError if input is not a string.

8. check_password_strength(password: str) > str
   - Categorizes the password as Weak, Medium, Strong, or Invalid.
   - Uses a scoring system based on length and character variety.
   - Weak: 0–2 points, Medium: 3–4 points, Strong: 5 points.

9. count_character_types(password: str) > dict
   - Returns a dictionary with counts of:
       * uppercase letters
       * lowercase letters
       * digits
       * special characters
   - Useful for detailed analysis or UI feedback.

10. is_common_password(password: str, common_list: list = None) > bool
    - Checks whether the password is included in a list of known common passwords.
    - Default list includes: ["password", "123456", "qwerty", "abc123"].
    - Case-insensitive comparison.

11. mask_password(password: str) > str
    - Returns a masked version of the password using asterisks.
    - Useful for displaying passwords safely in UI or logs.

12. generate_strong_password(length: int = 12) > str
    - Generates a random strong password with at least one uppercase, lowercase, digit, and special character.
    - Ensures password meets "Strong" criteria.
    - Raises ValueError if length < 8.

13. detect_repeated_patterns(password: str) > bool
    - Detects repeated sequences within the password (e.g., "abcabc", "1212").
    - Returns True if repeated patterns exist, False otherwise.

14. advanced_password_evaluation(password: str) > dict
    - Returns a full password evaluation including:
      * length
      * counts of uppercase, lowercase, digits, special characters
      * entropy estimate
      * strength category (Weak, Medium, Strong, Invalid)
      * common-password check
      * repeated-pattern detection
      * masked password

# TEST CODE
if __name__ == "__main__":
    test_passwords = ["password123!", "Abc$1234", "aaAA11!!", "", "StrongPass#2025"]
    for pwd in test_passwords:
        print(f"Evaluating password: {pwd}")
        result = advanced_password_evaluation(pwd)
        for k, v in result.items():
            print(f"  {k}: {v}")
        print("-" * 50)
