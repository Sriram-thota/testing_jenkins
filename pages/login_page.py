from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Enter password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    ADMIN_BUTTON = (By.XPATH, "//button[contains(.,'Admin')]")
    USER_BUTTON = (By.XPATH, "//button[contains(.,'User')]")

    def select_user_role(self):
        self.click(self.USER_BUTTON)

    def select_admin_role(self):
        self.click(self.ADMIN_BUTTON)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    # Admin login helper
    def login_as_admin(self, username, password):
        self.select_admin_role()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # User login helper
    def login_as_user(self, username, password):
        self.select_user_role()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()