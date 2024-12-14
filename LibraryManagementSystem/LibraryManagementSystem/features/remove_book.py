from data.books import get_books

# Remove a book from the library by its ID.
def remove_book():
    books = get_books()
    book_id = input("Enter the book ID to remove: ").strip()

    if not book_id.isdigit() or int(book_id) not in books:
        print("Invalid book ID. Please try again.")
        return

    book_id = int(book_id)
    book = books[book_id]

    confirmation = input(f"Are you sure you want to remove '{book['title']}'? (yes/no): ").strip().lower()
    if confirmation == "yes":
        del books[book_id]
        print(f"\nThe book '{book['title']}' has been successfully removed from the library.")
    else:
        print("\nOperation cancelled. The book was not removed.")
