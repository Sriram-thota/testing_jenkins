from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.project_page import ProjectsPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()


def test_project_creation_flow(driver):

    logger.info("TC05 started")

    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    WebDriverWait(driver, 20).until(
        EC.url_contains("dashboard")
    )

    dashboard = DashboardPage(driver)
    dashboard.go_to_projects_page()

    projects_page = ProjectsPage(driver)

    project_name = "Automation Test Project"

    logger.info("Creating new project")

    projects_page.create_project(project_name)

    # wait until project appears in table
    WebDriverWait(driver, 20).until(
        lambda d: projects_page.is_project_visible(project_name)
    )

    assert projects_page.is_project_visible(project_name)

    logger.info("TC05 passed")
