from book import Book
from library import Library
def main():
    library = Library()

    while True:
        print("Оберіть дію:\n1. Додати книгу до бібліотеки\n"
              "2. Видалити книгу з бібліотеки\n3. Показати всі книги\n"
              "4. Пошук книги за назвою\n5. Пошук книги за автором\n"
              "6. Пошук книги за роком видання\n7. Вихід")

        selector = input("Ваш вибір: ")

        if selector == "1":
           title = input("Введіть назву книги")
           author = input("Введіть автора книги")
           year = input("Введіть дату видання")
           book = Book(title, author, year)
           library.add_book(book)
           print("Книгу додано.")
        elif selector == "2":
            title = input("Введіть назву книги яку бажаєте видалити: ")
            library.remove_book(title)
        elif selector == "3":
            library.list_books()
        elif selector == "4":
            title = input("Введіть назву книги для пошуку: ")
            library.search_by_title(title)
        elif selector == "5":
            author = input("Введіть ім'я автора для пошуку: ")
            library.search_by_author(author)
        elif selector == "6":
            year = input("Введіть рік видання для пошуку: ")
            library.search_by_year(year)
        elif selector == "7":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
if __name__ == "__main__":
    main()