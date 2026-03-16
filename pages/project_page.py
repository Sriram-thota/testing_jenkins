from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    CREATE_BUTTON = (By.XPATH, "//button[contains(.,'Create')]")
    PROJECT_NAME_INPUT = (By.XPATH, "//input[@placeholder='Project Name']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")

    PROJECT_TABLE = (By.XPATH, "//table")

    def create_project(self, project_name):

        self.click(self.CREATE_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_NAME_INPUT)
        )

        self.find(self.PROJECT_NAME_INPUT).send_keys(project_name)

        self.click(self.SAVE_BUTTON)

        # wait for table to reload
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    def is_project_visible(self, project_name):

        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")

        for row in rows:
            if project_name.lower() in row.text.lower():
                return True

        return False
