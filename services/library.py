from datetime import datetime

# Dictionary for storing books
books = {}

def add_book():
    name = input("Enter Book Name: ")

    if name in books:
        print("Book already exists")
    else:
        books[name] = {
            "available": True,
            "issued_to": None,
            "issue_date": None
        }
        print(name, "added successfully")


def show_books():
    if not books:
        print("No books available")
        return

    print("\nAvailable Books:")
    for book, info in books.items():
        status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
        print(f"{book} - {status}")


def issue_book():
    name = input("Enter book name: ")

    if name in books and books[name]["available"]:
        student = input("Enter student name: ")

        books[name]["available"] = False
        books[name]["issued_to"] = student
        books[name]["issue_date"] = datetime.now()

        print(name, "issued to", student)
    else:
        print("Book not available")


def return_book():
    name = input("Enter book name: ")

    if name in books and not books[name]["available"]:
        issue_date = books[name]["issue_date"]
        days = (datetime.now() - issue_date).days

        fine = 0
        if days > 7:
            weeks = (days - 7) // 7 + 1
            fine = weeks * 10

        print("Days used:", days)
        print("Fine:", fine)

        books[name]["available"] = True
        books[name]["issued_to"] = None
        books[name]["issue_date"] = None

        print("Book returned successfully")

    else:
        print("Invalid return")