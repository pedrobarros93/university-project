from data.books import get_books


# Add a new book to the library.
def add_book():
    books = get_books()

    # Get details from the user
    title = input("Enter the book title: ").strip()
    author = input("Enter the author name: ").strip()
    genre = input("Enter the genre: ").strip()
    year = input("Enter the publication year: ").strip()
    quantity = input("Enter the quantity of books: ").strip()

    # Generate a new book ID
    new_id = max(books.keys(), default=0) + 1

    # Add the new book to the dictionary
    books[new_id] = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": int(year) if year.isdigit() else year,
        "quantity": int(quantity) if quantity.isdigit() else 0,
        "borrower": None,
        "checkout_date": None,
        "checkin_date": None
    }

    print(f"\nBook '{title}' has been successfully added with ID {new_id}!")
