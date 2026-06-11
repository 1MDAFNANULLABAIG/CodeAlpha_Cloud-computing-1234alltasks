import sqlite3
import hashlib

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# Encrypt password using SHA-256
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register user
def register(username, password):
    encrypted_pass = encrypt_password(password)

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, encrypted_pass)
    )

    conn.commit()
    print("User Registered Successfully!")

# Secure Login
def login(username, password):
    encrypted_pass = encrypt_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, encrypted_pass)
    )

    result = cursor.fetchone()

    if result:
        print("Login Successful!")
    else:
        print("Invalid Username or Password!")

# Main Menu
while True:
    print("\n----- SQL Injection Protection System -----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Enter Username: ")
        pwd = input("Enter Password: ")
        register(user, pwd)

    elif choice == "2":
        user = input("Enter Username: ")
        pwd = input("Enter Password: ")
        login(user, pwd)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")

conn.close()