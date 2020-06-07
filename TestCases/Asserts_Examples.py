import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC01_AddUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtils()
        cls.login = Login()
        cls.driver = cls.login.login("user", "password123")

    def setUp(self):
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/dashboard")

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def test_checkDashboardPresent(self):
        self.assertTrue(self.driver.find_element(By.XPATH, "//h1[text()='Dashboard']").is_displayed(), "The Dashboard is not visible")
        return self.driver

    def test_quickLunchItems(self):
        quickLaunchItems = self.driver.find_elements_by_xpath("//table[@class='quickLaungeContainer']//td")
        self.assertEqual(len(quickLaunchItems), 6, "Quick launch item count expected: 6 but found:" + str(len(quickLaunchItems)))
        return self.driver

    def test_checkboxClick(self):
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/recruitment/addCandidate")


    @classmethod
    def tearDownClass(cls):
        lo = Logout()
        driver = cls.getDriver(cls)
        cls.assertTrue(lo.logout(driver), "The user is not able to Logout successfully")

if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/AddUserReport.html"))

