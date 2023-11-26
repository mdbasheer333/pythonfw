import os

import allure
import pytest
from allure import attachment_type

from ui.core.DriverListenerFactory import DriverFactory
from ui.utils import logger, allurelog
from ui.utils.CommonLib import CommonLib


@pytest.fixture(scope="function")
def browser(config, browser_cmdln):
    browser_type = config['browser'] if browser_cmdln == None else browser_cmdln
    allurelog.log_step(f"browser is {browser_type}")
    driver = DriverFactory.get_driver(browser_type)
    yield driver
    allurelog.log_step(f"browser is closed...!")
    driver.quit()


def pytest_html_report_title(report):
    report.title = "test results!"


def pytest_configure(config):
    pass


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if "ui/tests" in report.nodeid and report.when == 'setup':
        logger.logger.info(f"---------------{report.nodeid} test execution started----------------")
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        fl_name = report.nodeid.replace("::", "_").split(".py")[1] + '.png'
        pth = CommonLib.get_timestamp_folder() + "screenshots/" + fl_name
        driver.save_screenshot("./testresults/" + pth)
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            allure.attach.file(os.path.join("", "./testresults/" + pth), name="PNG example",
                               attachment_type=attachment_type.PNG)
            extra.append(pytest_html.extras.image("../" + pth, 'screenshot'))
            extra.append(pytest_html.extras.html('<div>FAIL REASON</div>'))
        report.extra = extra
    if report.when == 'teardown':
        logger.logger.info(f"---------------{report.nodeid} test execution ended----------------")
