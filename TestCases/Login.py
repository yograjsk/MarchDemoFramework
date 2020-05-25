from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from commonUtils.commonUtilities import commonUtils
from ObjectRepository.ObjectRepository import ObjectRepo


class Login(ObjectRepo):

    def login(self, username, password):
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
        cu.sendkeys(By.NAME, OR.username_txt_name, username, self.driver)
        cu.sendkeys(By.NAME, OR.password_txt_name, password, self.driver)
        cu.click(By.NAME, OR.login_btn_name, self.driver)

        # self.assertTrue(self.driver.find_element(By.ID, OR.welcome_lbl_id).is_displayed(), "The user is not able to login successfully")
        return self.driver





