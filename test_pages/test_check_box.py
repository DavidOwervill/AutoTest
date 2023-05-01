import pytest
from src.pages.check_box.text_check_box import CheckBoxSRC


@pytest.mark.usefixtures("set_up_chrome")
class TestCheckBox:
    @pytest.mark.parametrize('link',
                             [
                                 ('https://demoqa.com/checkbox')
                             ])
    def test_check_box_PO(self, link):
        """
        Данная функция работает с https://demoqa.com/checkbox.
        В данной функции последовательно проверяется нажатие на галочку возле соответствующей директории и
        возможность попасть внутрь.
        Порядок проверки следующий - Home -> Desktop -> Documents -> Downloads -> Notes ->Commands->
        WorkSpace -> Office -> React -> Angular -> Vue -> Public -> Private -> Classified -> General ->
        Word file.doc -> Excel File.doc
        """
        self.driver.get(link)
        self.check_box = CheckBoxSRC(self.driver)
        self.check_box.home_click()
        self.check_box.one_level_down()
        self.check_box.desktop_check()
        self.check_box.documents_check()
        self.check_box.downloads_check()
        self.check_box.desktop_level_down()
        self.check_box.notes_check()
        self.check_box.commands_check()
        self.check_box.go_out_from_desktop_level()
        self.check_box.documents_level_down()
        self.check_box.workspace_check()
        self.check_box.office_check()
        self.check_box.workspace_download_level_down()
        self.check_box.react_check()
        self.check_box.angular_check()
        self.check_box.veu_check()
        self.check_box.workspace_download_level_out()
        self.check_box.office_download_level_down()
        self.check_box.public_check()
        self.check_box.private_check()
        self.check_box.classified_check()
        self.check_box.general_check()
        self.check_box.office_download_level_out()
        self.check_box.download_level_down()
        self.check_box.word_check()
        self.check_box.excel_check()


if __name__ == "__main__":
    TestCheckBox().test_check_box_PO()
