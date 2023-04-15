from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class BooksOpenPage:
    git_pocket_guide_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    back_to_book_store_loc = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button"
    learning_java_script_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    designing_evolvable_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    speaking_java_script_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"
    you_dont_know_isbn = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"

    def __init__(self, driver):
        self.driver = driver

    def find_first_book(self):
        self.driver.find_element(by=By.ID, value="see-book-Git Pocket Guide").click()
        time.sleep(3)

    def return_check_isnb_git(self):
        return self.driver.find_element(by=By.XPATH, value=BooksOpenPage.git_pocket_guide_isbn).text

    def back_to_book_store(self):
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                                 value=BooksOpenPage.back_to_book_store_loc).click()
        time.sleep(3)

    def find_second_book_and_go_back(self):
        self.driver.find_element(by=By.ID, value="see-book-Learning JavaScript Design Patterns").click()
        time.sleep(3)

    def return_check_isnb_java(self):
        return self.driver.find_element(by=By.XPATH, value=BooksOpenPage.learning_java_script_isbn).text

    def back_to_book_store_with_up(self):
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH,
                                 value=BooksOpenPage.back_to_book_store_loc).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)

    def find_third_book_and_go_back(self):
        self.driver.find_element(by=By.ID, value="see-book-Designing Evolvable Web APIs with ASP.NET").click()
        time.sleep(3)

    def return_check_isnb_see(self):
        return self.driver.find_element(by=By.XPATH, value=BooksOpenPage.designing_evolvable_isbn).text

    # back_to_book_store_with_up

    def find_four_book_and_go_back(self):
        self.driver.find_element(by=By.ID, value="see-book-Speaking JavaScript").click()
        time.sleep(3)

    def return_check_isnb_speaking(self):
        return self.driver.find_element(by=By.XPATH, value=BooksOpenPage.speaking_java_script_isbn).text

    # back_to_book_store_with_up

    def find_five_book_and_go_back(self):
        self.driver.find_element(by=By.ID, value="see-book-You Don't Know JS").click()
        time.sleep(3)

    def return_check_isnb_you_dont(self):
        return self.driver.find_element(by=By.XPATH, value=BooksOpenPage.you_dont_know_isbn).text

    def back_to_book_store_with_down(self):
        self.driver.execute_script("window.scrollTo(0, 350);")
        time.sleep(3)
        button_back_to_the_store = self.driver.find_element(by=By.XPATH,
                                                            value=BooksOpenPage.back_to_book_store_loc)
        self.driver.execute_script("arguments[0].click();", button_back_to_the_store)
        time.sleep(3)
