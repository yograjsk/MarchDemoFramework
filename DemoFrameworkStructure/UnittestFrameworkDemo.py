import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class UnitTestFrameworkDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("SetupClass Method - Executed only once for this class Before the first test method is executed")
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")

    def setUp(self):
        print("\nSetup Method - Executed before every test method")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()

    # URL to add user: https://opensource-demo.orangehrmlive.com/index.php/admin/view

    def test_scenario1(self): #add user
        print("First test Scenario")
        print(self.driver.title)

    def test_scenario2(self): #edit user
        print("Second test Scenario")
        print(self.driver.title)

    def test_scenario3(self): #Delete user
        print("Third test Scenario")
        print(self.driver.title)

    def test_scenario4(self):
        print("Fourth test Scenario")
        print(self.driver.title)

    def tearDown(self):
        print("TearDown Method - Executed after every test method")
        # self.driver.find_element_by_id("welcome").click()
        self.driver.find_element(By.ID, "welcome").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()
        if(self.driver.find_element_by_name("txtUsername").is_displayed()):
            print("User LOGGED OUT Successfully")
            return True
        else:
            print("User Could NOT LOGOUT of the application")
            return False

    @classmethod
    def tearDownClass(cls):
        print("TearDownClass Method - Executed only once for this class After the last test method is executed")


if __name__ == '__main__':
    unittest.main()
