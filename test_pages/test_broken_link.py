import pytest
from src.pages.broken_link.text_broken_link import BrokenLinks


@pytest.mark.usefixtures("set_up_chrome")
class TestBrokenLink:
    @pytest.mark.parametrize('link, link_assert_1, link_assert_2, link_assert_3, link_assert_4',
                        [("https://demoqa.com/broken",
                          "https://demoqa.com/images/Toolsqa.jpg",
                          "https://demoqa.com/images/Toolsqa_1.jpg",
                          "https://demoqa.com/",
                          "http://the-internet.herokuapp.com/status_codes/500")
                         ])
    def test_bl(self, link, link_assert_1, link_assert_2, link_assert_3, link_assert_4):
        """
        Данная функция работает со страничкой https://demoqa.com/broken.
        Для начала, проверяет наличие картинок путем сверки href с заданной и затем делает скриншот.
        Далее нажимает на ссылки и проверяет правильность перехода по нужной ссылке.
        """
        self.driver.get(link)
        self.broken_link = BrokenLinks(self.driver)
        assert self.broken_link.first_link_check() == link_assert_1
        assert self.broken_link.second_link_check() == link_assert_2
        self.broken_link.scroll_to()
        self.broken_link.find_valid_link()
        assert self.broken_link.valid_link_check() == link_assert_3
        self.broken_link.scroll_to()
        assert self.broken_link.broken_link_check() == link_assert_4


if __name__ == "__main__":
    TestBrokenLink().test_bl()
