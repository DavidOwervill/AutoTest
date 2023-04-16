from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


class TextBoxPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    user_name = "userName"
    user_name_check = "//*[@id='name']"
    user_email = "userEmail"
    user_email_check = "//*[@id='email']"
    current_address = "currentAddress"
    ca_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]"
    permanent_address = "permanentAddress"
    pa_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]"


    def add_user_name(self, user_name):
        self.driver.find_element(by=By.ID, value=TextBoxPage.user_name).send_keys(user_name)
        time.sleep(3)

    def add_user_email(self, user_email):
        self.driver.find_element(by=By.ID, value=TextBoxPage.user_email).send_keys(user_email)
        time.sleep(3)

    def add_current_address(self, current_address):
        self.driver.find_element(by=By.ID, value=TextBoxPage.current_address).send_keys(
            current_address)
        time.sleep(3)

    def add_permanent_address(self, permanent_address):
        self.driver.find_element(by=By.ID, value=TextBoxPage.permanent_address).send_keys(
            permanent_address)
        time.sleep(3)

    def add_values(self):
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.ID, value="submit").click()
        time.sleep(10)

    def assert_values_user_name(self):
        return self.driver.find_element(by=By.XPATH, value=TextBoxPage.user_name_check).text

    def assert_values_user_email(self):
        return self.driver.find_element(by=By.XPATH, value=TextBoxPage.user_email_check).text

    def assert_values_current_address(self):
        return self.driver.find_element(by=By.XPATH, value=TextBoxPage.ca_check).text

    def assert_values_permanent_address(self):
        return self.driver.find_element(by=By.XPATH, value=TextBoxPage.pa_check).text
