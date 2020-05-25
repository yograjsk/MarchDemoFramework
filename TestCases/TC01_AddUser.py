import unittest

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
        cls.browser = cls.login.login("user", "password123")

    # def setDriver(self, driver):
    #     self.driver = driver

    def getDriver(self):
        return self.browser

    def test_addUser(self):
        cu = commonUtils()
        # userToAdd = userToAddDelete
        userToAdd = "user"+cu.getTodaysTimeStamp()
        self.browser.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/viewSystemUsers")
        self.browser.find_element(By.ID, "btnAdd").click()
        self.browser.find_element(By.XPATH, "//h1[@id='UserHeading' and text()='Add User']").is_displayed()
        dd_UserRole = Select(self.browser.find_element(By.ID, "systemUser_userType"))
        dd_UserRole.select_by_visible_text("Admin")
        self.browser.find_element(By.ID, "systemUser_employeeName_empName").send_keys("testAdminAuto1 m last")
        self.browser.find_element(By.ID, "systemUser_userName").send_keys(userToAdd)
        # self.driver.find_element(By.ID, "systemUser_password").send_keys("password123")
        # self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("password123"+Keys.ENTER)
        cu.click(By.ID, "btnSave", self.browser)
        # self.action.click(self.driver.find_element(By.ID, "btnSave")).perform()
        # cu.clickByActions(By.ID, "btnSave", self.driver)
        # self.driver.find_element(By.ID, "btnSave").click()
        recordAdded = self.browser.find_element(By.XPATH, "//table[@id='resultTable']//a[text()='" + userToAdd + "']/../..//input").is_displayed()
        print("Is user Added?: " + str(recordAdded))
        self.browser.save_screenshot("NewUserCreated.png")

    @classmethod
    def tearDownClass(self):
        logout = Logout()
        logout.logout(self.getDriver())

if __name__ == '__main__':
    unittest.main()

