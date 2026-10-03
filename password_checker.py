print("Password Strength Checker")
password = input("Enter a password: ")
if len(password) >= 8:
    print("Password is long enough!")
else:
    print("Use at least 8 characters!")
if any(char.isdigit() for char in password):
    print("Password contains a number!")
else:
    print("Password needs a number!")
