from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.usefixtures("set_up_chrome")
class TestUploadDownload:
    def test_upload_download_file(self):
        self.driver.get("https://demoqa.com/upload-download")
        upload = self.driver.find_element(by=By.XPATH, value="//*[@id='uploadFile']")
        time.sleep(5)
        upload.send_keys("C:/Users/User/Desktop/GIT/Autotests/img/sampleFile.jpeg")
        time.sleep(5)


if __name__ == "__main__":
    TestUploadDownload().test_upload_download_file()
