from selenium.webdriver.common.by import By
import pytest
import time


class LogInVars:
    # Перечень используемых локаторов в виде переменных
    # XPATH
    log_in_button = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button"
    log_in_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button"
    control_user_name = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"
    log_in_failed = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/p"


@pytest.mark.usefixtures("set_up_chrome")
class TestLogInClass:
    @pytest.mark.parametrize("username, password", [
        ('TestUserName', "David123456789!")
    ])
    def test_log_in(self, username, password):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться,
        Затем проводится проверка авторизации путем сверки НикНейма на страничке https://demoqa.com/books
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
        assert username == self.driver.find_element(by=By.XPATH, value=LogInVars.control_user_name).text

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
    TestLogInClass().test_log_in()
