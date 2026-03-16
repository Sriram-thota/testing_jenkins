from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    # Sidebar navigation links
    DASHBOARD_LINK = (By.XPATH, "//a[@href='/dashboard']")
    USERS_LINK = (By.XPATH, "//a[@href='/users']")
    PROJECTS_LINK = (By.XPATH, "//a[@href='/projects']")
    TASKS_LINK = (By.XPATH, "//a[@href='/tasks']")
    TEST_SCENARIOS_LINK = (By.XPATH, "//a[@href='/test-scenarios']")

    # Correct dashboard verification locator
    DASHBOARD_TITLE = (By.XPATH, "//h2[contains(text(),'Dashboard')]")

    def is_dashboard_loaded(self):
        return self.is_element_visible(self.DASHBOARD_TITLE)

    def go_to_users_page(self):
        self.click(self.USERS_LINK)

    def go_to_projects_page(self):
        self.click(self.PROJECTS_LINK)

    def go_to_tasks_page(self):
        self.click(self.TASKS_LINK)

    def go_to_test_scenarios(self):
        self.click(self.TEST_SCENARIOS_LINK)