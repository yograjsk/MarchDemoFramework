import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from commonUtils.commonUtilities import commonUtils


class UnitTestFrameworkDemo(unittest.TestCase):

    # userToAddDelete = "Auto4"

    @classmethod
    def setUpClass(cls):
        print("SetupClass Method - Executed only once for this class Before the first test method is executed")
        # cls.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
        cu = commonUtils()
        configProperties = cu.readProperties("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\commonUtils\\config.properties")
        browserToLaunch = configProperties["browser"]
        impliciteWaitTime = configProperties["wait"]
        cls.UserToAddDelete = configProperties["user"]
        cls.driver = cu.getBrowser(browserToLaunch)
        cls.driver.implicitly_wait(impliciteWaitTime)
        cls.action = ActionChains(cls.driver)

    def setUp(self):
        print("\nSetup Method - Executed before every test method")
        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.get("http://localhost:81/")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        self.driver.find_element_by_name("txtUsername").send_keys("user")  #user
        self.driver.find_element_by_name("txtPassword").send_keys("password123")   #password123
        self.driver.find_element_by_name("Submit").click()

    # URL to add user: https://opensource-demo.orangehrmlive.com/index.php/admin/view

    def test_scenario1(self): #add user
        cu = commonUtils()
        # userToAdd = userToAddDelete
        userToAdd = self.UserToAddDelete
        # print("First test Scenario")
        # print(self.driver.title)
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/viewSystemUsers")
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.XPATH, "//h1[@id='UserHeading' and text()='Add User']").is_displayed()
        dd_UserRole = Select(self.driver.find_element(By.ID, "systemUser_userType"))
        dd_UserRole.select_by_visible_text("Admin")
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("testAdminAuto1 m last")
        self.driver.find_element(By.ID, "systemUser_userName").send_keys(userToAdd)
        self.driver.find_element(By.ID, "systemUser_password").send_keys("password123")
        self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("password123")
        self.action.click(self.driver.find_element(By.ID, "btnSave")).perform()
        # cu.clickByActions(By.ID, "btnSave", self.driver)
        # self.driver.find_element(By.ID, "btnSave").click()
        recordAdded = self.driver.find_element(By.XPATH, "//table[@id='resultTable']//a[text()='"+userToAdd+"']/../..//input").is_displayed()
        print("Is user Added?: " + str(recordAdded))

    # def test_scenario2(self): #edit user
    #     print("Second test Scenario")
    #     print(self.driver.title)
    #
    def test_scenario3(self): #Delete user
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

    #
    # def test_scenario4(self):
    #     print("Fourth test Scenario")
    #     print(self.driver.title)

    def tearDown(self):
        print("TearDown Method - Executed after every test method")
        # self.driver.find_element(By.ID, "welcome").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()
        # if(self.driver.find_element_by_name("txtUsername").is_displayed()):
        #     print("User LOGGED OUT Successfully")
        #     return True
        # else:
        #     print("User Could NOT LOGOUT of the application")
        #     return False

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Method - Executed only once for this class After the last test method is executed")


if __name__ == '__main__':
    unittest.main()
