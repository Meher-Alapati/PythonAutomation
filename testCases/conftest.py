from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path=".\\drivers\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=".\\drivers\\geckodriver.exe")
    else:  # we can replace this with IE also
        driver = webdriver.Chrome(
            executable_path=".\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):  # This method will get the commandline options from CLI
    parser.addoption("--browser")


@pytest.fixture()  # This will return the browser value to the setup method
def browser(request):
    return request.config.getoption("--browser")


# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP Commerce'
    config._metadata['Module Name'] = 'Billing'
    config._metadata['Project Owner'] = 'Mark'


# Hook to modify/Delete Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
