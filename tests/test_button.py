from selenium.webdriver.common.by import By

from configuration import TEST_URL, TEST_URL_2, TEST_URL_3


def test_is_button_exists_simple(browser):
    browser.get(TEST_URL)
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_is_button_exists_like_a_button(browser):
    browser.get(TEST_URL_2)
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_is_button_disabled(browser):
    browser.get(TEST_URL_3)
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
