# from DemoFrameworkStructure.UnittestFrameworkDemo import UnitTestFrameworkDemo
import datetime

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ObjectRepository.ObjectRepository import ObjectRepo


class commonUtils():

    def __init__(self):
        self.OR = ObjectRepo()
    # def __init__(self):
    #     self.__sspath =

    def setSSPath(self, newssPath):
        self.__sspath = newssPath

    def getSSPath(self):
        return self.__sspath

    def getTodaysTimeStamp(self):
        now = datetime.datetime.now()
        return (str(now.hour)+str(now.minute)+str(now.second))

    def sendkeys(self, ByType, ByValue, valueToPass, driver):
        driver.find_element(ByType, ByValue).send_keys(valueToPass)

    def selectDropdownValue(self, ByType, ByValue, DropdownTextToSelect, driver):
        dd_UserRole = Select(driver.find_element(ByType, ByValue))
        dd_UserRole.select_by_visible_text(DropdownTextToSelect)

    def clickByActions(self, ByType, ByValue, driver):
        action = ActionChains(driver)
        action.click(ByType, ByValue).perform()

    def clickByAction(self, webObj, driver):
        action = ActionChains(driver)
        action.click(webObj).perform()

    def click(self, ByType, ByValue, driver):
        driver.find_element(ByType, ByValue).click()

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

        if browserName in ("Chrome", "chrome", "chromeheadless"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-infobar")
            chrome_options.add_argument("--window-size=1920,1080")
            # chrome_options.add_argument("--start-maximized")
            if browserName == "chromeheadless":
                chrome_options.add_argument("--headless")

            # capabilities = DesiredCapabilities.CHROME.copy()
            # capabilities['acceptSslCerts'] = True
            # capabilities['acceptInsecureCerts'] = True

            self.browser = webdriver.Chrome(chrome_options=chrome_options,
                    executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
            # self.browser = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
        elif browserName in ("Firefox", "FF", "firefox", "ff"):
            # self.browser = webdriver.Firefox(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\geckodriver.exe")
            fireFoxOptions = webdriver.FirefoxOptions()
            # fireFoxOptions.add_argument("--headless")

            brower = webdriver.Firefox(firefox_options=fireFoxOptions)

            brower.get('https://pythonbasics.org')
            print(brower.page_source)
        return self.browser


    def takeScreenshot(self, driver, fileName):
        # driver.save_screenshot(self.__sspath+fileName+".png")
        driver.save_screenshot(commonUtils.getSSPath() + fileName + ".png")

    def fluentWaitForElement(self, driver, ByType, ByValue, time=10):
        wait = WebDriverWait(driver, time, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        return wait.until(EC.element_to_be_clickable((ByType, ByValue)))

    def waitExplicitely(self, driver, ByType, ByValue, time=10):
        wait = WebDriverWait(driver, time)
        return wait.until(EC.element_to_be_clickable((ByType, ByValue)))

    def checkElementDisplayed(self, ByType, ByValue, driver):
        driver.find_element(ByType, ByValue).is_displayed()