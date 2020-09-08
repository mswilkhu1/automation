import pytest
from pytest_bdd import scenario, given, when, then
from base import initiate_driver
from pages import home_page
from pages import mens_footwear
from pages import filtered_product_list


@pytest.fixture()
def browser():
    global driver
    driver = initiate_driver.start_browser()

    yield driver
    initiate_driver.close_browser()


@scenario("../features/filterProducts.feature", 'Apply filters on mens footwear section')
def test_apply_filters_on_mens_footwear_section(browser):
    """Apply filters on mens footwear section"""


@given('user is on mens footwear section')
def user_is_on_mens_footwear_section():
    home = home_page.HomePage(driver)
    home.click_mens_footwear()


@when('user selects filters category <category>')
def user_selects_filters_category(category):
    footwear = mens_footwear.MensFootwear(driver)
    footwear.click_filter_button()
    footwear.filter_category(category)


@when('size of the footwear <size>')
def size_of_the_footwear(size):
    footwear = mens_footwear.MensFootwear(driver)
    footwear.select_size_filter(size)


@when('clicks on the apply filter button')
def clicks_on_the_apply_filter_button():
    footwear = mens_footwear.MensFootwear(driver)
    footwear.click_apply_filter()


@then('filter should be applied with correct count <count>')
def filter_should_be_applied_with_correct_count(count):
    filterCount = filtered_product_list.FilteredProductList(driver)
    filterCount.validate_filter_count(count)


@then('validate the filter within product selected <category> <size>')
def validate_filter_applied(category, size):
    filterValidation = filtered_product_list.FilteredProductList(driver)
    filterValidation.click_product()
    filterValidation.validate_filter_size(size)
    filterValidation.validate_filter_category(category)
    filterValidation.validate_filter_size_another_way(size)
