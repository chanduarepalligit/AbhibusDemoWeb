from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            print("Unable to identify locator tpe")

    def getElement(self, locator, locatorType="xpath", element=""):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except Exception as e:
            print(e)
        return element

    def getElements(self, locator, locatorType="xpath"):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
        except Exception as e:
            print(e)
        return element

    def clickElement(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except Exception as e:
            print(e)

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except Exception as e:
            print(e)

    def clearData(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
        except Exception as e:
            print(e)

    def waitForElement(self, locator, locatorType="xpath"):
        element = None
        try:
            byType = self.getByType(locatorType)
            wait = WebDriverWait(self.driver, 10, ignored_exceptions=
            [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException,
             ElementClickInterceptedException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
        except Exception as e:
            print(e)
        return element

    def scrollToView(self, locator, locatorType="xpath"):
        try:
            elm = self.getElement(locator, locatorType)
            element = self.driver.execute_script("arguments[0].scrollIntoView(true);", elm)
        except Exception as e:
            print(e)
