from selenium.webdriver.common.by import By
import time


class LogInSRC:
    # Перечень используемых локаторов в виде переменных
    # XPATH
    log_in_button = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button"
    log_in_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button"
    control_user_name = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"
    log_in_failed = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/p"
    user_name_loc = 'userName'
    password_loc = 'password'

    def __init__(self, driver):
        self.driver = driver

    def log_in_button_click(self):
        self.driver.find_element(by=By.XPATH,
                                 value=LogInSRC.log_in_button).click()
        time.sleep(3)

    def user_name_val_send(self, username):
        self.driver.find_element(by=By.ID, value=LogInSRC.user_name_loc).send_keys(username)
        time.sleep(3)

    def password_val_send(self, password):
        self.driver.find_element(by=By.ID, value=LogInSRC.password_loc).send_keys(password)
        time.sleep(3)

    def log_in_button_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=LogInSRC.log_in_check).click()
        time.sleep(3)

    def assert_control_user_name(self):
        return self.driver.find_element(by=By.XPATH, value=LogInSRC.control_user_name).text
