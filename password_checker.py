import secrets
import string
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
common_patterns = [
    "123456",
    "abcdef",
    "qwerty",
    "987654"]  
if any(pattern in password.lower() for pattern in common_patterns):
    print("⚠️ Warning: Your password contains a predictable pattern!")
def generate_password(length=12):
    password = ""

    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)
   
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password += secrets.choice(characters)
    return password
common_password = password.lower() in common_passwords

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
pattern_found = any(pattern in password.lower() for pattern in common_patterns)

has_number = any(char.isdigit() for char in password)

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
if pattern_found:
    score -= 1
if common_password:
    score -= 1
print ("Score:", score,"/ 5")
if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")
print ("Generated password:", generate_password())
