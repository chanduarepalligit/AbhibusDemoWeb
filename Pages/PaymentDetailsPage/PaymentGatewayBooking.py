from Base.SeleniumMethods import SeleniumDriver


class PaymentGateway(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Payment Gateway Methods #
    _ebs_payment_gateway = "//div[@id='pggwid']//div[@id='ebs']"
    _phonePe_payment_gateway = "//div[@id='pggwid']//div[@id='PhenePe']"
    _amazon_payment_gateway = "//div[@id='pggwid']//div[@id='amazonPay']"

    # Click on Make Payment #
    _click_on_make_payment = "/html/body/div[4]/div/form/table/tbody/tr[6]/td/div/input"

    def selectPaymentGateway(self, PaymentMethod):
        PaymentMethod = PaymentMethod.upper()
        if PaymentMethod == "EBS":
            self.waitForElement(self._ebs_payment_gateway)
            self.scrollToView(self._ebs_payment_gateway)
            self.clickElement(self._ebs_payment_gateway)
        if PaymentMethod == "PHONEPE":
            self.waitForElement(self._phonePe_payment_gateway)
            self.scrollToView(self._phonePe_payment_gateway)
            self.clickElement(self._phonePe_payment_gateway)
        if PaymentMethod == "AMAZONPAY":
            self.waitForElement(self._amazon_payment_gateway)
            self.scrollToView(self._amazon_payment_gateway)
            self.clickElement(self._amazon_payment_gateway)

    def clickMakePayment(self):
        self.clickElement(self._click_on_make_payment)

    def paymentForBooking(self, SelectPaymentGateway):
        self.selectPaymentGateway(SelectPaymentGateway)
        self.clickMakePayment()
