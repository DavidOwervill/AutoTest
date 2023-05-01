from generators.web_tablets_gen import WebTabletsGen
from src.pages.text_web_tables.text_web_tables import WebTablesSCR
import pytest


@pytest.mark.usefixtures("set_up_chrome")
class TestWebTables:

    @pytest.mark.parametrize('link, first_name, last_name, email, age, salary, dep, first_name_change',
                             [(
                                     "https://demoqa.com/webtables",
                                     WebTabletsGen.first_name_gen,
                                     WebTabletsGen.last_name_gen,
                                     WebTabletsGen.email_gen,
                                     WebTabletsGen.age_gen,
                                     WebTabletsGen.solary_gen,
                                     WebTabletsGen.dep_gen,
                                     WebTabletsGen.first_name_gen_changes
                             )])
    def test_web_tables_po(self, link, first_name, last_name, email, age, salary, dep, first_name_change):
        self.driver.get("https://demoqa.com/webtables")
        self.web_tablet = WebTablesSCR(self.driver)
        self.web_tablet.add_record_button()
        self.web_tablet.send_first_name(first_name)
        self.web_tablet.send_last_name(last_name)
        self.web_tablet.send_email(email)
        self.web_tablet.send_age(age)
        self.web_tablet.send_salary(salary)
        self.web_tablet.send_dep(dep)
        assert self.web_tablet.assert_first_name() == first_name
        assert self.web_tablet.assert_last_name() == last_name
        assert self.web_tablet.assert_email() == email
        assert self.web_tablet.assert_age() == str(age)
        assert self.web_tablet.assert_salary() == str(salary)
        assert self.web_tablet.assert_dep() == dep
        self.web_tablet.scroll_func()
        self.web_tablet.change_check(first_name_change)
        assert self.web_tablet.assert_first_name_mod() == first_name_change


if __name__ == "__main__":
    TestWebTables().test_web_tables_po()
