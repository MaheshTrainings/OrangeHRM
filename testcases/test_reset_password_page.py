import time

from OrangeHRMTesting.Pages import reset_password_page
from OrangeHRMTesting.Pages.login_page import LoginPage

class TestLoginPage:

    def test_reset_password_by_entering_username(self, driver):
        loginpage = LoginPage(driver)
        resetpasswordpage = reset_password_page.ResetPasswordPage(driver)
        reset_password_success = resetpasswordpage.reset_password()
        if reset_password_success:
            assert True
        else:
            loginpage.take_screenshot("test_reset_password_by_entering_username.png")
            assert False

    def test_reset_password_cancel(self, driver):
        resetpasswordpage = reset_password_page.ResetPasswordPage(driver)
        cancelled_reset_password = resetpasswordpage.reset_password_cancel()
        loginpage = LoginPage(driver)
        if cancelled_reset_password:
            assert True
        else:
            loginpage.take_screenshot("test_reset_password_cancel.png")
            assert False

