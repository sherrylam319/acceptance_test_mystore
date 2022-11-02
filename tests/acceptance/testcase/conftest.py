import json

import pytest


from tests.acceptance.utils.driver_factory import DriverFactory
from tests.acceptance.utils.path import *


@pytest.fixture(scope='class')
def config():
    file_to_open = path_param_1() / "MyStore/tests/acceptance/testcase/config.json"
    f = open(file_to_open)
    config_data = json.load(f)
    return config_data

@pytest.fixture(scope='class')
def spreadsheet_id(config):
    spreadsheet_id = config["config"][0]["spreadsheet_id"]
    return spreadsheet_id

@pytest.fixture(scope='class')
def val_range_name(config):
    val_range_name = config["config"][0]["val_range_name"]
    return val_range_name

@pytest.fixture(scope='class')
def key_range_name(config):
    key_range_name = config["config"][0]["key_range_name"]
    return key_range_name


@pytest.fixture(scope='class')
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    request.cls.driver = driver
    yield
    driver.quit()







