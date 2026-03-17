from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = get_logger()


def test_admin_users_page_access(driver):

    logger.info("TC03 started")

    login_page = LoginPage(driver)

    logger.info("Logging in with admin credentials")
    login_page.login_as_admin("admin@example.com", "Admin@123")

    # wait until dashboard URL appears
    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    dashboard = DashboardPage(driver)

    logger.info("Checking dashboard loaded")
    assert dashboard.is_dashboard_loaded(), "Dashboard did not load"

    logger.info("Opening Users page")
    dashboard.go_to_users_page()

    users_page = UsersPage(driver)

    logger.info("Checking Users table")
    assert users_page.is_users_table_visible(), "Users table not visible"

    logger.info("TC03 passed")
