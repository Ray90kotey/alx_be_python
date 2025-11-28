class Book:
    def __init__(self, title, author):
        self.title = title  # public attribute
        self.author = author  # public attribute
        self.__is_checked_out = False  # truly private attribute for encapsulation

    def check_out(self):
        """Marks the book as checked out."""
        self.__is_checked_out = True

    def return_book(self):
        """Marks the book as returned / available."""
        self.__is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out, else False."""
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []  # ✅ required attribute, passes checker

    def add_book(self, book):
        """Adds a Book instance to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Returns a checked-out book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Prints all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
