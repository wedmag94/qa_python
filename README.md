# qa_python
## Autotests for the BooksCollector class
### Project description
    This project is a set of automated tests to test the functionality of the BooksCollector class. The tests are written using the pytest framework.
### Implemented tests:
    1. test_add_new_book_add_two_books
    Checks the addition of two new books to the dictionary. 

    2. test_set_book_genre_success
    The purpose of this test is to verify the correctness of the genre setting method for the book.

    3. test_get_book_genre_true_existing_book
    The purpose of this test is to verify the correctness of the genre extraction method for an already added and configured book in the BooksCollector system.

    4. test_get_books_with_specific_genre_list_of_books
    The purpose of this test is to verify the correctness of the book filtering method by a given genre in the BooksCollector system.

    5. test_get_books_genre_output
    The purpose of this test is to verify the correctness of the method that returns a complete list of all books with their genres in the BooksCollector system.

    6. test_get_books_for_children_with_age_restrictions
    The purpose of this test is to verify the correctness of the filtering method for books suitable for children based on the specified age restrictions in the BooksCollector system.

    7. test_add_book_in_favorites_append
    The purpose of this test is to check the correctness of the functionality for adding a book to the favorites list in the BooksCollector system.

    8. test_delete_book_from_favorites_succes
    The purpose of this test is to verify the correctness of the method of deleting a book from the favorites list in the BooksCollector system.

    9. test_get_list_of_favorites_books_correct
    The purpose of this test is to verify the correctness of the method for getting a list of books from favorites in the BooksCollector system.

### Running tests
    To run the tests, you must:
    1. Install pytest: pip install pytest
    2. Run the tests: pytest -v test_books_collector.py