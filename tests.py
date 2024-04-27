import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Сталкер', 'Мастер и Маргарита'])
    def test_add_new_book_check_in_books(self, book_name, collector):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_set_book_genre_from_list_check_genre(self, collector):
        book = 'Сталкер'
        genre = 'Фантастика'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_set_book_genre_not_in_list(self, collector):
        book = 'Затворники'
        genre = 'Триллер'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_book_not_exist(self, collector):
        book = 'Азазель'
        collector.set_book_genre(book, 'Детектив')
        genre = collector.get_book_genre(book)
        assert genre is None

    @pytest.mark.parametrize('books, specific_genre', [['Фауст', 'Комедии'],
                                                       ['Алиса в стране чуда', 'Мультфильмы'],
                                                       ['Четвёртое крыло', 'Фантастика'],
                                                       ['Я знаю, что видел', 'Детективы'],
                                                       ['Семь ликов страха', 'Ужасы']])
    def test_get_books_with_specific_genre(self, collector, books, specific_genre):
        collector.add_new_book(books)
        collector.set_book_genre(books, specific_genre)
        assert books in collector.get_books_with_specific_genre(specific_genre)

    def test_get_books_genre_return_current_books_genre(self, collector):
        book = 'Дракула'
        genre = 'Ужасы'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_genre() == {book: genre}

    def test_get_books_for_children_get_books_without_rating(self, collector):
        book_1 = 'Сияние'
        book_2 = 'Солярис'
        genre_book_horror = 'Ужасы'
        genre_book_fantasy = 'Фантастика'
        collector.add_new_book(book_1)
        collector.set_book_genre(book_1, genre_book_horror)
        collector.add_new_book(book_2)
        collector.set_book_genre(book_2, genre_book_fantasy)
        assert collector.get_books_for_children() == [book_2]

    def test_add_book_in_favorites_add_book_from_books_genre(self, collector):
        book = 'Оно'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self, collector):
        book = '1984'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_whole_list_books_from_favorites(self, collector):
        name_book_1 = 'Дракула'
        name_book_2 = 'Оно'
        collector.add_new_book(name_book_1)
        collector.add_new_book(name_book_2)
        collector.add_book_in_favorites(name_book_1)
        collector.add_book_in_favorites(name_book_2)
        assert collector.get_list_of_favorites_books() == [name_book_1, name_book_2] and len(collector.get_list_of_favorites_books()) == 2
