import pytest
from src.pages.buttons.text_buttons import ButtonsSRC


@pytest.mark.usefixtures("set_up_chrome")
class TestButtons:
    @pytest.mark.parametrize('link, assert_check_double_click, assert_check_right_click, assert_check_dynamic_click',
                             [
                                 ('https://demoqa.com/buttons', "You have done a double click",
                                  "You have done a right click",
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
        self.buttons = ButtonsSRC(self.driver)
        self.buttons.double_click_find()
        assert self.buttons.double_click_check() == assert_check_double_click
        self.buttons.right_click_find()
        assert self.buttons.right_click_check() == assert_check_right_click
        self.buttons.left_click_find()
        assert self.buttons.left_click_check() == assert_check_dynamic_click


if __name__ == "__main__":
    TestButtons().test_buttons()
