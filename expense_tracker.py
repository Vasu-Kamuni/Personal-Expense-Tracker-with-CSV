import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
    except FileExistsError:
        pass


def get_date():
    while True:
        value = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            if parsed.strftime("%Y-%m-%d") != value:
                raise ValueError
            return value
        except ValueError:
            print("Invalid date. Example: 2026-10-27")


def get_amount():
    while True:
        try:
            amount = Decimal(input("Enter amount: ").strip())
            if not amount.is_finite() or amount <= 0:
                print("Amount must be a positive number.")
                continue
            return amount
        except InvalidOperation:
            print("Invalid amount. Enter a number such as 150 or 99.50.")


def read_expenses():
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_expense():
    print("\n--- Add Expense ---")
    date = get_date()
    category = input("Enter category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()
    amount = get_amount()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "date": date,
            "category": category.title(),
            "description": description,
            "amount": str(amount.quantize(Decimal("0.01")))
        })

    print("Expense saved successfully!")


def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nDate       | Category     | Description          | Amount")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['category']:<12} | "
            f"{expense['description']:<20} | "
            f"{expense['amount']:>10}"
        )


def view_expenses():
    print("\n--- All Expenses ---")
    display_expenses(read_expenses())


def filter_expenses():
    print("\n1. Filter by category")
    print("2. Filter by date")
    choice = input("Choose filter: ").strip()

    expenses = read_expenses()

    if choice == "1":
        category = input("Enter category: ").strip().casefold()
        results = [
            e for e in expenses
            if e["category"].casefold() == category
        ]
    elif choice == "2":
        date = get_date()
        results = [e for e in expenses if e["date"] == date]
    else:
        print("Invalid filter choice.")
        return

    display_expenses(results)


def category_summary():
    expenses = read_expenses()
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = Decimal(expense["amount"])
        totals[category] = totals.get(category, Decimal("0")) + amount

    if not totals:
        print("No expenses available for summary.")
        return

    print("\n--- Category Summary ---")
    for category, total in sorted(totals.items()):
        print(f"{category:<15} : {total:.2f}")

    grand_total = sum(totals.values(), Decimal("0"))
    print("-" * 30)
    print(f"{'Grand Total':<15} : {grand_total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter expenses")
        print("4. Category summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                filter_expenses()
            elif choice == "4":
                category_summary()
            elif choice == "5":
                print("Expenses saved. Goodbye!")
                break
            else:
                print("Invalid choice. Select 1 to 5.")
        except (OSError, csv.Error, InvalidOperation, KeyError) as error:
            print("Could not process the expense file:", error)


if __name__ == "__main__":
    main()
