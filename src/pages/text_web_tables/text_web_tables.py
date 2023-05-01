from selenium.webdriver.common.by import By
import time


class WebTablesSCR:
    first_name = 'firstName'
    first_name_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]'
    last_name = 'lastName'
    last_name_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]'
    user_email = 'userEmail'
    user_email_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]'
    age = 'age'
    age_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]'
    salary = 'salary'
    salary_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[5]'
    dep = 'department'
    dep_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[6]'
    sub = 'submit'
    check = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[7]/div/span[1]'

    def __init__(self, driver):
        self.driver = driver

    def add_record_button(self):
        self.driver.find_element(by=By.ID, value="addNewRecordButton").click()
        time.sleep(10)

        # Вносим данные в открывшемся окне

    def send_first_name(self, first_name):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.first_name).send_keys(first_name)
        time.sleep(5)

    def send_last_name(self, last_name):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.last_name).send_keys(last_name)
        time.sleep(5)

    def send_email(self, email):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.user_email).send_keys(email)
        time.sleep(5)

    def send_age(self, age):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.age).send_keys(age)
        time.sleep(5)

    def send_salary(self, salary):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.salary).send_keys(salary)
        time.sleep(5)

    def send_dep(self, dep):
        self.driver.find_element(by=By.ID, value=WebTablesSCR.dep).send_keys(dep)
        self.driver.find_element(by=By.ID, value=WebTablesSCR.sub).click()
        time.sleep(15)

        # Проверяем внесение данных в исходную табличку

    def assert_first_name(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.first_name_ck).text

    def assert_last_name(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.last_name_ck).text

    def assert_age(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.age_ck).text

    def assert_email(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.user_email_ck).text

    def assert_salary(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.salary_ck).text

    def assert_dep(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.dep_ck).text

    def scroll_func(self):
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, 250);")
        target_left = self.driver.find_element(by=By.CLASS_NAME, value='action-buttons')
        self.driver.execute_script("arguments[0].scrollIntoView();", target_left)
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(250, 0);")
        self.driver.find_element(by=By.XPATH,
                                 value=WebTablesSCR.check).click()
        time.sleep(5)

        # Проверка изменения

    def change_check(self, first_name_change):
        self.driver.find_element(by=By.ID, value='firstName').clear()
        self.driver.find_element(by=By.ID, value='firstName').send_keys(first_name_change)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value='submit').click()
        time.sleep(5)
        target_right = self.driver.find_element(by=By.CLASS_NAME, value='rt-td')
        self.driver.execute_script("arguments[0].scrollIntoView();", target_right)
        time.sleep(5)

    def assert_first_name_mod(self):
        return self.driver.find_element(by=By.XPATH, value=WebTablesSCR.first_name_ck).text
