from selenium import webdriver
from selenium.webdriver.common.by import By

class handleIframes():
    def handleTheIframe(self):
        # // iframe[ @ src = '//aax-eu.amazon-adsystem.com/s/v3/pr?exlist=nsln_imdb&fv=1.0&a=cm']
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10);
        # navigate to the url
        # self.driver.get("https://www.amazon.in/")
        # self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#Open%20New%20Window")
        self.driver.get("http://demo.automationtesting.in/Frames.html")
        iframes = self.driver.find_elements_by_tag_name("iframe")
        frames = self.driver.find_elements_by_tag_name("frame")
        print("total iframes are: " , len(iframes))
        print("total frames are: " , len(frames))

        print("total elements count on the page before switch: ", len(self.driver.find_elements_by_xpath("//*")))
        # self.driver.find_element(By.CLASS_NAME, "analystic").click()
        self.driver.switch_to.frame("singleframe")

        elements = self.driver.find_elements_by_xpath("//*")
        self.driver.find_element_by_xpath("//div[@class='container']//input").send_keys("this is the input inside iframe")
        print("total elements count on the page after switch: ", len(elements))
        for i in elements:
            print(elements.index(i), i.get_attribute("type"))
            print(elements.index(i), i.text)
        # self.driver.switch_to.frame("globalSqa")
        self.driver.switch_to.default_content()
        print("total elements count after coming out of the iframe: ", len(self.driver.find_elements_by_xpath("//*")))


# //div[@class='container']//input

hf = handleIframes()
hf.handleTheIframe()