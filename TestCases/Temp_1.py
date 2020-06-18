from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from commonUtils.commonUtilities import commonUtils
from ObjectRepository.ObjectRepository import ObjectRepo


class Temp(ObjectRepo):

    def temp(self):
        cu = commonUtils()
        OR = ObjectRepo
        configProperties = cu.readProperties("commonUtils\\config.properties")
        self.UserToAddDelete = configProperties["user"]
        self.driver = cu.getBrowser(configProperties["browser"])
        self.driver.implicitly_wait(configProperties["wait"])
        self.action = ActionChains(self.driver)
        self.ssPath = configProperties["ssPath"]
        self.ssExt = configProperties["ssExt"]
        self.driver.get("http://localhost:8080/")
        print("Number of Jobs running on Jenkins")
        jobsRows = self.driver.find_elements_by_xpath("//tr[contains(@id,'job')]")
        for i in jobsRows:
            tableCells = i.find_elements_by_tag_name("td")
            for j in tableCells:
                print(j.text)

        self.driver.find_elements_by_xpath("//")

t = Temp()
t.temp()


