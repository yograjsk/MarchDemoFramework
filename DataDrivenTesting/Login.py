from selenium.common.exceptions import NoSuchElementException

import DataDrivenTesting.DDUtils as ddu
from selenium import webdriver
from selenium.webdriver.common.by import By

class checkLogin():

    def DDloginCheck(self):
        # excelFile = "C:\Users\USER\PycharmProjects\MarchDemoFramework\DataDrivenTesting\testData\loginData.xlsx"
        excelFile = "testData/loginData.xlsx"
        sheetName = "Sheet1"
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        rows = ddu.getRowCount(excelFile, sheetName)
        cols = ddu.getColumnCount(excelFile, sheetName)
        for r in range(2, rows+1):
            username = ddu.readExcel(excelFile, sheetName, r, 1)
            password = ddu.readExcel(excelFile, sheetName, r, 2)
            self.driver.find_element(By.NAME, "txtUsername").send_keys(username)
            self.driver.find_element(By.NAME, "txtPassword").send_keys(password)
            self.driver.find_element(By.NAME, "Submit").click()
            if (self.checkElementPresent(self.driver, By.ID, "welcome")):
                message = "Test Passed - Login Successful"
            else:
                message = "Test Failed - Login Unsuccessful"
            ddu.writeExcel(excelFile, sheetName, r, 3, message)

    def checkElementPresent(self, driver, ByType, ByValue):
        try:
            check = driver.find_element(ByType, ByValue).is_displayed()
        # return check
        except NoSuchElementException:
            check = False
        finally:
            return check

cl = checkLogin()
cl.DDloginCheck()






