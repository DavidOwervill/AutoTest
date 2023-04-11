import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class LocatorsButtons:
    find_double_click = '//*[@id="doubleClickBtn"]'
    double_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]"
    find_right_click = '//*[@id="rightClickBtn"]'
    right_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]"
    find_dynamic_click = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button'
    dynamic_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[3]"


@pytest.mark.usefixtures("set_up_chrome")
class TestButtons:
    @pytest.mark.parametrize('link, assert_check_double_click, assert_check_right_click, assert_check_dynamic_click',
                             [
                                 ('https://demoqa.com/buttons', "You have done a double click", "You have done a right click",
                                  "You have done a dynamic click")
                             ])
    def test_buttons(self, link, assert_check_double_click, assert_check_right_click, assert_check_dynamic_click):
        """
        Данная функция проводит проверку работы сайта https://demoqa.com/buttons.
        Вводит 3 переменные и далее с помощью ActionChains выполняет:
        double_click().perform() - двойной клик,
        context_click().perform() - клик правой кнопкой мыши,
        click().perform() - обычный клик левой кнопкой мыши.

        """
        self.driver.get(link)

        # Создаем переменную для двойного клика

        double_click = self.driver.find_element(by=By.XPATH, value=LocatorsButtons.find_double_click)
        action = ActionChains(self.driver)
        action.double_click(double_click).perform()
        time.sleep(5)
        assert assert_check_double_click == self.driver.find_element(by=By.XPATH,
                                                                     value=LocatorsButtons.double_click).text

        # Создаем переменную для правого клика

        right_click = self.driver.find_element(by=By.XPATH, value=LocatorsButtons.find_right_click)
        action.context_click(right_click).perform()
        time.sleep(5)
        assert assert_check_right_click == self.driver.find_element(by=By.XPATH,
                                                                    value=LocatorsButtons.right_click).text

        # Создаем переменную для левого клика

        left_click = self.driver.find_element(by=By.XPATH,
                                              value=LocatorsButtons.find_dynamic_click)
        action.click(left_click).perform()
        time.sleep(5)
        assert assert_check_dynamic_click == self.driver.find_element(by=By.XPATH,
                                                                      value=LocatorsButtons.dynamic_click).text


if __name__ == "__main__":
    TestButtons().test_buttons()
