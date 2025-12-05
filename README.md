# Password Strength Utility Library

## Project Title and Description
The Password Strength Utility Library is a Python-based toolkit that analyzes, evaluates, and improves password security. It includes 15+ fully documented functions that validate password structure, check strength requirements, detect weak patterns, calculate entropy, identify common passwords, and generate secure random passwords. This library serves as the foundation for an object-oriented redesign in Project 02.


## Domain Focus and Problem Statement
Password security is a critical component of modern information systems, yet users frequently create weak or predictable passwords. Common issues include short passwords, missing character types, repeated patterns, and the use of passwords found on common-password lists. These weaknesses make systems vulnerable to brute-force attacks, dictionary attacks, and credential stuffing.

This project addresses this challenge by providing a reusable password-analysis function library that:
- validates password structure
- checks for uppercase, lowercase, digits, and special characters
- calculates password entropy
- detects repeated patterns (e.g., abcabc, 1212)
- flags commonly used or compromised passwords
- generates strong, random passwords
- produces complete evaluation summaries for security audits

---

## Installation and Setup Instructions

### 1. Clone the repository
git clone https://github.com/akhan146/Project_One_Abdullah-Khan.git

## Usage Examples for Key Functions
- Evaluate a password

from src.library_name import advanced_password_evaluation

print(advanced_password_evaluation("StrongPass#2025"))



- Generate a strong password
from src.library_name import generate_strong_password

print(generate_strong_password(16))


- Check password strength category
from src.library_name import check_password_strength

print(check_password_strength("Abc123!"))


### Function Library Overview and Organization 

## Simple Validation Functions

is_non_empty() — checks if password is not empty

has_min_length() — checks minimum length

contains_uppercase() — detects uppercase letters

contains_lowercase() — detects lowercase letters

contains_digit() — detects numerical digits

contains_special_char() — detects special characters

## Medium Complexity Functions

calculate_entropy() — estimates password entropy

check_password_strength() — rates password as Weak/Medium/Strong

count_character_types() — counts uppercase, lowercase, digits, special

is_common_password() — checks if password is commonly used

mask_password() — hides password for UI display

## Complex Functions

generate_strong_password() — creates a secure random password

detect_repeated_patterns() — identifies repeated substring patterns

advanced_password_evaluation() — full password analysis summary