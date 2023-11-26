import os

import pytest
from dotenv import dotenv_values

from ui.utils import logger, allurelog
from ui.utils.CommonLib import CommonLib


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None,
                     help="this browser cmd line var to accept browser from cmdline")
    parser.addoption("--env", action="store", default="qa",
                     help="ths is to read env value from cmd line")


@pytest.fixture(scope="session")
def browser_cmdln(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def config(request):
    env_to_load = request.config.getoption("--env") + '.env'
    logger.logger.info(f"env is {env_to_load}")
    allurelog.log_step(f"env is {env_to_load}")
    config = dotenv_values(os.path.abspath(os.curdir) + "\\configs\\" + env_to_load)
    return config


def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        outcome = call.excinfo if call.excinfo else None
        CommonLib.set_global_test_results(
            {'TC_Name': item.name, 'Status': 'Failed' if outcome else 'Passed'})
