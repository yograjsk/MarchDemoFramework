import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from TestCases.Login import Login
from TestCases.Logout import Logout
from commonUtils.commonUtilities import commonUtils

class TC02_DeleteUser(unittest.TestCase):

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

    def test_DeleteUser(self):
        cu = commonUtils()
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/viewSystemUsers")
        # userToDelete = userToA7ddDelete
        userToDelete = self.UserToAddDelete
        self.driver.find_element(By.ID, "resultTable").is_displayed()
        self.driver.find_element(By.XPATH, "//table[@id='resultTable']//a[text()='"+userToDelete+"']/../..//input").click()
        self.action.click(self.driver.find_element(By.ID, "btnDelete")).perform()
        # cu.clickByActions(By.ID, "btnDelete", self.driver)
        # self.driver.find_element(By.ID, "btnDelete").click()
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()
        recordDeleted = not(self.driver.find_element
                            (By.XPATH, "//table[@id='resultTable']//a[text()='"+userToDelete+"']/../..//input").is_displayed())
        print("Is user deleted: " + str(recordDeleted))
        # print("Third test Scenario")
        # print(self.driver.title)
        self.driver.save_screenshot("NewUserDeleted.png")

    @classmethod
    def tearDownClass(self):
        logout = Logout()
        logout.logout(self.getDriver())

if __name__ == '__main__':
    unittest.main()

