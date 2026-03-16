from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    NEW_PROJECT_BUTTON = (By.XPATH, "//button[contains(.,'New Project')]")

    PROJECT_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Project') or contains(@name,'title')]"
    )

    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Create') or contains(.,'Save')]")

    PROJECT_TABLE = (By.XPATH, "//table")

    def create_project(self, project_name):

        # click "+ New Project"
        self.wait.until(
            EC.element_to_be_clickable(self.NEW_PROJECT_BUTTON)
        ).click()

        # wait for modal input
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_NAME_INPUT)
        )

        # enter project name
        self.find(self.PROJECT_NAME_INPUT).send_keys(project_name)

        # click Save/Create
        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()

        # wait for table refresh
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    def is_project_visible(self, project_name):

        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")

        for row in rows:
            if project_name.lower() in row.text.lower():
                return True

        return False
