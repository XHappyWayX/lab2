class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' видалена з бібліотеки.")
                return
        print(f"Книга '{title}' не знайдена у бібліотеці.")

    def list_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        else:
            print("Книги у бібліотеці:")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            print(f"Результати пошуку за назвою '{title}':")
            for book in found_books:
                print(book)
        else:
            print(f"Книга з назвою '{title}' не знайдена у бібліотеці.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f"Результати пошуку автора '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"Книги автора '{author}' не знайдено у бібліотеці.")

    def search_by_year(self, year):
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            print(f"Результати пошуку за роком видання '{year}':")
            for book in found_books:
                print(book)