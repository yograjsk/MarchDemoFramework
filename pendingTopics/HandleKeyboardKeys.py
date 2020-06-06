from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class workingWithKeys():

    def handleKeyboardKeys(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        # set implicit time to 30 seconds
        self.driver.get("http://localhost:81/orangehrm/symfony/web/index.php/auth/login")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, "txtUsername").send_keys("user")
        # self.driver.find_element(By.NAME, "txtPassword").send_keys("password123" + Keys.ENTER)
        # self.driver.find_element(By.NAME, "Submit")
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('n').key_up(Keys.CONTROL).perform()



k = workingWithKeys()
k.handleKeyboardKeys()
