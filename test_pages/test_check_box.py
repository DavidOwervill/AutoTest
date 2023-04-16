from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time, logging


class LocatorsCheckBox:
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

@pytest.mark.usefixtures("set_up_chrome")
class TestCheckBox:

    def test_check_box(self):
        """
        Данная функция работает с https://demoqa.com/checkbox.
        В данной функции последовательно проверяется нажатие на галочку возле соответствующей директории и
        возможность попасть внутрь.
        Порядок проверки следующий - Home -> Desktop -> Documents -> Downloads -> Notes ->Commands->
        WorkSpace -> Office -> React -> Angular -> Vue -> Public -> Private -> Classified -> General ->
        Word file.doc -> Excel File.doc
        """
        self.driver.get(
            "https://demoqa.com/checkbox")
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_check_box).click()
        assert "home" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_title).text
        time.sleep(5)

        # Опускаемся на 1 слой глубже

        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_check_box).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=LocatorsCheckBox.first_level_aria_button).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_check_box).click()
        assert "desktop" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_title).text
        #logging.info('Desktop checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_check_box).click()
        assert "documents" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_title).text
        logging.info('Documents checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_check_box).click()
        assert "downloads" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_title).text
        logging.info('Downloads checked')
        time.sleep(5)

        # Опускаемся на 1 слой глубже в разделе Desktop

        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_level_aria_button).click()

        # Опустились

        logging.info('Down to the Desktop level')
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.notes_check_box).click()
        assert "notes" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.notes_title).text
        logging.info('Notes checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.notes_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.commands_check_box).click()
        assert "commands" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.commands_title).text
        logging.info('Commands checked')
        time.sleep(5)

        # Следующим действием выходим из desktop

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.commands_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_level_aria_button).click()
        logging.info('Down to the Documents level')
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_level_aria_button).click()

        # Опустились на уровень Documents

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.workspace_check_box).click()
        assert "workspace" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_title).text
        logging.info("WorkSpace checked")
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.workspace_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.office_check_box).click()
        assert "office" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_title).text
        logging.info("Office checked")

        # Проваливаемся на 1 уровень ниже в рамках Documents

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.office_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()

        # Работаем со вложением WorkSpace

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.react_check_box).click()
        assert "react" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.react_title).text
        logging.info('React checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.react_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.angular_check_box).click()
        assert "angular" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Angular checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.angular_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.veu_check_box).click()
        assert "veu" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Veu Checked')
        time.sleep(5)

        # Выходим из уровня workspace

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.veu_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_level_aria_button).click()

        # Работаем с уровнем Office

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.public_check_box).click()
        assert "public" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('public checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.public_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.private_check_box).click()
        assert "private" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Private was checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.private_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.classified_check_box).click()
        assert "classified" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Classified was checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.classified_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.general_check_box).click()
        self.driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        assert "general" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('General was checked')
        time.sleep(5)

        # Выходим из уровня Office

        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.general_check_box).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_level_aria_button).click()
        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()

        # Падаем в уровень Downloads

        self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_level_aria_button).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.wordfile_check_box).click()
        assert "wordFile" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Word File checked')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.wordfile_check_box).click()
        self.driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.excelfile_check_box).click()
        assert "excelFile" == self.driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text
        logging.info('Excel File checked')
        time.sleep(5)


if __name__ == "__main__":
    TestCheckBox().test_check_box()