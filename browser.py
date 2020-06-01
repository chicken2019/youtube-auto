from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self):
        self.driver = None


class FirefoxBrowser(Browser):
    def __init__(self):
        super().__init__()
        self.init_driver()

    def init_driver(self):
        profile = "C:\\Users\\noname\\Documents\\file\\firefox-profile\\j7nj8gnr.user1"

        self.driver = Firefox(firefox_profile=profile, executable_path="C:\\Users\\noname\\Documents\\file\\geckodriver.exe")

    def get_driver(self):
        return self.driver

    def stop(self):
        self.driver.close()
        self.driver.quit()


class Youtube:
    def __init__(self, driver):
        self.url_upload = "https://youtube.com/upload"
        self.driver = driver

    def init(self):
        self.driver.get(self.url_upload)
        time.sleep(2)

        input_file = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#select-files-button"))
        )

        input_file.click()


    def run(self):
        pass



web = FirefoxBrowser()
driver = web.get_driver()
yt = Youtube(driver)
yt.init()