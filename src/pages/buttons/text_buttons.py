from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class ButtonsSRC:
    find_double_click = '//*[@id="doubleClickBtn"]'
    double_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]"
    find_right_click = '//*[@id="rightClickBtn"]'
    right_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]"
    find_dynamic_click = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button'
    dynamic_click = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[3]"


    def __init__(self, driver):
        self.driver = driver

    def double_click_find(self):
        double_click = self.driver.find_element(by=By.XPATH, value=ButtonsSRC.find_double_click)
        action = ActionChains(self.driver)
        action.double_click(double_click).perform()
        time.sleep(5)

    def double_click_check(self):
        return self.driver.find_element(by=By.XPATH, value=ButtonsSRC.double_click).text

    # Создаем переменную для правого клика

    def right_click_find(self):
        right_click = self.driver.find_element(by=By.XPATH, value=ButtonsSRC.find_right_click)
        action = ActionChains(self.driver)
        action.context_click(right_click).perform()
        time.sleep(5)

    def right_click_check(self):
        return self.driver.find_element(by=By.XPATH, value=ButtonsSRC.right_click).text

    # Создаем переменную для левого клика

    def left_click_find(self):

        left_click = self.driver.find_element(by=By.XPATH, value=ButtonsSRC.find_dynamic_click)
        action = ActionChains(self.driver)
        action.click(left_click).perform()
        time.sleep(5)

    def left_click_check(self):
        return self.driver.find_element(by=By.XPATH, value=ButtonsSRC.dynamic_click).text
