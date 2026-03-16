from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UsersPage(BasePage):

    USERS_TABLE = (By.TAG_NAME, "table")

    def is_users_table_visible(self):
        return self.is_element_visible(self.USERS_TABLE)