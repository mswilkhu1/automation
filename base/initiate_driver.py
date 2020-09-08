from selenium import webdriver
from library import configReader


def start_browser():
    global driver

    if (configReader.read_config_data('Details', 'Browser')) == "Chrome":
        driver = webdriver.Chrome()

    elif (configReader.read_config_data('Details', 'Browser')) == "Firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.get(configReader.read_config_data('Details', 'Application_Url'))
    driver.maximize_window()
    return driver


def close_browser():
    driver.close()
