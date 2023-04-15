from selenium.webdriver.common.by import By
from generators.web_tablets_gen import WebTabletsGen
import pytest
import time


class LWebTables:
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


@pytest.mark.usefixtures("set_up_chrome")
class TestWebTables:
    def test_web_tables(self):
        """
        Данная функция работает со страничкой https://demoqa.com/webtables.
        Сначала мы нажимаем на кнопку Add, затем заполняем выпавшую форму следующими значениями -
        Test First Name,
        Test Last Name,
        TestMail@test.com,
        23,
        23,
        Test department.
        Далее методом try/except во внесенной табличке проверяем что данные внесены верно.
        После нажимаем на кнопку исправить и меняем значения поля First name на Test First Name 2.
        Затем повторно в табличке проверяем что значения внесены верно.
        Так же, в данной функции используется проверка скрола вертикального и горизонтального в рамках.
        """
        self.driver.get("https://demoqa.com/webtables")
        self.driver.find_element(by=By.ID, value="addNewRecordButton").click()
        time.sleep(10)

        # Вносим данные в открывшемся окне

        self.driver.find_element(by=By.ID, value=LWebTables.first_name).send_keys(WebTabletsGen.first_name_gen)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=LWebTables.last_name).send_keys(WebTabletsGen.last_name_gen)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=LWebTables.user_email).send_keys(WebTabletsGen.email_gen)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=LWebTables.age).send_keys(WebTabletsGen.age_gen)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=LWebTables.salary).send_keys(WebTabletsGen.solary_gen)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=LWebTables.dep).send_keys(WebTabletsGen.dep_gen)
        self.driver.find_element(by=By.ID, value=LWebTables.sub).click()
        time.sleep(15)

        # Проверяем внесение данных в исходную табличку

        assert f'{WebTabletsGen.first_name_gen}' == self.driver.find_element(by=By.XPATH,
                                                                             value=LWebTables.first_name_ck).text
        assert f'{WebTabletsGen.last_name_gen}' == self.driver.find_element(by=By.XPATH,
                                                                            value=LWebTables.last_name_ck).text
        assert f'{WebTabletsGen.age_gen}' == self.driver.find_element(by=By.XPATH,
                                                                      value=LWebTables.age_ck).text
        assert f'{WebTabletsGen.email_gen}' == self.driver.find_element(by=By.XPATH,
                                                                        value=LWebTables.user_email_ck).text
        assert f'{WebTabletsGen.solary_gen}' == self.driver.find_element(by=By.XPATH,
                                                                         value=LWebTables.salary_ck).text

        assert f'{WebTabletsGen.dep_gen}' == self.driver.find_element(by=By.XPATH,
                                                                      value=LWebTables.dep_ck).text

        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, 250);")
        target_left = self.driver.find_element(by=By.CLASS_NAME, value='action-buttons')
        self.driver.execute_script("arguments[0].scrollIntoView();", target_left)
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(250, 0);")
        self.driver.find_element(by=By.XPATH,
                                 value=LWebTables.check).click()
        time.sleep(5)

        # Проверка изменения

        self.driver.find_element(by=By.ID, value='firstName').clear()
        self.driver.find_element(by=By.ID, value='firstName').send_keys(WebTabletsGen.first_name_gen_changes)
        time.sleep(5)
        self.driver.find_element(by=By.ID, value='submit').click()
        time.sleep(5)
        target_right = self.driver.find_element(by=By.CLASS_NAME, value='rt-td')
        self.driver.execute_script("arguments[0].scrollIntoView();", target_right)
        time.sleep(5)
        assert WebTabletsGen.first_name_gen_changes == self.driver.find_element(by=By.XPATH,
                                                               value=LWebTables.first_name_ck).text


if __name__ == "__main__":
    TestWebTables().test_web_tables()
