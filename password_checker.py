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
if any(char.isupper() for char in password):
    print("Password contains an uppercase!)
          else:
    print("Password needs an uppercase letter")
if any(char.islower() for char in password):
    print("Password contains a lowercase!")
else:print("Password needs a lowercase letter")  
