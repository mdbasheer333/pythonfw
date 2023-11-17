import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def ui_browser(browser_env):
    print("browser is " + browser_env)
    if browser_env == "chrome":
        service = Service()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_env == "ff":
        driver = webdriver.Firefox()
    elif browser_env == "edge":
        driver = webdriver.Edge()
    elif browser_env == "remote_chrome":
        browser_capabilities = {
            "platformName": "Windows 7",
            "browserName": "Chrome",
            "browserVersion": "109.0.5414.120"
        }
        driver = webdriver.Remote(
            command_executor="http://10.0.0.10:4444",
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    else:
        raise Exception("given wrong browser name ", browser_env)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_html_report_title(report):
    report.title = "YXZ org test results!"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('ui_browser')
        pth = os.path.abspath(os.curdir) + "\\testresults\\screenshots\\" + \
              report.nodeid.replace("::", "_").split(".py")[1] + '.png'
        driver.save_screenshot(pth)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.image(pth))
            extra.append(pytest_html.extras.html('<div>FAIL REASON</div>'))
        report.extra = extra
