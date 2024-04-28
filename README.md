# qa_python - Sprint_4

1. Метод add_new_book:
* test_add_new_book_check_in_books - Проверяем добавление книги 
2. Метод set_book_genre:
* test_set_book_genre_from_list_check_genre - Проверям назначение книге жанра 
* test_set_book_genre_not_in_list - Проверяем азначение книге жанра не из списка
3. Метод get_book_genre:
* test_get_book_genre_book_not_exist - Проверяем назначение жанра книге не из списка
4. Метод get_books_with_specific_genre:
* test_get_books_with_specific_genre - Проверяем правильность вывода списка книг определенного жанра
5. Метод get_books_genre:
* test_get_books_genre_return_current_books_genre - Проверяем правильный вывод из словаря books_genre, который получаем методом get_books_genre содержание словаря books_genre
6. Метод get_books_for_children:
* test_get_books_for_children_get_books_without_rating - Проверяем, что метод не выводит в список книг для детей, которые им подходят. У жанра книги не должно быть возрастного рейтинга, который присутствует в списке genre_age_rating
7. Метод add_book_in_favorites:
* test_add_book_in_favorites_add_book_from_books_genre - Проверяем добавление книги, находящейся в словаре books_genre, в список favorites
8. Метод delete_book_from_favorites:
* test_delete_book_from_favorites_delete_book - Проверяем удаление книги, которая были добавлены в favorites
9. Метод get_list_of_favorites_books:
* test_get_list_of_favorites_books_get_whole_list_books_from_favorites - Проверяем соответствие списка, получаемого методом get_list_of_favorites_books в список favorites