import configparser


def read_config_data(section, key):
    config = configparser.ConfigParser()
    config.read('./config.cfg')
    return config.get(section, key)


def fetch_home_page_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/home_page.cfg')
    return config.get(section, key)


def fetch_mens_footwear_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/mens_footwear.cfg')
    return config.get(section, key)


def fetch_filtered_products_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/filtered_product_list.cfg')
    return config.get(section, key)
