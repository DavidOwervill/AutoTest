from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time


class LocatorsBooksStore:
    # By XPATH
    git_pocket_guide_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    back_to_book_store = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button"
    learning_java_script_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    designing_evolvable_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    speaking_java_script_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    you_dont_know_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"

@pytest.mark.usefixtures("set_up_chrome")
class TestBooksOpen:
    @pytest.mark.parametrize('link', ["https://demoqa.com/books"])
    def test_books_open(self, link):
        """
        Данная функция работает с https://demoqa.com/books.
        В данной функции мы проверяем содержимое книжного магазина выбирая последовательно все книги на сайте
        и сверяем с первой строчкой в карточке ISBN, что бы проверить что открыта именно данная вкладка.
        В разработке добавления сверки URL.
        Так же, данная функция делает скриншот после выполнения проверки каждой книги. Данная функция введена для
        визуального контроля карточки товара.
        """
        self.driver.get(link)
        self.driver.find_element(by=By.ID, value="see-book-Git Pocket Guide").click()
        time.sleep(3)
        assert "9781449325862" == self.driver.find_element(by=By.XPATH,
                                                                  value=LocatorsBooksStore.git_pocket_guide_isbn).text
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsBooksStore.back_to_book_store).click()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="see-book-Learning JavaScript Design Patterns").click()
        time.sleep(3)
        assert "9781449331818" == self.driver.find_element(by=By.XPATH,
                                                                  value=LocatorsBooksStore.learning_java_script_isbn).text

        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsBooksStore.back_to_book_store).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="see-book-Designing Evolvable Web APIs with ASP.NET").click()
        time.sleep(3)
        assert "9781449337711" == self.driver.find_element(by=By.XPATH,
                                                                  value=LocatorsBooksStore.designing_evolvable_isbn).text

        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsBooksStore.back_to_book_store).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="see-book-Speaking JavaScript").click()
        time.sleep(3)
        assert "9781449365035" == self.driver.find_element(by=By.XPATH,
                                                                  value=LocatorsBooksStore.speaking_java_script_isbn).text
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsBooksStore.back_to_book_store).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="see-book-You Don't Know JS").click()
        time.sleep(3)
        assert "9781491904244" == self.driver.find_element(by=By.XPATH,
                                                                  value=LocatorsBooksStore.you_dont_know_isbn).text

        self.driver.execute_script("window.scrollTo(0, 350);")
        time.sleep(3)
        button_back_to_the_store = self.driver.find_element(by=By.XPATH,
                                                       value=LocatorsBooksStore.back_to_book_store)
        self.driver.execute_script("arguments[0].click();", button_back_to_the_store)
        time.sleep(3)


if __name__ == "__main__":
    TestBooksOpen().test_books_open()