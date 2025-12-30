# Login Validation System 🔐

This project is a basic Python-based login validation system that demonstrates how user authentication works using control flow, validation, and security checks.

## 🚀 Features
- Username and password input
- Empty field validation
- Username format validation (letters and numbers only)
- Limited login attempts
- Automatic account lock after multiple failures
- Password hidden while typing

## 🧠 How It Works
1. The user enters a username and password.
2. The system checks if both fields are filled.
3. The username is checked for correct format and existence.
4. The password is matched with the stored value.
5. If the user fails multiple times, the account is locked for a short time.
6. On successful login, access is granted.

## 🛠 Technologies Used
- Python
- Regular Expressions
- getpass (for hidden password input)

## ▶ How to Run
1. Make sure Python is installed.
2. Download or clone this repository.
3. Open terminal inside the folder.
4. Run:
   ```bash
   python login.py