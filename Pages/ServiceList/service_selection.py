import string
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base.SeleniumMethods import SeleniumDriver


class ServiceSelection(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        global onward_seat_count

        # Bus Type Filter #

    _bus_type_filter = "//div[@class='filters']//span[@id='BtFid']"
    _bus_type_non_ac = "//*[@id='Bustypes201']"
    _bus_type_ac = "//*[@id='Bustypes200']"
    _close_bus_type_filter = "//div[@class='filters']//span[@class='selectArrow']"

    # Service List #
    _onward_result_list_grid = "//div[@id='ForwardResults']"
    _onward_services = "//div[@class='rSetForward']"

    # Boarding Point #
    _boarding_point = "//select[@id='ForwardBoardId']"
    _boarding_point_list = "//select[@id='ForwardBoardId']/option"

    # Dropping Point #
    _dropping_point = "//select[@id='ForwardDroppingId']"
    _dropping_point_list = "//select[@id='ForwardDroppingId']/option"

    # Show Layout #
    _show_layout_button = "//input[@id='fwLtBtn']"

    # Seat layout #
    _seat_layout = "//div[@class='seats']//ul"
    _available_seats = "//li[@class='availSeatClassS']"

    # Passenger Details #
    _passenger_details_scroll = "//td[@align='left']//tbody/tr[1]/td[@class='paxHeaderCS']"
    _mobile_number = "//input[@name='mobileNo']"
    _email_id = "//input[@name='email']"
    _passenger_details_block = "//table[@id='PaxTblForward']/tbody/tr"
    _gender_type = "//select[@id='genderCodeIdForward0']"
    _passenger_name = "//input[@id='passengerNameForward0']"
    _passenger_age = "//input[@id='passengerAgeForward0']"
    _concession_type = "//select[@id='concessionIdsForward0']"

    # Continue Button #
    _continue_button = "//*[@id='BookNowBtn']"

    def busTypeFilter(self, filterType):
        filterType = filterType.upper()
        try:
            self.waitForElement(self._bus_type_filter)
            self.clickElement(self._bus_type_filter)
            if filterType == "NON-AC":
                self.clickElement(self._bus_type_non_ac)
                self.clickElement(self._close_bus_type_filter)
            elif filterType == "AC":
                self.clickElement(self._bus_type_ac)
                self.clickElement(self._close_bus_type_filter)
            else:
                print("Bus Type filter not found")
        except Exception as e:
            print(e)

    def selectService(self, serviceNumber, seats):
        service_list_grid = self.getElement("//div[@id='ForwardResults']")
        available_services = service_list_grid.find_elements(By.XPATH, "//div[@class='rSetForward']")
        time.sleep(1)
        try:
            for i in range(1, len(available_services) + 1):
                service_numbers = self.getElement(
                    "//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[1]/div[1]").text
                if service_numbers == serviceNumber:
                    available_seats = self.getElement(
                        "//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[4]/span[1]").get_attribute(
                        "availcs")
                    if int(available_seats) >= int(seats):
                        self.clickElement("//div[@id='ForwardResults']/div[" + str(i) + "]/div[1]/div[5]/input[1]")
                        break
            else:
                print("Selected Service is not available")
        except Exception as e:
            print(e)

    def boardingPoint(self):
        self.waitForElement(self._boarding_point)
        boarding_point = self.getElement(self._boarding_point)
        boarding_point_list = boarding_point.find_elements(By.XPATH, self._boarding_point_list)
        try:
            for i in boarding_point_list:
                if i.text.strip() == "Select One":
                    boarding = Select(boarding_point)
                    boarding.select_by_index(1)
                    break
                else:
                    break
        except Exception as e:
            print(e)

    def droppingPoint(self):
        dropping_point = self.getElement(self._dropping_point)
        dropping_point_list = dropping_point.find_elements(By.XPATH, self._dropping_point_list)
        try:
            for i in dropping_point_list:
                if i.text.strip() == "Select One":
                    dropping = Select(dropping_point)
                    dropping.select_by_index(1)
                    break
                else:
                    break
        except Exception as e:
            print(e)

    def showLayout(self):
        self.clickElement(self._show_layout_button)

    def seatSelection(self, selectSeats):
        self.scrollToView(self._boarding_point)
        self.waitForElement(self._seat_layout)
        seatLayout = self.getElements(self._seat_layout)
        self.onward_seat_count = selectSeats
        time.sleep(1)
        try:
            count = 1
            for seat in seatLayout:
                if count <= int(self.onward_seat_count) <= 6:
                    i = seat.find_element(By.XPATH, self._available_seats)
                    i.click()
                    count += 1
                    if count > int(self.onward_seat_count) or count > 6:
                        break
            else:
                print("Please select less than 6 seats")
        except Exception as e:
            print(e)

    def passengerDetails(self, mobileNumber, email):
        self.waitForElement(self._passenger_details_scroll)
        self.scrollToView(self._passenger_details_scroll)
        self.clearData(self._mobile_number)
        self.sendKeys(mobileNumber, self._mobile_number)
        self.clearData(self._email_id)
        self.sendKeys(email, self._email_id)

    def passengerGender(self, genders):
        try:
            for i in range(0, int(self.onward_seat_count)):
                if i <= int(self.onward_seat_count):
                    gender = self.getElement("//select[@id='genderCodeIdForward" + str(i) + "']")
                    gen = Select(gender)
                    if genders.split(":")[i].upper() == "M":
                        gen.select_by_visible_text("MALE")
                    if genders.split(":")[i].upper() == "F":
                        gen.select_by_visible_text("FEMALE")
                    if i > int(self.onward_seat_count):
                        break
        except Exception as e:
            print(e)

    def passengerNames(self):
        try:
            for i in range(0, int(self.onward_seat_count)):
                if i <= int(self.onward_seat_count):
                    name = self.getElement(
                        "//input[@id='passengerNameForward" + str(i) + "']")
                    randNames = ''.join(random.choices(string.ascii_uppercase, k=6))
                    name.send_keys(randNames)
                if i > int(self.onward_seat_count):
                    break
        except Exception as e:
            print(e)

    def passengerAges(self, ages):
        try:
            for i in range(0, int(self.onward_seat_count)):
                if i <= int(self.onward_seat_count):
                    age = self.getElement("//input[@id='passengerAgeForward" + str(i) + "']")
                    age.send_keys(ages.split(":")[i])
                if i > int(self.onward_seat_count):
                    break
        except Exception as e:
            print(e)

    def concessionTypes(self, concessionType):
        try:
            for i in range(0, int(self.onward_seat_count)):
                if i < int(self.onward_seat_count):
                    concession = self.getElement(
                        "//tr[@id='Forward" + str(i) + "tr']//select[@id='concessionIdsForward" + str(
                            i) + "']")
                    con = Select(concession)
                    if concessionType.split(":")[i].upper() == "GENERAL":
                        con.select_by_visible_text("GENERAL PUBLIC")
                    if concessionType.split(":")[i].upper() == "SENIOR":
                        con.select_by_visible_text("SENIOR CITIZEN")
                        conType = self.getElement("//input[@id='cardNumberForward" + str(i) + "']")
                        conType.send_keys(''.join(random.choices(string.digits.replace('0', '1'), k=4)))
                    if concessionType.split(":")[i].upper() == "JOURN":
                        con.select_by_visible_text("JOURN 2/3 CONC")
                        conType = self.getElement("//input[@id='cardNumberForward" + str(i) + "']")
                        conType.send_keys(''.join(random.choices(string.digits.replace('0', '1'), k=4)))
                    if i > int(self.onward_seat_count):
                        break
        except Exception as e:
            print(e)

    def clickContinue(self):
        self.clickElement(self._continue_button)

    def serviceList(self, filterType, serviceNumber, seats, gender, age, concession):
        self.busTypeFilter(filterType)
        self.selectService(serviceNumber, seats)
        self.boardingPoint()
        self.droppingPoint()
        self.showLayout()
        self.seatSelection(seats)
        self.passengerDetails("9999999999", "try@except.com")
        self.passengerGender(gender)
        self.passengerNames()
        self.passengerAges(age)
        self.concessionTypes(concession)
        # self.clickContinue()
        time.sleep(2)
