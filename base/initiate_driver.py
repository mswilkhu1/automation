from selenium import webdriver
from lib import conf_reader


def start_browser():
    global driver

    if (conf_reader.read_config_data('Details', 'Browser')) == "Chrome":
        driver = webdriver.Chrome()

    elif (conf_reader.read_config_data('Details', 'Browser')) == "Firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.get(conf_reader.read_config_data('Details', 'Application_Url'))
    driver.maximize_window()
    return driver


def close_browser():
    driver.close()
