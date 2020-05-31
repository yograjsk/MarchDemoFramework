from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from commonUtils.commonUtilities import commonUtils
from ObjectRepository.ObjectRepository import ObjectRepo
from selenium.webdriver.support import expected_conditions as EC


class Logout():

    def logout(self, driver):
        OR = ObjectRepo()
        cu = commonUtils()
        cu.click(By.ID, "welcome", driver)
        cu.click(By.LINK_TEXT, "Logout", driver)
        check = cu.checkElementDisplayed(By.NAME, OR.username_txt_name, driver)
        driver.close()
        return check



