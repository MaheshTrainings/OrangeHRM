import time

import pytest

from OrangeHRMTesting.Pages import login_page

class TestLoginPage:

    def test_login_page_title(self, config, driver):
        loginpage = login_page.LoginPage(driver)
        title = loginpage.get_login_page_title()
        assert title == config["LoginPage"]["login_page_title"]

    def test_username_password_fields_enabled(self, driver):
        loginpage = login_page.LoginPage(driver)
        username_field_enabled = loginpage.username_field_enabled()
        password_field_enabled = loginpage.password_field_enabled()

        assert username_field_enabled and password_field_enabled

    def test_login_success(self, driver):
        loginpage = login_page.LoginPage(driver)
        login_success = loginpage.login_success()
        assert login_success

    def test_invalid_usename_password(self, driver):
        loginpage = login_page.LoginPage(driver)
        login_unsuccess = loginpage.login_with_invalid_username_and_password()
        if login_unsuccess:
            assert True
        else:
            loginpage.take_screenshot("test_invalid_usename_password.png")
            assert False

    def test_login_without_password(self, driver):
        loginpage = login_page.LoginPage(driver)
        login_unsuccess = loginpage.login_without_password()
        if login_unsuccess:
            assert True
        else:
            loginpage.take_screenshot("test_login_without_password.png")
            assert False

    def test_login_without_username_password(self, driver):
        loginpage = login_page.LoginPage(driver)
        login_unsuccess = loginpage.login_without_username_password()
        if login_unsuccess:
            assert True
        else:
            loginpage.take_screenshot("test_login_without_username_password.png")
            assert False

    def test_forgot_password_link(self, driver):
        loginpage = login_page.LoginPage(driver)
        open_reset_passwd_page = loginpage.verify_forgot_password_link()
        if open_reset_passwd_page:
            assert True
        else:
            loginpage.take_screenshot("test_forgot_password_link.png")
            assert False
