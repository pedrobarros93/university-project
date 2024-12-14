from data.books import get_books


# Check in a book by its ID.
def checkin_book():
    books = get_books()
    book_id = input("Enter the book ID to check in: ").strip()

    if not book_id.isdigit() or int(book_id) not in books:
        print("Invalid book ID. Please try again.")
        return

    book_id = int(book_id)
    book = books[book_id]

    if "borrowers" not in book or not book["borrowers"]:
        print(f"The book '{book['title']}' is already fully available in the library.")
        return

    print("\nBorrowers:")
    for i, borrower in enumerate(book["borrowers"], start=1):
        print(f"{i}. {borrower['name']} (Checked out on: {borrower['checkout_date']})")

    borrower_index = input("Enter the number of the borrower to check in: ").strip()

    if not borrower_index.isdigit() or not (1 <= int(borrower_index) <= len(book["borrowers"])):
        print("Invalid selection. Please try again.")
        return

    borrower_index = int(borrower_index) - 1
    returned_borrower = book["borrowers"].pop(borrower_index)

    # Increase quantity since a copy is returned
    book["quantity"] += 1

    print(f"\nThe book '{book['title']}' has been successfully checked in by {returned_borrower['name']}!")

