from selenium.common.exceptions import NoSuchElementException


__author__ = 'xubin'


def is_element_present(driver, how, locator):
    try:
        driver.implicitly_wait(1)
        driver.find_element(by=how, value=locator)
        driver.implicitly_wait(30)
    except NoSuchElementException, e:
        return False
    return True


def is_element_visible(driver, how, locator):
    if driver.find_element(by=how, value=locator).is_displayed():
        return True
    else:
        return False


def is_element_not_visible(driver, how, locator):
    if not driver.find_element(by=how, value=locator).is_displayed():
        return True
    else:
        return False


def scroll_to(driver, how, locator):
    element = driver.find_element(by=how, value=locator)
    print "id:------" + element.id
    driver.execute_script("mobile: scrollTo", {"element": element.id})


def scroll_to_and_tap_on(driver, how, locator):
    element = driver.find_element(by=how, value=locator)
    print "id:------" + element.id
    driver.execute_script("mobile: scrollTo", {"element": element.id})
    element.click()