import pytest
from selenium.webdriver.common.by import By
import time


class LocatorsBrokenLinks:
    image_tools_qa = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]"
    broken_image_tools_qa = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]"
    valid_links = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[1]"
    broken_links = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[2]"


@pytest.mark.usefixtures("set_up_chrome")
class TestBrokenLink:
    @pytest.mark.parametrize('link, link_assert_1, link_assert_2, link_assert_3, link_assert_4',
                        [("https://demoqa.com/broken",
                          "https://demoqa.com/images/Toolsqa.jpg",
                          "https://demoqa.com/images/Toolsqa_1.jpg",
                          "https://demoqa.com/",
                          "http://the-internet.herokuapp.com/status_codes/500")
                         ])
    def test_broken_link(self, link, link_assert_1, link_assert_2, link_assert_3, link_assert_4):
        """
        Данная функция работает со страничкой https://demoqa.com/broken.
        Для начала, проверяет наличие картинок путем сверки href с заданной и затем делает скриншот.
        Далее нажимает на ссылки и проверяет правильность перехода по нужной ссылке.
        """

        self.driver.get(link)
        assert link_assert_1 == self.driver.find_element(by=By.XPATH,
                                                         value=LocatorsBrokenLinks.image_tools_qa).get_attribute(
            "src")
        assert link_assert_2 == self.driver.find_element(by=By.XPATH,
                                                         value=LocatorsBrokenLinks.broken_image_tools_qa).get_attribute(
            "src")
        self.driver.execute_script("window.scrollTo(0, 250);")
        self.driver.find_element(by=By.XPATH, value=LocatorsBrokenLinks.valid_links).click()
        time.sleep(5)
        url_correct = self.driver.current_url
        self.driver.back()
        assert link_assert_3 == url_correct
        self.driver.execute_script("window.scrollTo(0, 250);")
        self.driver.find_element(by=By.XPATH, value=LocatorsBrokenLinks.broken_links).click()
        time.sleep(5)
        url_uncorrect = self.driver.current_url
        assert link_assert_4 == url_uncorrect
        self.driver.back()


if __name__ == "__main__":
    TestBrokenLink().test_broken_link()
