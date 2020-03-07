# Selenium test suite for Respa Admin UI https://github.com/City-of-Helsinki/respa/

import pytest
from selenium import webdriver


URL = 'https://respa.koe.hel.ninja/ra/'
USERNAME = 'xxx'
PASSWORD = 'xxx'


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


# Log in with Django account

@pytest.fixture()
def test_login(test_setup):

    driver.get(URL)

    driver.find_element_by_id('username').send_keys(USERNAME)
    driver.find_element_by_id('password').send_keys(PASSWORD).submit()


# Create new resource

def test_create_new_resource(test_setup, test_login):

    # Move to new resource page
    driver.find_element_by_link_text('Resources').click()
    driver.find_element_by_partial_link_text('Add a new resource').click()

    # Fill resource form
    driver.find_element_by_name('language-fi').click()
    driver.find_element_by_name('language-sv').click()
    driver.find_element_by_id('id_name_fi').send_keys('testresource')
    driver.find_element_by_id('id_name_en').send_keys('testresource')
