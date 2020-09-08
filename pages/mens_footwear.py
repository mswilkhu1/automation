from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from lib import conf_reader


class MensFootwear:

    def __init__(self, obj):
        global driver
        driver = obj

    def click_filter_button(self):
        try:
            filterButton = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH,
                                                conf_reader.fetch_mens_footwear_elements_locators('MensFootwear',
                                                                                                   'filter_button_xpath'))))
            filterButton.click()
        except TimeoutException:
            print("Loading took too much time!")

    def filter_category(self, category):
        category_filter = driver.find_element_by_id('category-' + category.lower().replace(" ", ""))
        category_filter.click()

    def select_size_filter(self, size):
        size_filter = driver.find_element_by_xpath(
            '//*[@data-qa-filter-size-' + str(size).replace(".", "") + '="true"]')
        driver.execute_script("arguments[0].click();", size_filter)

    def click_apply_filter(self):
        applyFilter = driver.find_element_by_xpath(conf_reader.fetch_mens_footwear_elements_locators('MensFootwear',
                                                                                                      'apply_filter_button'))
        applyFilter.click()
        driver.execute_script("window.scrollTo(0, 0)")
