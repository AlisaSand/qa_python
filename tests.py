import pytest
from main import BooksCollector

DEFAULT_RATING = 1


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_rating_1_is_set_for_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Как править миром, не привлекая внимания санитаров')
        assert collector.get_book_rating('Как править миром, не привлекая внимания санитаров') == DEFAULT_RATING

    @pytest.mark.parametrize('rating', [1, 10])
    def test_set_book_rating_when_rating_is_valid(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Excel 2010')
        collector.set_book_rating('Excel 2010', rating)
        assert collector.get_book_rating('Excel 2010') == rating

    @pytest.mark.parametrize('rating', [0, 11])
    def test_set_book_rating_when_rating_is_invalid(self, rating):
        collector = BooksCollector()
        collector.add_new_book('Школа игры на гитаре')
        collector.set_book_rating('Школа игры на гитаре', rating)
        assert collector.get_book_rating('Школа игры на гитаре') == DEFAULT_RATING

    def test_get_books_with_specified_rating_shows_only_books_with_this_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Как править миром, не привлекая внимания санитаров')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        collector.set_book_rating('Как править миром, не привлекая внимания санитаров', 10)
        actual_result = collector.get_books_with_specific_rating(10)
        expected_result = [
            'Гордость и предубеждение и зомби',
            'Как править миром, не привлекая внимания санитаров'
        ]
        assert actual_result == expected_result

    def test_get_books_rating_return_dictionary_of_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        expected_result = {
            'Гордость и предубеждение и зомби': 10,
            'Что делать, если ваш кот хочет вас убить': 5,
        }
        actual_result = collector.get_books_rating()
        assert actual_result == expected_result

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites_delete_one_of_two_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']
