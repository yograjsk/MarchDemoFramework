import time
import unittest
from datetime import date

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        cls.ssPath = configProperties["ssPath"]
        cls.ssExt = configProperties["ssExt"]

    def setUp(self):
        cu = commonUtils()
        print("\nSetup Method - Executed before every test method")
        # self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.get("http://localhost:81/")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        self.driver.find_element_by_name("txtUsername").send_keys("user")  #user
        self.driver.find_element_by_name("txtPassword").send_keys("password123")   #password123
        self.driver.find_element_by_name("Submit").click()
        # Using assert statements to check if user is logged in successfully or not
        self.assertTrue(self.driver.find_element(By.ID, "welcome").is_displayed(), "The user is not able to login successfully")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/recruitment/addCandidate")

        self.driver.find_element(By.ID, "addCandidate_appliedDate").click()
        self.selectDate("1 Jan 2022", self.driver)

        # Normal way if date field is allwoing you to send keys, the take can be set with below line of code
        # self.driver.find_element(By.ID, "addCandidate_appliedDate").clear()
        # self.driver.find_element(By.ID, "addCandidate_appliedDate").send_keys("2021-10-20")

        # The converntional way to checking if login happened
        # loggedIn = self.driver.find_element(By.ID, "welcome").is_displayed()
        # if loggedIn:
        #     cu.takeScreenshot(self.driver, self.ssPath+"UserLoggedInSuccessfully")
        #     # self.driver.save_screenshot("UserLoggedInSuccessfully.png")
        # else:
        #     # self.driver.save_screenshot("UserFailedToLogIn.png")
        #     cu.takeScreenshot(self.driver, self.ssPath+"UserFailedToLogIn")

    def test_sample(self):
        print("sample test method")

    # Ignore below method
    # def getTodaysTimeStamp(self):
    #     return date.today().strftime('%Y%m%d')

    def selectDate(self, dateValue, driver):
        cu = commonUtils()
        self.driver.find_element(By.ID, "ui-datepicker-div").is_displayed()
        dateSplitted = dateValue.split()
        print(dateSplitted)
        day = dateSplitted[0]
        month = dateSplitted[1]
        year = dateSplitted[2]
        cu.selectDropdownValue(By.CLASS_NAME, "ui-datepicker-month", month, self.driver)
        cu.selectDropdownValue(By.CLASS_NAME, "ui-datepicker-year", year, self.driver)
        # self.driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']//a[text()='"+day+"']").click()
        self.driver.find_element(By.LINK_TEXT, day).click()

    def scenario1(self): #add user
        cu = commonUtils()
        # userToAdd = userToAddDelete
        userToAdd = self.UserToAddDelete
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
        self.driver.save_screenshot("NewUserCreated.png")

    def atest_case1_Upload(self): #upload file
        cu = commonUtils()
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.ID, "pimCsvImport_csvFile").\
            send_keys("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\InputData\\importData(2).csv")
        cu.takeScreenshot("fileUpload")
        # print("Second test Scenario")
        # print(self.driver.title)

    def atest_case2_Download(self): #upload file
        cu = commonUtils()
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/admin/pimCsvImport")
        self.driver.find_element(By.LINK_TEXT, "Download").click()
        cu.takeScreenshot("fileDownload")

        # print("Second test Scenario")
        # print(self.driver.title)

    def scenario3(self): #Delete user
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
        self.driver.save_screenshot("NewUserCreated.png")

    # def test_scenario4(self):
    #     print("Fourth test Scenario")
    #     print(self.driver.title)

    def tearDown(self):
        print("TearDown Method - Executed after every test method")
        # self.driver.find_element(By.ID, "welcome").click()

        # Explicit wait
        # wait = WebDriverWait(self.driver, 10)
        # logout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        # logout.click()

        #Fluent wait
        # wait = WebDriverWait(self.driver, 10, poll_frequency=1,
        #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        # logout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        # logout.click()

        # self.driver.find_element_by_link_text("Logout").click()
        # if(self.driver.find_element_by_name("txtUsername").is_displayed()):
        #     print("User LOGGED OUT Successfully")
        #     self.driver.save_screenshot("UserLoggedOutSuccessfully.png")
        #     return True
        # else:
        #     print("User Could NOT LOGOUT of the application")
        #     self.driver.save_screenshot("UserCouldNotLogOut.png")
        #     return False

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Method - Executed only once for this class After the last test method is executed")


if __name__ == '__main__':
    unittest.main()



'''
waits:
implicite wait - wait for certain time untill some condition is satisfied - NOT A HARD WAIT (30 sec time)
explicite wait - 
fluent wait - flexibility, different parameters, can override different exceptions, poling time, poling frequency

Explicite wait example code:
=========
wait = WebDriverWait(self.driver, 10)
welcome = wait.until(EC.element_to_be_clickable((By.ID,"welcome")))
welcome.click()

Fluent wait
============
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Firefox()
# Load some webpage
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
'''