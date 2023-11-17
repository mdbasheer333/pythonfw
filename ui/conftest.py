import pytest
import os

from ui.core.DriverListenerFactory import DriverFactory


@pytest.fixture(scope="function")
def browser(browser_config, browser_cmdln):
    browser_type = browser_config if browser_cmdln is None else browser_cmdln
    driver = DriverFactory.get_driver(browser_type)
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
        driver = feature_request.getfixturevalue('browser')
        pth = os.path.abspath(os.curdir) + "\\testresults\\screenshots\\" + \
              report.nodeid.replace("::", "_").split(".py")[1] + '.png'
        driver.save_screenshot(pth)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.image(pth))
            extra.append(pytest_html.extras.html('<div>FAIL REASON</div>'))
        report.extra = extra
