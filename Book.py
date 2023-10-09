class Book():
    def int(self, book_title, book_author, book_year):
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year

    def get_book_info(self):
        return f"{self.book_title} {self.book_author} {self.book_year}"