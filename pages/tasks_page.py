from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TasksPage(BasePage):

    FIRST_EDIT_BUTTON = (By.XPATH, "//table//tbody//tr[1]//button[contains(@class,'btn-outline-primary')]")

    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/following::select[1]")

    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")

    STATUS_BADGE = (By.XPATH, "//table//tbody//tr[1]//span[contains(@class,'badge')]")

    def click_first_edit(self):
        self.click(self.FIRST_EDIT_BUTTON)

        self.wait.until(
            EC.visibility_of_element_located(self.STATUS_DROPDOWN)
        )

    def change_status(self, status):
        dropdown = Select(self.find(self.STATUS_DROPDOWN))
        dropdown.select_by_value(status)

   def save_task(self):
        self.click(self.SAVE_BUTTON)

    # wait until table updates
        self.wait.until(
        EC.visibility_of_element_located(self.STATUS_BADGE)
    )

    def get_status(self):
        # always re-find the badge to avoid stale element
        badge = self.wait.until(
            EC.presence_of_element_located(self.STATUS_BADGE)
        )
        return badge.text
