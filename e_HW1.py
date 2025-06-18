# Home_Work 3
# Exercise 1
# Date: Feb 24, 2025
# Author: Marzie Mohammadsadeqiqayem

'''
Write a Python program to check the validity of password tried by a user by checking the following 
features: 
• Minimum length: 9 characters. 
• Maximum length: 13 characters. 
• At least one letter between [a-z] and one letter between [A-Z]. 
• At least two numbers between [0-9]. 
• At least one character from [&$#@*]. 
If the password tried by the used is not valid, you should give him/her a message and explain which 
one(s) of the above criterion is/are not satisfied.  '''

def check_password(password):
    errors = []

    # Check password length
    if len(password) < 9:
        errors.append("Password must be at least 9 characters long.")
    elif len(password) > 13:
        errors.append("Password must not be longer than 13 characters.")

    # these items must be check to check required character types
    has_lower = False
    has_upper = False
    digit_count = 0
    has_special = False
    special_chars = "&$#@*"

    # Go through each character in the password
    for char in password:
        if 'a' <= char <= 'z':  # Lowercase letter 
            has_lower = True
        elif 'A' <= char <= 'Z':  # Uppercase letter 
            has_upper = True
        elif '0' <= char <= '9':  # Digit 
            digit_count += 1
        elif char in special_chars:  # Special character 
            has_special = True

    # Validate step for each requirement
    if not has_lower:
        errors.append("Password must include at least one lowercase letter (a-z).")
    if not has_upper:
        errors.append("Password must include at least one uppercase letter (A-Z).")
    if digit_count < 2:
        errors.append("Password must include at least two numbers (0-9).")
    if not has_special:
        errors.append("Password must include at least one special character from [&$#@*].")

    # Display results
    if errors:
        print("Invalid password. Please fix the following issues:")
        for error in errors:
            print("-", error)
    else:
        print("Password is valid!")

# Get user input
password = input("Enter a password: ")
check_password(password)
