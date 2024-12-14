from data.books import get_books


# View all books in the library
def view_all_books():
    books = get_books()
    if not books:
        print("No books are available in the library.")
        return
    
    print("\nAvailable Books in the Library:")
    print("ID | Title                    | Author               | Year | Quantity | Status")
    print("-" * 75)
    for book_id, details in books.items():
        status = "Available" if details["borrower"] is None else f"Checked out by {details['borrower']}"
        print(
            f"{book_id:<3}| {details['title']:<25}| {details['author']:<20}| {details['year']:<5}| {details['quantity']:<8}| {status}"
        )
