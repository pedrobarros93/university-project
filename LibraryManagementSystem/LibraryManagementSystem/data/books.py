# A dictionary to store book details
books = {
    1: {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "year": 1925,
        "quantity": 3,  # Number of available copies
        "borrower": None,  # Name of the person who borrowed (None if available)
        "checkout_date": None,  # Date of checkout (None if available)
        "checkin_date": None  # Date of check-in (None if available)
    },
    2: {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "quantity": 5,
        "borrower": None,
        "checkout_date": None,
        "checkin_date": None
    },
    3: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "quantity": 2,
        "borrower": None,
        "checkout_date": None,
        "checkin_date": None
    },
    4: {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "year": 1951,
        "quantity": 4,
        "borrower": None,
        "checkout_date": None,
        "checkin_date": None
    }
}

# Function to retrieve all books
def get_books():
    return books
