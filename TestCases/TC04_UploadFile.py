import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC04_UploadFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtils()
        # self.driver = self.__cu.getBrowser()
        # cls.driver = cu.getBrowser()
        cls.login = Login()
        cls.driver = cls.login.login("user", "password123")

    # def setDriver(self, driver):
    #     self.driver = driver

    def getDriver(self):
        return self.driver



    def test_UploadFile(self):
        cu = commonUtils()
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.ID, "pimCsvImport_csvFile").\
            send_keys("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\InputData\\importData(2).csv")
        # cu.takeScreenshot("fileUpload")


    @classmethod
    def tearDownClass(self):
        logout = Logout()
        logout.logout(self.getDriver())

if __name__ == '__main__':
    unittest.main()
