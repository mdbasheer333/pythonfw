import os
import logging
import pytest
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="this browser cmd line var to accept browser from cmdline")
    parser.addoption("--env", action="store", default="qa",
                     help="ths is to read value from cmd line")


@pytest.fixture(scope="session")
def browser_cmdln(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def browser_config(request):
    env_to_load = '.env.' + request.config.getoption("--env")
    logging.info("env to load is " + env_to_load)
    load_dotenv(dotenv_path=os.path.abspath(os.curdir) + "\\" + env_to_load)
    logging.info("browser is " + request.config.getoption("browser"))
    return os.getenv("browser")
