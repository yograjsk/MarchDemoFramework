import unittest

import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC01_AddUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cu = commonUtils()
        # self.driver = self.__cu.getBrowser()
        # cls.driver = cu.getBrowser()
        cls.login = Login()
        cls.driver = cls.login.login("user", "password123")

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def test_addUser(self):
        try:
            cu = commonUtils()
            # userToAdd = userToAddDelete
            userToAdd = "user"+cu.getTodaysTimeStamp()  #user054020
            self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/viewSystemUsers")
            self.driver.find_element(By.ID, "btnAdd").click()
            self.driver.find_element(By.XPATH, "//h1[@id='UserHeading' and text()='Add User']").is_displayed()
            dd_UserRole = Select(self.driver.find_element(By.ID, "systemUser_userType"))
            dd_UserRole.select_by_visible_text("Admin")
            self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("testAdminAuto1 m last")
            self.driver.find_element(By.ID, "systemUser_userName").send_keys(userToAdd)
            # self.driver.find_element(By.ID, "systemUser_password").send_keys("password123")
            # self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("password123"+Keys.ENTER)
            cu.click(By.ID, "btnSave", self.driver)
            # self.action.click(self.driver.find_element(By.ID, "btnSave")).perform()
            # cu.clickByActions(By.ID, "btnSave", self.driver)
            # self.driver.find_element(By.ID, "btnSave").click()
            recordAdded = self.driver.find_element(By.XPATH, "//table[@id='resultTable']//a[text()='" + userToAdd + "']/../..//input").is_displayed()
            print("Is user Added?: " + str(recordAdded))
            self.driver.save_screenshot("NewUserCreated.png")
        except:
            self.setDriver(self.driver)

    @classmethod
    def tearDownClass(cls):
        lo = Logout()
        driver = cls.getDriver(cls)
        cls.assertTrue(lo.logout(driver), "The user is not able to Logout successfully")

if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/AddUserReport.html"))

