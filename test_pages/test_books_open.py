from src.pages.books_open.books_open_page import BooksOpenPage
import pytest


@pytest.mark.usefixtures("set_up_chrome")
class TestBooksOpen:
    @pytest.mark.parametrize('link, isnb_git, isnb_java, isnb_design, isnb_speaking, isnb_you_dont',
                             [(
                                     "https://demoqa.com/books",
                                     "9781449325862",
                                     "9781449331818",
                                     "9781449337711",
                                     "9781449365035",
                                     "9781491904244")])
    def test_books_open(self, link, isnb_git, isnb_java, isnb_design, isnb_speaking, isnb_you_dont):
        """
        Данная функция работает с https://demoqa.com/books.
        В данной функции мы проверяем содержимое книжного магазина выбирая последовательно все книги на сайте
        и сверяем с первой строчкой в карточке ISBN, что бы проверить что открыта именно данная вкладка.
        В разработке добавления сверки URL.
        """
        self.driver.get(link)
        self.books_open = BooksOpenPage(self.driver)
        self.books_open.find_first_book()
        assert self.books_open.return_check_isnb_git() == isnb_git
        self.books_open.back_to_book_store()
        self.books_open.find_second_book()
        assert self.books_open.return_check_isnb_java() == isnb_java
        self.books_open.back_to_book_store_with_up()
        self.books_open.find_third_book()
        assert self.books_open.return_check_isnb_design() == isnb_design
        self.books_open.back_to_book_store_with_up()
        self.books_open.find_four_book()
        assert self.books_open.return_check_isnb_speaking() == isnb_speaking
        self.books_open.back_to_book_store_with_up()
        self.books_open.find_five_book()
        assert self.books_open.return_check_isnb_you_dont() == isnb_you_dont
        self.books_open.back_to_book_store_with_down()


if __name__ == "__main__":
    TestBooksOpen().test_books_open()
