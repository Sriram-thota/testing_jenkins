from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProjectsPage(BasePage):

    NEW_PROJECT_BUTTON = (By.XPATH, "//button[contains(.,'New Project')]")

    TITLE_INPUT = (By.XPATH, "//label[text()='Title']/following::input[1]")
    DESCRIPTION_INPUT = (By.XPATH, "//label[text()='Description']/following::textarea[1]")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/following::select[1]")

    SAVE_BUTTON = (By.XPATH, "//div[contains(@class,'modal-body')]//button[contains(.,'Save')]")
    def click_new_project(self):
        self.click(self.NEW_PROJECT_BUTTON)

    def enter_title(self, title):
        self.type(self.TITLE_INPUT, title)

    def enter_description(self, description):
        self.type(self.DESCRIPTION_INPUT, description)

    def select_status(self, status):
        dropdown = Select(self.find(self.STATUS_DROPDOWN))
        dropdown.select_by_value(status)

    def click_save(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        button.click()

    def is_project_visible(self, project_name):
        locator = (By.XPATH, f"//div[@class='fw-semibold' and contains(text(),'{project_name}')]")
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0