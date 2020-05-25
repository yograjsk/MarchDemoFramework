from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from commonUtils.commonUtilities import commonUtils
from ObjectRepository.ObjectRepository import ObjectRepo
from selenium.webdriver.support import expected_conditions as EC


class Logout():

    def logout(self, driver):
        OR = ObjectRepo()
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        logout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout.click()
        self.assertTrue(self.driver.find_element(OR.username_txt).is_displayed(), "The user is not able to login successfully")



