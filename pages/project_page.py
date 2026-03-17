from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class ProjectsPage(BasePage):
    NEW_PROJECT_BUTTON  = (By.XPATH, "//button[contains(.,'New Project')]")
    PROJECT_INPUT       = (By.XPATH, "//input[@type='text']")
    DESCRIPTION_INPUT   = (By.XPATH, "//textarea")
    STATUS_DROPDOWN     = (By.XPATH, "//select")
    CREATE_BUTTON       = (By.XPATH, "//button[contains(.,'Create')]")
    SAVE_BUTTON         = (By.XPATH, "//button[contains(.,'Save')]")
    PROJECT_TABLE       = (By.XPATH, "//table")

    # ── individual step methods (used by test) ──────────────────────────────

    def click_new_project(self):
        self.wait.until(
            EC.element_to_be_clickable(self.NEW_PROJECT_BUTTON)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_INPUT)
        )

    def enter_title(self, title):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_INPUT)
        )
        field.clear()
        field.send_keys(title)

    def enter_description(self, description):
        field = self.wait.until(
            EC.visibility_of_element_located(self.DESCRIPTION_INPUT)
        )
        field.clear()
        field.send_keys(description)

    def select_status(self, status):
        dropdown = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_DROPDOWN)
        )
        Select(dropdown).select_by_value(status)

    def click_save(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    # ── convenience method (bundles all steps) ──────────────────────────────

    def create_project(self, project_name):
        self.click_new_project()
        self.enter_title(project_name)
        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    def is_project_visible(self, project_name):
        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")
        for row in rows:
            if project_name.lower() in row.text.lower():
                return True
        return False
