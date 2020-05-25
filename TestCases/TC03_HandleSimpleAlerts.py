import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC03_HandleSimpleAlerts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtils()
        cls.driver = cls.cu.getBrowser("Chrome")
        # self.driver = self.__cu.getBrowser()
        # cls.driver = cu.getBrowser()
        # cls.login = Login()
        # cls.browser = cls.login.login("user", "password123")

    # def setDriver(self, driver):
    #     self.driver = driver

    def getDriver(self):
        return self.driver

    def test_HandleASimpleAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.accept()
        print("Alert box Accepted")

    @classmethod
    def tearDownClass(self):
        logout = Logout()
        logout.logout(self.getDriver())

if __name__ == '__main__':
    unittest.main()

