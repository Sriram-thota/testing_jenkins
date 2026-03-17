from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProjectsPage(BasePage):
    # ── Locators (using exact IDs from the HTML) ─────────────────────────────
    NEW_PROJECT_BUTTON  = (By.ID, "projects-new-btn")
    TITLE_INPUT         = (By.ID, "projects-title-input")
    DESCRIPTION_INPUT   = (By.ID, "projects-description-input")
    STATUS_SELECT       = (By.ID, "projects-status-select")
    SAVE_BUTTON         = (By.ID, "projects-save-btn")
    CANCEL_BUTTON       = (By.ID, "projects-cancel-btn")
    PROJECT_TABLE       = (By.XPATH, "//table")

    # ── Individual step methods (called by test) ──────────────────────────────

    def click_new_project(self):
        self.wait.until(
            EC.element_to_be_clickable(self.NEW_PROJECT_BUTTON)
        ).click()
        # wait for modal to appear
        self.wait.until(
            EC.visibility_of_element_located(self.TITLE_INPUT)
        )

    def enter_title(self, title):
        field = self.wait.until(
            EC.visibility_of_element_located(self.TITLE_INPUT)
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
            EC.visibility_of_element_located(self.STATUS_SELECT)
        )
        Select(dropdown).select_by_value(status)

    def click_save(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()
        # wait for modal to close and table to reload
        self.wait.until(
            EC.invisibility_of_element_located(self.SAVE_BUTTON)
        )
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    # ── Convenience method (bundles all steps) ────────────────────────────────

    def create_project(self, project_name):
        self.click_new_project()
        self.enter_title(project_name)
        self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        ).click()
        self.wait.until(
            EC.invisibility_of_element_located(self.SAVE_BUTTON)
        )
        self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TABLE)
        )

    # ── Assertion helper ──────────────────────────────────────────────────────

    def is_project_visible(self, project_name):
        rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")
        for row in rows:
            if project_name.lower() in row.text.lower():
                return True
        return False
