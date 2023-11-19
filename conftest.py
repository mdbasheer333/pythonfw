import os
import logging
import pytest
from dotenv import load_dotenv
from dotenv import dotenv_values


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
    logging.info("env is " + env_to_load)
    config = dotenv_values(os.path.abspath(os.curdir) + "\\configs\\" + env_to_load)
    return config
