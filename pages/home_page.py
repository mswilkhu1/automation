from selenium.webdriver import ActionChains

from lib import conf_reader


class HomePage:

    def __init__(self, obj):
        global driver
        driver = obj

    def click_mens_footwear(self):
        hover_mens_button = driver.find_element_by_id(
            conf_reader.fetch_home_page_elements_locators('HomePage', 'mens_button_id'))
        hover = ActionChains(driver).move_to_element(hover_mens_button)
        hover.perform()

        click_footwear_button = driver.find_element_by_xpath(
            conf_reader.fetch_home_page_elements_locators('HomePage', 'footwear_button_xpath'))
        driver.execute_script("arguments[0].click();", click_footwear_button)
