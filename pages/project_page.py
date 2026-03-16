from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProjectsPage(BasePage):

    NEW_PROJECT_BUTTON = (
        By.XPATH,
        "//button[.//i[contains(@class,'bi-plus-circle')]]"
    )

    PROJECT_TITLE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Title']"
    )

    CREATE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Create')]"
    )

    PROJECT_TABLE = (By.XPATH, "//table")

    def create_project(self, project_name):

        # click "+ New Project"
        self.wait.until(
            EC.element_to_be_clickable(self.NEW_PROJECT_BUTTON)
        ).click()

        # wait for modal input
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TITLE_INPUT)
        )

        # enter project name
        self.find(self.PROJECT_TITLE_INPUT).clear()
        self.find(self.PROJECT_TITLE_INPUT).send_keys(project_name)

        # click Create
        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        ).click()

        # wait for table reload
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    def is_project_visible(self, project_name):

        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")

        for row in rows:
            if project_name.lower() in row.text.lower():
                return True

        return False
