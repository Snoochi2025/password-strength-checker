\# Password Strength Checker 🔐



A beginner-friendly Python cybersecurity project that checks password strength, detects common and predictable passwords, and generates secure random passwords.



\## Features



\- Checks password length

\- Detects uppercase and lowercase letters

\- Checks for numbers and special characters

\- Detects commonly used passwords

\- Detects predictable patterns

\- Detects repeated characters

\- Counts security warnings

\- Calculates a password strength score

\- Generates secure random passwords



\## Cybersecurity concepts



This project introduces several basic cybersecurity concepts:



\- Password strength and complexity

\- Common-password detection

\- Predictable-pattern detection

\- Repeated-character detection

\- Security warning systems

\- Secure random password generation using Python's `secrets` module



\## How to run



1\. Make sure Python is installed.

2\. Open a terminal in the project folder.

3\. Run the program with:



```bash

py password\_checker.py

4.Enter a password when prompted.

5.The program will display the password score, strength, security warnings, and a generated password.





\## Example output



```text

=========================

PASSWORD STRENGTH CHECKER

=========================



Enter a password: Example123!



Password is long enough!

Password contains a number!

Password contains an uppercase letter!

Password contains a lowercase!

Password contains a special character!



Score: 5 / 5

Security warnings: 0

Password strength: Strong



Generated password: <randomly generated password>



This password shown above is an example and should not be used as a real password.





\## Limitations



This project is designed for learning and demonstrates basic password security concepts.



Current limitations include:



\- The common-password list is relatively small.

\- Pattern detection is basic and may not detect every predictable pattern.

\- The password checker is not a replacement for professional password-auditing tools.

\- Passwords entered into the program should be test passwords, not real passwords.





\## Future improvements



Possible improvements for this project include:



\- Add a larger database of commonly used passwords

\- Improve predictable-pattern detection

\- Add password entropy calculations

\- Add automated tests

\- Create a graphical user interface (GUI)

\- Improve password-generation options

\- Add more detailed security recommendations





\## Technologies



\- Python

\- Python `secrets` module

\- Python `string` module

\- Git

\- GitHub

