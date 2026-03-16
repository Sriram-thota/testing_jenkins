from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = get_logger()


def test_non_admin_cannot_access_users(driver):

    logger.info("TC04 started")

    login_page = LoginPage(driver)

    login_page.login_as_user("John@example.com", "User@123")

    dashboard = DashboardPage(driver)

    users_links = driver.find_elements(*dashboard.USERS_LINK)

    assert len(users_links) == 0

    logger.info("TC04 passed - Users menu hidden for non-admin")