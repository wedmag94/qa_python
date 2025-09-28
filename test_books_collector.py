from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
        "book_name, genre",
        [("Гарри Поттер", "Фантастика"), ("Русалочка", "Мультфильмы")],
    )
    def test_set_book_genre_success(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_true_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.get_book_genre("Гарри Поттер")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_books_with_specific_genre_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        books_with_specific_genre = collector.get_books_with_specific_genre(
            "Фантастика"
        )
        assert books_with_specific_genre == ["Гарри Поттер"]

    def test_get_books_genre_output(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_new_book("Следствие вели колобки")
        collector.set_book_genre("Следствие вели колобки", "Мультфильмы")
        books = {
            "Гарри Поттер": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Следствие вели колобки": "Мультфильмы",
        }
        assert collector.get_books_genre() == books

    def test_get_books_for_children_with_age_restrictions(self):
        collector = BooksCollector()
        collector.add_new_book("Паранормальное явление")
        collector.set_book_genre("Паранормальное явление", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_new_book("Следствие вели колобки")
        collector.set_book_genre("Следствие вели колобки", "Мультфильмы")
        books_for_children = ["Следствие вели колобки"]
        assert collector.get_books_for_children() == books_for_children

    def test_add_book_in_favorites_append(self):
        collector = BooksCollector()
        collector.add_new_book("Паранормальное явление")
        collector.set_book_genre("Паранормальное явление", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_book_in_favorites("Шерлок Холмс")
        assert collector.favorites == ["Шерлок Холмс"]

    def test_delete_book_from_favorites_succes(self):
        collector = BooksCollector()
        collector.add_new_book("Паранормальное явление")
        collector.set_book_genre("Паранормальное явление", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_book_in_favorites("Шерлок Холмс")
        collector.add_book_in_favorites("Паранормальное явление")
        collector.delete_book_from_favorites("Паранормальное явление")
        assert collector.favorites == ["Шерлок Холмс"]

    def test_get_list_of_favorites_books_correct(self):
        collector = BooksCollector()
        collector.add_new_book("Паранормальное явление")
        collector.set_book_genre("Паранормальное явление", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        collector.add_book_in_favorites("Шерлок Холмс")
        collector.add_book_in_favorites("Паранормальное явление")
        result = collector.get_list_of_favorites_books()
        assert result == ["Шерлок Холмс", "Паранормальное явление"]