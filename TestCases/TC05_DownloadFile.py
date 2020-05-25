import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC05_DownloadFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtils()
        # self.driver = self.__cu.getBrowser()
        # cls.driver = cu.getBrowser()
        cls.login = Login()
        cls.driver = cls.login.login("user", "password123")

    def getDriver(self):
        return self.driver

    def test_DownloadFile(self):
        cu = commonUtils()
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.LINK_TEXT, "Download").click()
        # cu.takeScreenshot("fileDownload")

    @classmethod
    def tearDownClass(self):
        logout = Logout()
        logout.logout(self.getDriver())

if __name__ == '__main__':
    unittest.main()

