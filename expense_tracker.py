from datetime import datetime


def add_expense():

    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    file = open("expenses.txt", "a")

    file.write(date + " | " + name + " - " + str(amount) + "\n")

    file.close()

    print("Expense added successfully!")


def view_expenses():

    try:

        file = open("expenses.txt", "r")

        data = file.readlines()

        file.close()

        if len(data) == 0:
            print("No expenses found")

        else:

            print("\n--- Expenses ---")

            total = 0

            for line in data:

                print(line.strip())

                parts = line.strip().split(" - ")

                total += float(parts[1])

            print("--------------")
            print("Total Expense =", total)

    except FileNotFoundError:
        print("No expense file found")


def delete_expense():

    try:

        file = open("expenses.txt", "r")

        data = file.readlines()

        file.close()

        if len(data) == 0:
            print("No expenses to delete")
            return

        print("\n--- Expenses ---")

        for i in range(len(data)):
            print(i + 1, ".", data[i].strip())

        delete = int(input("Enter expense number to delete: "))

        if delete > 0 and delete <= len(data):

            removed = data.pop(delete - 1)

            file = open("expenses.txt", "w")

            file.writelines(data)

            file.close()

            print("Deleted:", removed.strip())

        else:
            print("Invalid number")

    except FileNotFoundError:
        print("Expense file not found")


def clear_all_expenses():

    confirm = input("Are you sure? (yes/no): ")

    if confirm == "yes":

        file = open("expenses.txt", "w")

        file.write("")

        file.close()

        print("All expenses deleted successfully!")

    else:
        print("Operation cancelled")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Clear All Expenses")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        clear_all_expenses()

    elif choice == "5":
        print("Closing App...")
        break

    else:
        print("Invalid choice")