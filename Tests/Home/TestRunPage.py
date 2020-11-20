import pytest
from Pages.Home.SearchPage import TestHome
from Pages.ServiceList.service_selection import ServiceSelection
import time
from ddt import ddt, data, unpack
import unittest
from Utilities.read_data import HomeData
from Base.SeleniumMethods import SeleniumDriver
from Pages.PaymentDetailsPage.PaymentGatewayBooking import PaymentGateway


@pytest.mark.usefixtures("web_driver")
@ddt
class TestHomePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, web_driver):
        self.home = TestHome(self.driver)
        self.service = ServiceSelection(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.pgw = PaymentGateway(self.driver)

    @data(*HomeData("Data.csv"))
    @unpack
    def test_home(self, FromCity, ToCity, BookingDay, BusTypeFilter, ServiceNumber, Seats, Gender, Age, Concession,PGW):
        self.home.homePageSearch(FromCity, ToCity, BookingDay)
        self.service.serviceList(BusTypeFilter, ServiceNumber, Seats, Gender, Age, Concession)
        self.pgw.paymentForBooking(PGW)
        time.sleep(1)
        self.sd.scrollToView("/html/body/div[3]/div/a[1]")
        self.sd.clickElement("/html/body/div[3]/div/a[1]")