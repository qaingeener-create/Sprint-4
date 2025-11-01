from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2.

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

    def test_get_books_for_children_single_book(self):
        collector = BooksCollector()
        collector.add_new_book("Детская книга")
        collector.set_book_genre("Детская книга", "Мультфильмы")
        children_books = collector.get_books_for_children()
        assert "Детская книга" in children_books

    def test_get_books_for_children_excludes_adult_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Взрослая книга")
        collector.set_book_genre("Взрослая книга", "Ужасы")
        children_books = collector.get_books_for_children()
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

    def test_add_new_book_valid_name_length(self):
        collector = BooksCollector()
        book_name = "Допустимое название книги"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
    
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        book_name = "Книга для проверки жанра"
        invalid_genre = "Этот жанр слишком длинный и содержит недопустимые символы!"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        collector.get_book_genre(book_name) is None

    def test_add_book_in_favorites_book_not_in_books_genre(self):
        collector = BooksCollector()
        book_name = "Неизвестная книга"
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()
