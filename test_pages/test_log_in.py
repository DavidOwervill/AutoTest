from selenium.webdriver.common.by import By
import pytest
import time
from src.pages.text_log_in.text_log_in import LogInVars


@pytest.mark.usefixtures("set_up_chrome")
class TestLogIn:
    @pytest.mark.parametrize("link, username, password", [
        ('https://demoqa.com/books', 'TestUserName', "David123456789!")
    ])
    def test_log_in_po(self, link, username, password):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться,
        Затем проводится проверка авторизации путем сверки НикНейма на страничке https://demoqa.com/books
        """
        self.driver.get(link)
        self.log_in = LogInVars(self.driver)
        self.log_in.log_in_button_click()
        self.log_in.user_name_val_send(username)
        self.log_in.password_val_send(password)
        self.log_in.log_in_button_check()
        assert username == self.log_in.assert_control_user_name()

    @pytest.mark.skip
    def test_log_in_failed(self, username: str = 11111, password: str = 22222222):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться:
        11111
        22222222
        Затем проводится проверка неудачной авторизации
        """
        self.driver.get("https://demoqa.com/books")
        self.driver.find_element(by=By.XPATH,
                                 value=LogInVars.log_in_button).click()
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="userName").send_keys(username)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="password").send_keys(password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value=LogInVars.log_in_check).click()
        time.sleep(3)
        try:
            self.assertEqual("Invalid username or password!",
                             self.driver.find_element(by=By.XPATH, value=LogInVars.log_in_failed))
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    TestLogIn().test_log_in_po()
