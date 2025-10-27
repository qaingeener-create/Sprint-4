from main import BooksCollector

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
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre() 

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = "Война и мир"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre 

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Комедии")
        collector.set_book_genre("Книга2", "Комедии")
        books = collector.get_books_with_specific_genre("Комедии")
        assert "Книга1" in books
        assert "Книга2" in books 

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books
        assert "Взрослая книга" not in children_books 

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Книга для избранных"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books() 

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Удаляемая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books() 


    def test_add_new_book_invalid_name_too_long(self):
        collector = BooksCollector()
        book_name = "Эта книга имеет слишком длинное название, превышающее допустимые 40 символов"
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre() 


    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        book_name = "Повторяющаяся книга"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name) 
        assert len(collector.get_books_genre()) == 1 

 
    def test_set_book_genre_non_existent_book(self):
        collector = BooksCollector()
        book_name = "Неизвестная книга"
        genre = "Фантастика"
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) is None 