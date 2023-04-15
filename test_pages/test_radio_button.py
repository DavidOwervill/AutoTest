from selenium.webdriver.common.by import By
import pytest
import time


class LocatorsRadioButton:
    you_have_selected = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/p"
    yes_button = "custom-control-label"
    impressive_button = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label"


@pytest.mark.usefixtures("set_up_chrome")
class TestRadioButton:
    @pytest.mark.parametrize("selected_1, selected_2",
                             [("You have selected Yes", "You have selected Impressive")]
                             )
    def test_radio_button(self, selected_1, selected_2):
        """
        Данная функция работает с сайтом https://demoqa.com/radio-button.
        Проверяет нажатие на кнопку Yes, Impressive.
        Кнопка No не действительна.

        """
        driver = self.driver
        driver.get("https://demoqa.com/radio-button")

        driver.find_element(by=By.CLASS_NAME, value=LocatorsRadioButton.yes_button).click()
        time.sleep(15)
        assert selected_1 == driver.find_element(by=By.XPATH,
                                                 value=LocatorsRadioButton.you_have_selected).text

        driver.find_element(by=By.XPATH, value=LocatorsRadioButton.impressive_button).click()
        time.sleep(15)
        assert selected_2 == driver.find_element(by=By.XPATH,
                                                 value=LocatorsRadioButton.you_have_selected).text


if __name__ == "__main__":
    TestRadioButton().test_radio_button()
