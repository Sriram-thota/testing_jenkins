from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.config import BROWSER, EXECUTION_MODE, GRID_URL, HEADLESS_MODE


class DriverFactory:

    @staticmethod
    def create_driver():

        if EXECUTION_MODE == "remote":
            return DriverFactory._create_remote_driver()

        return DriverFactory._create_local_driver()

    @staticmethod
    def _create_local_driver():

        if BROWSER.lower() == "chrome":

            options = ChromeOptions()

            if HEADLESS_MODE:
                options.add_argument("--headless")

            driver = webdriver.Chrome(options=options)

        elif BROWSER.lower() == "firefox":

            options = FirefoxOptions()

            if HEADLESS_MODE:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception("Unsupported browser")

        driver.maximize_window()

        return driver

    @staticmethod
    def _create_remote_driver():

        if BROWSER.lower() == "chrome":

            options = ChromeOptions()

        elif BROWSER.lower() == "firefox":

            options = FirefoxOptions()

        else:
            raise Exception("Unsupported browser")

        if HEADLESS_MODE:
            options.add_argument("--headless")

        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )

        driver.maximize_window()

        return driver