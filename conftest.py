import pytest
import json

from selenium import webdriver


@pytest.fixture()
def driver():
    wd = webdriver.Chrome()
    yield wd
    wd.close()

@pytest.fixture()
def config():
    json_path = r"D:\2024\Nandini Software\Day31\OrangeHRMTesting\config\config.json"

    with open(json_path, "r") as json_file:
        jf = json_file.read()
        json_data = json.loads(jf)
        return json_data