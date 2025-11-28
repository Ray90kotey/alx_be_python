class Book:
    def __init__(self, title, author):
        self.title = title        # public
        self.author = author      # public
        self.__is_checked_out = False  # private attribute

    def check_out(self):
        """Mark book as checked out."""
        self.__is_checked_out = True

    def return_book(self):
        """Mark book as returned / available."""
        self.__is_checked_out = False

    def is_available(self):
        """Check availability status."""
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []  # private list of books

    def add_book(self, book: Book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self.__books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self.__books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book (mark it available again)."""
        for book in self.__books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self.__books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
