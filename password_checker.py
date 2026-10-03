print("=========================")
print("PASSWORD STRENGTH CHECKER")
print("=========================")
password = input("Enter a password: ")
common_passwords = [
    "password",
    "password123",
    "12345678",
    "qwerty",
    "qwerty123",
    "letmein",
    "welcome",
    "admin123",
    "abc123"
    "pass@123"
]
if password.lower() in common_passwords:
    print("⚠️ Warning: This is a commonly used password!")
else:
    print("This password was not found in the common password list.")
if len(password) >= 8:
    print("Password is long enough!")
else:
    print("Use at least 8 characters!")
if any(char.isdigit() for char in password):
    print("Password contains a number!")
else:
    print("Password needs a number!")
if any(char.isupper() for char in password):
    print("Password contains an uppercase letter!")
else:
    print("Password needs an uppercase letter!")
if any(char.islower() for char in password):
    print("Password contains a lowercase!")
else:
    print("Password needs a lowercase letter")  
special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
if any(char in special_characters for char in password):
    print("password contains a special character")
else:
    print("Password needs a special character!")
score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char in special_characters for char in password):
    score += 1
print ("Score:", score,"/ 5")
if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")
