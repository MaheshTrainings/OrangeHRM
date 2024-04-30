import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

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
        "password_locator": (By.NAME, "password"),
        "button_locator": (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]'),
        "invalid_creds_locator": (By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]'),
        "forgot_password_locator": (By.CLASS_NAME, "orangehrm-login-forgot"),
        "reset_password_text_locator": (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/h6')
    }

    def find_element(self, element):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        return ele

    def find_link_element(self, element):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        return ele

    def take_screenshot(self, screenshotname):
        self.driver.save_screenshot(self.screenshot_path + screenshotname)

    def enter_username(self, element, username):
        element.send_keys(username)

    def enter_password(self, element, password):
        element.send_keys(password)

    def click_element(self, element):
        element.click()

    def login(self, username, password):
        self.driver.get(self.url)
        username_loc = self.locators["username_locator"]
        password_loc = self.locators["password_locator"]
        button_loc = self.locators["button_locator"]
        username_field = self.find_element(username_loc)
        password_field = self.find_element(password_loc)
        button = self.find_element(button_loc)
        self.enter_username(username_field, username)
        self.enter_password(password_field, password)
        self.click_element(button)

    def get_login_page_title(self):
        self.driver.get(self.url)
        return self.driver.title

    def username_field_enabled(self):
        self.driver.get(self.url)
        username_loc = self.locators["username_locator"]
        username_field = self.find_element(username_loc)
        return username_field.is_enabled

    def password_field_enabled(self):
        self.driver.get(self.url)
        password_loc = self.locators["password_locator"]
        password_field = self.find_element(password_loc)
        return password_field.is_enabled

    def login_success(self):
        username = self.json_data["LoginPage"]["user_name"]
        password = self.json_data["LoginPage"]["password"]
        self.login(username, password)
        homepage_url = self.json_data["HomePage"]["url"]
        current_url = self.driver.current_url
        if current_url == homepage_url:
            return True
        else:
            return False

    def login_with_invalid_username_and_password(self):
        username = self.json_data["LoginPage"]["invalid_user_name"]
        password = self.json_data["LoginPage"]["invalid_password"]
        self.login(username, password)
        invalid_creds_element = self.find_element(self.locators["invalid_creds_locator"])
        error_message = invalid_creds_element.text
        expected_error_message = self.json_data["LoginPage"]["login_failure_error_message"]
        if error_message == expected_error_message:
            return True
        else:
            return False

    def login_without_password(self):
        self.driver.get(self.url)
        username = self.json_data["LoginPage"]["invalid_user_name"]
        username_loc = self.locators["username_locator"]
        button_loc = self.locators["button_locator"]
        username_element = self.find_element(username_loc)
        button_element = self.find_element(button_loc)
        self.enter_username(username_element, username)
        self.click_element(button_element)
        error_msg_count = self.driver.page_source.count("Required")
        if "Required" in self.driver.page_source and error_msg_count == 1:
            return True
        else:
            return False

    def login_without_username_password(self):
        self.driver.get(self.url)
        button_loc = self.locators["button_locator"]
        button_element = self.find_element(button_loc)
        self.click_element(button_element)
        error_msg_count = self.driver.page_source.count("Required")
        print(error_msg_count)
        if "Required" in self.driver.page_source and error_msg_count == 2:
            return True
        else:
            return False

    def verify_forgot_password_link(self):
        self.driver.get(self.url)
        forgot_password_loc = self.locators["forgot_password_locator"]
        forgot_password_elem = self.find_link_element(forgot_password_loc)
        self.click_element(forgot_password_elem)
        current_url = self.driver.current_url
        expected_url = self.json_data["ResetPasswordPage"]["url"]
        self.find_element(self.locators["reset_password_text_locator"])

        if "Reset Password" in self.driver.page_source and expected_url == current_url:
            return True
        else:
            return False





