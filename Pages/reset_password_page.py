import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from OrangeHRMTesting.Pages.login_page import LoginPage


class ResetPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.json_path = r"D:\2024\Nandini Software\Day31\OrangeHRMTesting\config\config.json"
        self.screenshot_path = r"D:\2024\Nandini Software\Day31\reports\screenshots\\"
        with open(self.json_path, "r") as json_file:
            jf = json_file.read()
            self.json_data = json.loads(jf)

        self.url = self.json_data["LoginPage"]["url"]

    locators = {
        "username_locator": (By.NAME, "username"),
        "reset_password_button_locator": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'),
        "reset_password_success_msg_locator": (By.TAG_NAME, 'h6'),
        "cancel_button": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')
    }

    def find_element(self, element):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        return ele

    def enter_username(self, element, username):
        element.send_keys(username)

    def click_element(self, element):
        element.click()

    def get_text_from_element(self, element):
        return element.text

    def reset_password(self):
        loginpage = LoginPage(self.driver)
        self.driver.get(self.url)
        forgot_password_loc = loginpage.locators["forgot_password_locator"]
        forgot_password_elem = self.find_element(forgot_password_loc)
        self.click_element(forgot_password_elem)
        username_loc = self.locators["username_locator"]
        username_elem = self.find_element(username_loc)
        username = self.json_data["LoginPage"]["user_name"]
        reset_password_loc = self.locators["reset_password_button_locator"]
        reset_password_elem = self.find_element(reset_password_loc)

        self.enter_username(username_elem, username)
        self.click_element(reset_password_elem)

        reset_password_success_msg_loc = self.locators["reset_password_success_msg_locator"]
        reset_password_success_msg_elem = self.find_element(reset_password_success_msg_loc)

        success_msg = self.get_text_from_element(reset_password_success_msg_elem)

        if success_msg == self.json_data["ResetPasswordPage"]["success_msg"]:
            return True
        else:
            return False

    def reset_password_cancel(self):
        loginpage = LoginPage(self.driver)
        self.driver.get(self.url)
        forgot_password_loc = loginpage.locators["forgot_password_locator"]
        forgot_password_elem = self.find_element(forgot_password_loc)
        self.click_element(forgot_password_elem)

        cancel_button_loc = self.locators["cancel_button"]
        cancel_button_elem = self.find_element(cancel_button_loc)
        self.click_element(cancel_button_elem)

        current_url = self.driver.current_url

        if current_url == self.json_data["LoginPage"]["url"]:
            return True
        else:
            return False


