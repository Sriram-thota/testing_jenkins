from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    NEW_PROJECT_BUTTON = (By.XPATH, "//button[contains(.,'New Project')]")

    # any visible text input inside modal
    PROJECT_INPUT = (By.XPATH, "//input[@type='text']")

    CREATE_BUTTON = (By.XPATH, "//button[contains(.,'Create')]")

    PROJECT_TABLE = (By.XPATH, "//table")

    def create_project(self, project_name):

        # click "+ New Project"
        self.wait.until(
            EC.element_to_be_clickable(self.NEW_PROJECT_BUTTON)
        ).click()

        # wait for modal input
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_INPUT)
        )

        field = self.find(self.PROJECT_INPUT)
        field.clear()
        field.send_keys(project_name)

        # click Create
        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        ).click()

        # wait until table reloads
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    def is_project_visible(self, project_name):

        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")

        for row in rows:
            if project_name.lower() in row.text.lower():
                return True

        return False
