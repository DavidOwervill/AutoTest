from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def set_up_chrome(request):
    # настройка для не открывающегося окна браузера
    # self.chrome_options = Options()
    # self.chrome_options.add_argument("--headless")
    # конец настройки неоткрывающегося окна
    driver = webdriver.Chrome() #options=self.chrome_options
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.fixture(scope="class")
# def set_up_ff(request):
#     ff_driver = webdriver.Firefox()
#     request.cls.driver = ff_driver
#     yield
#     ff_driver.close()