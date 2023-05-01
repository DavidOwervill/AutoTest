from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class CheckBoxSRC:
    # XPATH
    home_check_box = "//*[@id='tree-node']/ol/li/span/label/span[1]"
    home_title = "//*[@id='result']/span[2]"
    desktop_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]"
    desktop_title = "//*[@id='result']/span[2]"
    documents_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]"
    documents_title = "//*[@id='result']/span[2]"
    documents_level_aria_button = "//*[@id='tree-node']/ol/li/ol/li[2]/span/button"
    downloads_check_box = "//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]"
    downloads_title = "//*[@id='result']/span[2]"
    downloads_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button'
    desktop_level_aria_button = "//*[@id='tree-node']/ol/li/ol/li[1]/span/button"
    notes_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]"
    notes_title = "//*[@id='result']/span[2]"
    commands_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]"
    commands_title = "//*[@id='result']/span[2]"
    workspace_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]"
    workspace_title = "//*[@id='result']/span[2]"
    workspace_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button'
    office_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]"
    office_title = "//*[@id='result']/span[2]"
    office_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button'
    react_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]'
    react_title = "//*[@id='result']/span[2]"
    angular_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]'
    title_check = "//*[@id='result']/span[2]"
    veu_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]'
    public_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]'
    private_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]'
    classified_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]'
    general_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]'
    wordfile_check_box = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]'
    excelfile_check_box = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]'
    # CSS
    first_level_aria_button = ".rct-collapse.rct-collapse-btn"

    def __init__(self, driver):
        self.driver = driver

    def home_click(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.home_check_box).click()
        assert "home" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.home_title).text
        time.sleep(5)

    def one_level_down(self):

        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.home_check_box).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=CheckBoxSRC.first_level_aria_button).click()

    def desktop_check(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.desktop_check_box).click()
        assert "desktop" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.desktop_title).text
        # logging.info('Desktop checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.desktop_check_box).click()

    def documents_check(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.documents_check_box).click()
        assert "documents" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.documents_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.documents_check_box).click()

    def downloads_check(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.downloads_check_box).click()
        assert "downloads" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.downloads_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.downloads_check_box).click()


    def desktop_level_down(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.desktop_level_aria_button).click()


    def notes_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.notes_check_box).click()
        assert "notes" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.notes_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.notes_check_box).click()

    def commands_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.commands_check_box).click()
        assert "commands" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.commands_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.commands_check_box).click()

    def go_out_from_desktop_level(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.desktop_level_aria_button).click()

    def documents_level_down(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.documents_level_aria_button).click()


    def workspace_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.workspace_check_box).click()
        assert "workspace" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.workspace_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.workspace_check_box).click()

    def office_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.office_check_box).click()
        assert "office" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.office_title).text


        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.office_check_box).click()

    def workspace_download_level_down(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.workspace_level_aria_button).click()


    def react_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.react_check_box).click()
        assert "react" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.react_title).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.react_check_box).click()

    def angular_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.angular_check_box).click()
        assert "angular" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.angular_check_box).click()

    def veu_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.veu_check_box).click()
        assert "veu" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.veu_check_box).click()

    def workspace_download_level_out(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.workspace_level_aria_button).click()

    def office_download_level_down(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.office_level_aria_button).click()


    def public_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.public_check_box).click()
        assert "public" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.public_check_box).click()

    def private_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.private_check_box).click()
        assert "private" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.private_check_box).click()

    def classified_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.classified_check_box).click()
        assert "classified" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.classified_check_box).click()

    def general_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.general_check_box).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        assert "general" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.general_check_box).click()

    def office_download_level_out(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.office_level_aria_button).click()
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.workspace_level_aria_button).click()


    def download_level_down(self):
        self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.downloads_level_aria_button).click()

    def word_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.wordfile_check_box).click()
        assert "wordFile" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.wordfile_check_box).click()

    def excel_check(self):
        self.driver.find_element(by=By.XPATH,
                                 value=CheckBoxSRC.excelfile_check_box).click()
        assert "excelFile" == self.driver.find_element(by=By.XPATH, value=CheckBoxSRC.title_check).text

        time.sleep(5)
