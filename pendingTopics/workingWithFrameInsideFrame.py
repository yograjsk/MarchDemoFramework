from selenium import webdriver
from selenium.webdriver.common.by import By


class handleIframes():
    def handleTheIframe(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10);
        self.driver.get("http://demo.automationtesting.in/Frames.html")
        self.driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()
        iframes = self.driver.find_elements_by_tag_name("iframe")
        print("count of iframes: ", len(iframes))
        for i in iframes:
            print(i.get_attribute("src"))
            if "MultipleFrames.html" in i.get_attribute("src"):
                self.driver.switch_to.frame(i)
                iframes2 = self.driver.find_elements_by_tag_name("iframe")
                print("count of iframes inside this iframe: ", len(iframes2))
                self.driver.switch_to.frame(i)
                for a in iframes2:
                    print(a.get_attribute("src"))
                    if "SingleFrame.html" in a.get_attribute("src"):
                        self.driver.switch_to.frame(a)
                        self.driver.find_element_by_tag_name("input").send_keys("This is the input box inside iframe of an iframe")



# //div[@class='container']//input

hf = handleIframes()
hf.handleTheIframe()