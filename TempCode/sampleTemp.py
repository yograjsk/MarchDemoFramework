from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from commonUtils.commonUtilities import commonUtils
from ObjectRepository.ObjectRepository import ObjectRepo


class sample(ObjectRepo):

    def sample(self):
        cu = commonUtils()
        OR = ObjectRepo
        configProperties = cu.readProperties("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\commonUtils\\config.properties")
        self.UserToAddDelete = configProperties["user"]
        self.driver = cu.getBrowser(configProperties["browser"])
        self.driver.implicitly_wait(configProperties["wait"])
        self.action = ActionChains(self.driver)
        self.ssPath = configProperties["ssPath"]
        self.ssExt = configProperties["ssExt"]
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        # # find all the links on the page
        allLinkelements = self.driver.find_elements_by_tag_name("a")
        print(type(allLinkelements), "number of links: ", len(allLinkelements))
        for i in allLinkelements:
            print(i.text)
        # # find all the input tags on the page
        allInputElements = self.driver.find_elements_by_tag_name("input")
        print(type(allInputElements), "number of input elements: ", len(allInputElements))
        for i in allInputElements:
            print(i.text)
        #

        # cu.sendkeys(By.NAME, OR.username_txt_name, username, self.driver)
        # cu.sendkeys(By.NAME, OR.password_txt_name, password, self.driver)
        # cu.click(By.NAME, OR.login_btn_name, self.driver)

        # self.assertTrue(self.driver.find_element(By.ID, OR.welcome_lbl_id).is_displayed(), "The user is not able to login successfully")
        return self.driver

sam = sample()
sam.sample()



