from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from Base.SeleniumMethods import SeleniumDriver
import datetime
from datetime import datetime, timedelta


class TestHome(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # From Place #
    _from_place = "//*[@id='fromPlaceName']"
    _list_of_from_places = "//ul[@id='ui-id-1']//li//a"

    # To Place #
    _to_place = "//*[@id='toPlaceName']"
    _list_of_to_places = "//ul[@id='ui-id-2']//li//a"

    # Onward Calendar #
    _click_on_calendar = '//*[@id="txtJourneyDate"]'
    _current_month_name = "//div[@class='ui-datepicker-group ui-datepicker-group-first']/div[1]/div[1]/span[1]"
    _next_month_name = "//div[@class='ui-datepicker-group ui-datepicker-group-last']/div[1]/div[1]/span[1]"
    _current_month_calendar = "//div[@class='ui-datepicker-group ui-datepicker-group-first']//table//tbody"
    _next_month_calendar = "//div[@class='ui-datepicker-group ui-datepicker-group-last']//table//tbody"

    # Submit Button #
    _submit_button = '//*[@id="searchBtn"]'

    def fromPlace(self, fromCity):
        fromCity = fromCity.upper()
        self.waitForElement(self._from_place)
        self.clearData(self._from_place)
        self.sendKeys(fromCity, self._from_place)
        from_list = self.getElements(self._list_of_from_places)
        try:
            for city in from_list:
                if city.text == fromCity:
                    city.click()
                    break
            else:
                print("From city not found")
        except Exception as e:
            print(e)

    def toPlace(self, toCity):
        toCity = toCity.upper()
        self.waitForElement(self._to_place)
        self.clearData(self._to_place)
        self.sendKeys(toCity, self._to_place)
        to_list = self.getElements(self._list_of_to_places)
        try:
            for city in to_list:
                if city.text == toCity:
                    city.click()
                    break
            else:
                print("To city not found")
        except Exception as e:
            print(e)

    def date(self, journeyDate):
        currentDay = datetime.now() + timedelta(days=float(journeyDate))
        day = str(currentDay.day)
        month = currentDay.strftime("%B")
        self.waitForElement(self._click_on_calendar)
        click_on_calendar = self.clickElement(self._click_on_calendar)
        onward_calendar = self.getElement(self._current_month_calendar)
        dates = onward_calendar.find_elements(By.TAG_NAME, "a")
        monthname = self.getElement(self._current_month_name).text
        monthname1 = self.getElement(self._next_month_name).text
        try:
            if monthname == month:
                for i in dates:
                    if i.text == day:
                        i.click()
                        break
                    else:
                        if len(dates) == len(str(i)):
                            print("Given date is not present in the current month")
                            break
            elif monthname1 == month:
                self.waitForElement(self._next_month_calendar)
                return_calendar = self.getElement(self._next_month_calendar)
                date = return_calendar.find_elements(By.TAG_NAME, "a")
                for j in date:
                    if j.text == day:
                        j.click()
                        break
                    else:
                        if len(date) == (len(str(j))):
                            print("Given date is not present in the next month")
                            break
            else:
                print("Given month is not available for Booking")

        except StaleElementReferenceException:
            pass

    def submitButton(self):
        self.clickElement(self._submit_button)

    def homePageSearch(self, fromCity, toCity, advanceBookingDays):
        self.fromPlace(fromCity)
        self.toPlace(toCity)
        self.date(advanceBookingDays)
        self.submitButton()