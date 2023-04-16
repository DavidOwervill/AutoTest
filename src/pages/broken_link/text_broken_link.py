from selenium.webdriver.common.by import By
import time


class BrokenLinks:
    image_tools_qa = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]"
    broken_image_tools_qa = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]"
    valid_links = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[1]"
    broken_links = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[2]"

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def first_link_check(self):
        return self.driver.find_element(by=By.XPATH, value=BrokenLinks.image_tools_qa).get_attribute("src")

    def second_link_check(self):
        return self.driver.find_element(by=By.XPATH, value=BrokenLinks.broken_image_tools_qa).get_attribute("src")

    def scroll_to(self):
        self.driver.execute_script("window.scrollTo(0, 250);")

    def find_valid_link(self):
        self.driver.find_element(by=By.XPATH, value=BrokenLinks.valid_links).click()
        time.sleep(5)

    def valid_link_check(self):
        url_correct = self.driver.current_url
        self.driver.back()
        return url_correct

    # scroll_to

    def broken_link_check(self):
        self.driver.find_element(by=By.XPATH, value=BrokenLinks.broken_links).click()
        time.sleep(5)
        url_uncorrect = self.driver.current_url
        self.driver.back()
        return url_uncorrect
