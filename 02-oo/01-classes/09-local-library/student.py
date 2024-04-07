class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        pass


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        pass

    def add_book(self, book):
        self.books.append(book)
        pass

    def remove_book(self, book):
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author:
                self.books.remove(lib_book)
        pass

    def search_books(self, search_string):
        result = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                result.append(book)
        return result
