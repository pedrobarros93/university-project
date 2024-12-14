from data.books import get_books


# Search for a book by its title
def search_book():
    books = get_books()

    # taking user input, removing whitespaces from the both ends and converting to lowercase
    search_query = input("Enter the book title to search: ").strip().lower()
    found = False

    print("\nSearch Results:")
    for book_id, details in books.items():
        if search_query in details["title"].lower():
            status = "Available" if details["borrower"] is None else f"Checked out by {details['borrower']}"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Year: {details['year']}, Quantity: {details['quantity']}, Status: {status}")
            found = True

    if not found:
        print("No books matched your search query.")
