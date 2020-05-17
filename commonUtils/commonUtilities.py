# from DemoFrameworkStructure.UnittestFrameworkDemo import UnitTestFrameworkDemo
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class commonUtils():

    # def __init__(self):
    #     self.__sspath =

    def setSSPath(self, newssPath):
        self.__sspath = newssPath

    def getSSPath(self):
        return self.__sspath



    def selectDropdownValue(self, ByType, ByValue, DropdownTextToSelect, driver):
        dd_UserRole = Select(driver.find_element(ByType, ByValue))
        dd_UserRole.select_by_visible_text(DropdownTextToSelect)

    def clickByActions(self, ByType, ByValue, driver):
        action = ActionChains(driver)
        action.click(ByType, ByValue).perform()

    def mouseOverAndClickByActions(self, ByType, ByValue, driver):
        action = ActionChains(driver)
        action.move_to_element(ByType, ByValue).click().perform()

    def readProperties(self, propertyFilePath):
        properties = {}

        with open(propertyFilePath, 'r') as fileContentsByLines:
            for line in fileContentsByLines:
                lineText = line.rstrip()
                if ("=" not in lineText or lineText.startswith("#")): continue
                k, v = lineText.split("=",1)
                properties[k] = v
        print(properties)
        return properties

    def getBrowser(self, browserName):
        if browserName in ("Chrome", "chrome"):
            self.browser = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
        elif browserName in ("Firefox", "FF", "firefox", "ff"):
            self.browser = webdriver.Firefox(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\geckodriver.exe")
        return self.browser

    def takeScreenshot(self, driver, fileName):
        # driver.save_screenshot(self.__sspath+fileName+".png")
        driver.save_screenshot(commonUtils.getSSPath()+fileName+".png")

    def fluentWaitForElement(self, driver, ByType, ByValue, time=10):
        wait = WebDriverWait(driver, time, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        return wait.until(EC.element_to_be_clickable((ByType, ByValue)))

    def waitExplicitely(self, driver, ByType, ByValue, time=10):
        wait = WebDriverWait(driver, time)
        return wait.until(EC.element_to_be_clickable((ByType, ByValue)))
