from selenium import webdriver


class workingWithTabs():

    def handleWindowTabs(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        # set implicit time to 30 seconds
        self.driver.implicitly_wait(5);
        # navigate to the url
        self.launchURLInNewTab(self.driver, "http://www.google.com")
        self.launchURLInNewTab(self.driver, "http://stackoverflow.com")
        self.launchURLInNewTab(self.driver, "http://gmail.com")
        # self.driver.get("http://www.google.com");
        # self.driver.execute_script("window.open('');")
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # # driver.switch_to_window()
        # self.driver.get("http://stackoverflow.com")
        # self.driver.execute_script("window.open('');")
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.get("http://gmail.com")
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 't')
        # Actions.send_keys(Keys.CONTROL + "T").perform()
        # Actions.key_down(Keys.CONTROL).send_keys("T").key_up(Keys.CONTROL).perform()
        # get the Session id of the Parent
        totalBrowserWindows_tabs = self.driver.window_handles
        print("total browser tabs", len(totalBrowserWindows_tabs))
        for i in totalBrowserWindows_tabs:
            # self.driver.switch_to.window(i)
            print(i)
            self.driver.switch_to.window(self.driver.window_handles[totalBrowserWindows_tabs.index(i)])
            print(totalBrowserWindows_tabs.index(i), self.driver.title)

    def launchURLInNewTab(self, driver, url):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)


tabs = workingWithTabs()
tabs.handleWindowTabs()
