import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class handleAlerts:

    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\chromedriver.exe")
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\USER\\PycharmProjects\\March2020\\drivers\\geckodriver.exe")
        self.url = "https://www.seleniumeasy.com/test/javascript-alert-box-demo.html"

    def handlingSimpleAlert(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.accept()
        print("Alert box Accepted")

    def handlingConfirmationAlert(self):
        self.driver.get(self.url)
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.accept()
        print(self.driver.find_element(By.ID, "confirm-demo").text)
        print("Alert box Accepted - Clicked OK")

        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.btn-lg").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.dismiss()
        print(self.driver.find_element(By.ID, "confirm-demo").text)
        print("Alert box Dismissed - Clicked Cancel")


    def handlingInputAlert(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.send_keys("Clicking on OK")
        simpleAlert.accept()
        print(self.driver.find_element(By.ID, "prompt-demo").text)
        print("Alert box Accepted - Clicked OK")

        self.driver.find_element(By.XPATH, "//button[text()='Click for Prompt Box']").click()
        time.sleep(5)
        simpleAlert = self.driver.switch_to.alert
        alertText = simpleAlert.text
        print(alertText)
        simpleAlert.send_keys("Clicking on CANCEL")
        simpleAlert.dismiss()
        print(self.driver.find_element(By.ID, "prompt-demo").text)
        print("Alert box Dismissed - Clicked Cancel")



ha = handleAlerts()
# ha.handlingSimpleAlert()
# ha.handlingConfirmationAlert()
ha.handlingInputAlert()


