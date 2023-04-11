from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
import time


class LocatorsTextBox:
    user_name = "userName"
    user_name_check = "//*[@id='name']"
    user_email = "userEmail"
    user_email_check = "//*[@id='email']"
    current_address = "currentAddress"
    ca_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]"
    permanent_address = "permanentAddress"
    pa_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]"
    test_user_name = "Full Name Test Write"
    test_user_email = "testmail@gmail.com"
    test_current_address = "Test Current Address"
    test_permanent_address = 'Test Permanent Address'


@pytest.mark.usefixtures("set_up_chrome")
class TestTextBox:
    def test_text_box(self):
        """
        Данная функция работает со страничкой https://demoqa.com/text-box.
        Сначала заполняем форму следующими значениями -
        Full Name Test Write,
        testmail@gmail.com,
        Test Current Address,
        Test Permanent Address.
        Затем осуществляем последовательную проверку внесенных значений.
        """
        self.driver.get("https://demoqa.com/text-box")
        self.driver.find_element(by=By.ID, value=LocatorsTextBox.user_name).send_keys(LocatorsTextBox.test_user_name)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=LocatorsTextBox.user_email).send_keys(LocatorsTextBox.test_user_email)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=LocatorsTextBox.current_address).send_keys(
            LocatorsTextBox.test_current_address)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value=LocatorsTextBox.permanent_address).send_keys(
            LocatorsTextBox.test_permanent_address)
        time.sleep(3)
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.ID, value="submit").click()
        time.sleep(10)
        assert f"Name:{LocatorsTextBox.test_user_name}" == self.driver.find_element(by=By.XPATH,
                                                                                    value=LocatorsTextBox.user_name_check).text
        assert f"Email:{LocatorsTextBox.test_user_email}" == self.driver.find_element(by=By.XPATH,
                                                                                      value=LocatorsTextBox.user_email_check).text
        assert f"Current Address :{LocatorsTextBox.test_current_address}" == self.driver.find_element(by=By.XPATH,
                                                                                                      value=LocatorsTextBox.ca_check).text
        assert f"Permananet Address :{LocatorsTextBox.test_permanent_address}" == self.driver.find_element(by=By.XPATH,
                                                                                                           value=LocatorsTextBox.pa_check).text


if __name__ == "__main__":
    TestTextBox().test_text_box()
