from data.books import get_books


# Check out a book by its ID.
def checkout_book():
    books = get_books()
    book_id = input("Enter the book ID to check out: ").strip()

    if not book_id.isdigit() or int(book_id) not in books:
        print("Invalid book ID. Please try again.")
        return

    book_id = int(book_id)
    book = books[book_id]

    if book["quantity"] <= 0:
        print(f"Sorry, the book '{book['title']}' is not available for checkout.")
        return

    borrower_name = input("Enter the name of the borrower: ").strip()
    checkout_date = input("Enter the checkout date (YYYY-MM-DD): ").strip()

    # Mark the book as checked out
    if "borrowers" not in book:
        book["borrowers"] = []

    book["borrowers"].append({
        "name": borrower_name,
        "checkout_date": checkout_date
    })
    book["quantity"] -= 1

    print(f"\nThe book '{book['title']}' has been successfully checked out by {borrower_name}!")
