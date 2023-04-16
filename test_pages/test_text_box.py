from src.pages.text_box.text_box_page import TextBoxPage
from generators.text_box_gen import TextBoxGen
import pytest


@pytest.mark.usefixtures("set_up_chrome")
class TestTextBox:
    @pytest.mark.parametrize("link, user_name, user_email, current_address, permanent_address ",
                             [("https://demoqa.com/text-box", TextBoxGen.name_gen, TextBoxGen.email_gen,
                               TextBoxGen.current_address_gen, TextBoxGen.permanent_address_gen)
                              ])
    def test_text_box(self, link, user_name, user_email, current_address, permanent_address):
        """
        Данная функция работает со страничкой https://demoqa.com/text-box.
        Сначала заполняем форму значениями из генератора,
        Затем осуществляем последовательную проверку внесенных значений.
        """
        self.driver.get(link)
        self.text_box = TextBoxPage(self.driver)
        self.text_box.add_user_name(user_name)
        self.text_box.add_user_email(user_email)
        self.text_box.add_current_address(current_address)
        self.text_box.add_permanent_address(permanent_address)
        self.text_box.add_values()
        assert self.text_box.assert_values_user_name() == f"Name:{user_name}"
        assert self.text_box.assert_values_user_email() == f"Email:{user_email}"
        assert self.text_box.assert_values_current_address() == f"Current Address :{current_address}"
        assert self.text_box.assert_values_permanent_address() == f"Permananet Address :{permanent_address}"


if __name__ == "__main__":
    TestTextBox().test_text_box()
