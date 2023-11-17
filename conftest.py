import os
import logging
import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="this brower cmd line var to accept browser from cmdline")
    parser.addoption("--environment", action="store", default="qa",
                     help="ths is to read value from cmd line")


@pytest.fixture(scope="session")
def browser_cmdln(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def author(request):
    return request.config.getoption("--author")


@pytest.fixture(scope="session")
def browser_env(request):
    env_to_load = '.env.' + request.config.getoption("--environment")
    logging.info("env to load is " + env_to_load)
    load_dotenv(dotenv_path=os.path.abspath(os.curdir) + "\\" + env_to_load)
    logging.info("browser is " + request.config.getoption("browser"))
    return os.getenv("browser")
