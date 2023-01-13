"""Book store, test."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        return self.title


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.min_rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating >= self.min_rating:
            if len(self.books) <= 0:
                return True
            else:
                for book_in_store in self.books:
                    if book_in_store.title == book.title and book_in_store.author == book.author:
                        return False
                    else:
                        return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book) is True:
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if len(self.books) <= 0:
            return False
        else:
            for book_in_store in self.books:
                if book_in_store.title == book.title and book_in_store.author == book.author:
                    return True
                else:
                    return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book) is True:
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        books_sorted_by_price = sorted(self.books, key=lambda book: book.price)
        return books_sorted_by_price

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        books_sorted_by_rating = sorted(self.books, key=lambda book: book.price, reverse=True)
        print(books_sorted_by_rating)
        best_books = []
        for book in books_sorted_by_rating:
            if book.rating == books_sorted_by_rating[0].rating:
                best_books.append(book)
        return best_books


if __name__ == '__main__':
    raamat1 = Book("Raamat1", "Autor", 10, 56)
    raamat2 = Book("Raamat2", "Autor", 10, 50)
    raamat3 = Book("Raamat3", "Autor", 30, 50)
    raamat4 = Book("Raamat4", "Autor", 40, 56)
    raamat5 = Book("Raamat5", "Autor", 50, 30)

    pood = Store("Pood", 40)

    pood.add_book(raamat1)
    pood.add_book(raamat2)
    pood.add_book(raamat3)
    pood.add_book(raamat4)
    pood.add_book(raamat5)
    print(pood.can_add_book(raamat1))
    print(pood.can_add_book(raamat2))
    print(pood.can_add_book(raamat3))
    print(pood.can_add_book(raamat4))
    print(pood.can_add_book(raamat5))
    print(pood.get_all_books())
    print(pood.get_most_popular_book())