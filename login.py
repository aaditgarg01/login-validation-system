import time
import re
from getpass import getpass

# User database
users = {
    "admin": "admin@2025",
    "user1": "pass123",
    "guest": "guest01"
}

MAX_ATTEMPTS = 3
LOCK_TIME = 30   # seconds
failed_attempts = 0
lock_until = 0

while True:

    # Check if locked
    if time.time() < lock_until:
        remaining = int(lock_until - time.time())
        print(f"Account locked. Try again after {remaining} seconds.\n")
        time.sleep(5)
        continue

    username = input("Enter username: ").strip()
    password = getpass("Enter password: ").strip()

    # Empty input check
    if username == "" or password == "":
        print("Username and password cannot be empty.\n")
        continue

    # Username format check
    if not re.match("^[A-Za-z0-9]+$", username):
        print("Invalid username format. Only letters and numbers allowed.\n")
        continue

    # Username existence check
    if username not in users:
        print("Username not found.")
        failed_attempts += 1

    else:
        # Password check
        if users[username] == password:
            print("Login successful! Welcome.")
            failed_attempts = 0
            break
        else:
            print("Incorrect password.")
            failed_attempts += 1

    # Lock account if attempts exceeded
    if failed_attempts >= MAX_ATTEMPTS:
        lock_until = time.time() + LOCK_TIME
        print(f"Too many failed attempts. Account locked for {LOCK_TIME} seconds.\n")
        failed_attempts = 0
