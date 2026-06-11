# Data Redundancy Removal System

database = []

def add_record(record):
    if record in database:
        print(f"{record} -> Redundant Data (Duplicate Found)")
    else:
        database.append(record)
        print(f"{record} -> Unique Data Added")

while True:
    print("\n1. Add Data")
    print("2. View Database")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        data = input("Enter data: ")
        add_record(data)

    elif choice == "2":
        print("\nStored Unique Data:")
        for item in database:
            print(item)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")