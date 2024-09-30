from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def add(a: int, b: int) -> int:
    return a + b


print(add(3.4, 8))


def find_element_by_id(driver: WebDriver, id: str) -> WebElement:
    return driver.find_element(by=By.ID, value=id)
