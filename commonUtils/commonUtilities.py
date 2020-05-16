from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class commonUtils():

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

