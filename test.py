import os
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def browser():
    global driver
    URL = "http://stagingapsrtc.abhibus.com/oprs-web/"
    ChromeDriver = "C:\\Users\\Chandu\\Downloads\\chromedriver_win32\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = ChromeDriver
    driver = webdriver.Chrome(ChromeDriver)
    driver.maximize_window()
    driver.get(URL)
    time.sleep(2)


def fromPlace(fromCity):
    fromCity = fromCity.upper()
    driver.find_element(By.XPATH, "//*[@id='fromPlaceName']").click()
    driver.find_element(By.XPATH, "//*[@id='fromPlaceName']").send_keys(fromCity)
    time.sleep(1)
    from_city = driver.find_elements(By.XPATH, '//ul[@id="ui-id-1"]//li//a')
    try:
        for city in from_city:
            if city.text == fromCity:
                city.click()
                break
            else:
                print("From city not found")
    except Exception as e:
        print(e)


def toPlace(toCity):
    toCity = toCity.upper()
    driver.find_element(By.XPATH, "//*[@id='toPlaceName']").click()
    driver.find_element(By.XPATH, "//*[@id='toPlaceName']").send_keys(toCity)
    time.sleep(1)
    to_city = driver.find_elements(By.XPATH, "//ul[@id='ui-id-2']//li//a")
    try:
        for city in to_city:
            if city.text == toCity:
                city.click()
                break
    except Exception as e:
        print(e)


def date(days):
    currentDay = datetime.now() + timedelta(days=days)
    day = str(currentDay.day)
    click_on_calendar = driver.find_element(By.XPATH, '//*[@id="txtJourneyDate"]').click()
    full_calendar = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']")
    onward_calendar = full_calendar.find_element(By.XPATH,
                                                 "//div[@class='ui-datepicker-group ui-datepicker-group-first']//table//tbody")
    dates = onward_calendar.find_elements(By.TAG_NAME, "a")
    time.sleep(1)
    try:
        for i in dates:
            if days <= 30 and i.text == day:
                i.click()
                break
            elif days <= 30:
                return_calendar = full_calendar.find_element(By.XPATH,
                                                             "//div[@class='ui-datepicker-group ui-datepicker-group-last']//table//tbody")
                dates = return_calendar.find_elements(By.TAG_NAME, "a")
                time.sleep(1)
                for j in dates:
                    if days <= 30 and j.text == day:
                        j.click()
                        break

    except Exception as e:
        print(e)

    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()


def bus_type(filterType):
    wait = WebDriverWait(driver, 10)
    elm = wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='filters']//span[@id='BtFid']")))
    busType = driver.find_element_by_xpath("//div[@class='filters']//span[@id='BtFid']")
    busType.click()
    if filterType == "Non-AC":
        driver.find_element_by_xpath("//*[@id='Bustypes201']").click()
        driver.find_element_by_xpath("//div[@class='filters']//span[@class='selectArrow']").click()
    elif filterType == "AC":
        driver.find_element_by_xpath("//*[@id='Bustypes200']").click()
        driver.find_element_by_xpath("//div[@class='filters']//span[@class='selectArrow']").click()
    else:
        print("Bus Type filter not found")


def service_selection(serviceNumber, seats):
    time.sleep(5)
    service_list_grid = driver.find_element_by_xpath("//div[@id='ForwardResults']")
    available_services = service_list_grid.find_elements_by_xpath("//div[@class='rSetForward']")
    for i in range(1, len(available_services) + 1):
        service_numbers = driver.find_element_by_xpath(
            "//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[1]/div[1]").text
        if service_numbers == str(serviceNumber):
            available_seats = driver.find_element_by_xpath(
                "//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[4]/span[1]").get_attribute("availcs")
            if available_seats >= str(seats):
                driver.find_element_by_xpath(
                    "//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[5]/input[1]").click()
                break
    else:
        print("Service not found")


def boardingPoint():
    time.sleep(1)
    boarding_point = driver.find_element_by_xpath("//select[@id='ForwardBoardId']")
    board = driver.find_elements_by_xpath("//select[@id='ForwardBoardId']/option")
    for i in board:
        if i.text.strip() == "Select One":
            Select(boarding_point).select_by_index(1)
            break
        else:
            break


def droppingPoint():
    time.sleep(1)
    boarding_point = driver.find_element_by_xpath("//select[@id='ForwardDroppingId']")
    board = driver.find_elements_by_xpath("//select[@id='ForwardDroppingId']/option")
    for i in board:
        if i.text.strip() == "Select One":
            Select(boarding_point).select_by_index(1)
            break
        else:
            break

    driver.find_element_by_xpath("//input[@id='fwLtBtn']").click()


browser()
fromPlace("Vijayawada")
toPlace("Bangalore")
date(7)
bus_type("Non-AC")
service_selection(3704, 2)
boardingPoint()
droppingPoint()
