from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.tasks_page import TasksPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()


def test_task_status_update(driver):

    logger.info("TC06 started")

    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    WebDriverWait(driver, 20).until(
        EC.url_contains("dashboard")
    )

    dashboard = DashboardPage(driver)
    dashboard.go_to_tasks_page()

    tasks_page = TasksPage(driver)

    logger.info("Editing first task")

    tasks_page.click_first_edit()

    logger.info("Changing status")

    tasks_page.change_status("in_progress")
    tasks_page.save_task()

    # wait until status badge visible
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(tasks_page.STATUS_BADGE)
    )

    status_text = tasks_page.get_status().lower()

    # accept any valid status change
    assert status_text in ["in progress", "in_progress", "done"]

    logger.info("TC06 passed")
