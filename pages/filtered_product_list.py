from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from lib import conf_reader


class FilteredProductList:

    def __init__(self, obj):
        global driver
        driver = obj

    def click_product(self):
        item = driver.find_element_by_xpath(conf_reader.fetch_filtered_products_elements_locators('FilteredProducts', 'select_product_xpath'))
        item.click()

    def validate_filter_category(self, category):
        try:
            categoryFilter = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, conf_reader.fetch_filtered_products_elements_locators('FilteredProducts', 'filter_category_xpath'))))
            assert category.lower() in categoryFilter.text.lower()
        except TimeoutException:
            print("Loading took too much time!")

    def validate_filter_count(self, count):
        try:
            filterCount = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, conf_reader.fetch_filtered_products_elements_locators('FilteredProducts', 'filter_count_xpath'))))
            assert filterCount.text == 'Filter ( ' + count + ' )'
        except TimeoutException:
            print("Loading took too much time!")

    def validate_filter_size(self, size):
        try:
            sizeFilter = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, conf_reader.fetch_filtered_products_elements_locators('FilteredProducts', 'filter_size_xpath'))))
            assert sizeFilter.text == size
        except TimeoutException:
            print("Loading took too much time!")

    def validate_filter_size_another_way(self, size):
        try:
            sizeFilterTwo = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@data-qa-size-button-' + str(size).replace(".", "") + '="true"]')))
            value = sizeFilterTwo.get_attribute('aria-checked')
            assert value == "true"
        except TimeoutException:
            print("Loading took too much time!")