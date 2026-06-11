import sqlite3
import random

# Create Database
conn = sqlite3.connect("buspass.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bus_passes(
    pass_id INTEGER PRIMARY KEY,
    name TEXT,
    source TEXT,
    destination TEXT,
    amount INTEGER
)
""")

conn.commit()

def book_pass():
    name = input("Enter Passenger Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    amount = 500

    pass_id = random.randint(1000, 9999)

    cursor.execute(
        "INSERT INTO bus_passes VALUES (?, ?, ?, ?, ?)",
        (pass_id, name, source, destination, amount)
    )

    conn.commit()

    print("\nPass Booked Successfully!")
    print("Pass ID:", pass_id)

def view_pass():
    pid = int(input("Enter Pass ID: "))

    cursor.execute(
        "SELECT * FROM bus_passes WHERE pass_id=?",
        (pid,)
    )

    result = cursor.fetchone()

    if result:
        print("\n----- BUS PASS -----")
        print("Pass ID:", result[0])
        print("Name:", result[1])
        print("Source:", result[2])
        print("Destination:", result[3])
        print("Amount:", result[4])
    else:
        print("Pass Not Found!")

while True:
    print("\n===== CLOUD BUS PASS SYSTEM =====")
    print("1. Book Pass")
    print("2. View Pass")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_pass()

    elif choice == "2":
        view_pass()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

conn.close()