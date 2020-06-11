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
    def __init__(self, profile):
        super().__init__()
        self.profile = profile
        self.init_driver()

    def init_driver(self):
        options = Options()
        options.add_argument("--headless")
        # profile = "C:\\Users\\noname\\Documents\\file\\firefox-profile\\j7nj8gnr.user1"

        self.driver = Firefox(firefox_profile=self.profile, executable_path="C:\\Users\\noname\\Documents\\file\\geckodriver.exe", firefox_options=options)

    def get_driver(self):
        return self.driver

    def stop(self):
        self.driver.close()
        self.driver.quit()


class Youtube:
    def __init__(self, driver, file_name, title, file_thumb=""):
        self.url_upload = "https://youtube.com/upload"
        self.driver = driver
        self.file_name = file_name
        self.title = title
        self.file_thumb = file_thumb

    def init(self):
        self.driver.get(self.url_upload)
        time.sleep(4)

        input_file = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='Filedata']"))
        )

        input_file.send_keys(self.file_name)

        input_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#textbox"))
        )

        input_thumb = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#file-loader"))
        )

        input_thumb.send_keys(self.file_thumb)
        input_title.clear()
        input_title.send_keys(self.title)

        btn_next = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#next-button"))
        )

        btn_kid = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='NOT_MADE_FOR_KIDS']"))
        )

        btn_kid.click()

        time.sleep(2)
        btn_next.click()

        time.sleep(2)
        btn_next.click()

        btn_set_public = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='PUBLIC']"))
        )

        btn_set_public.click()
        time.sleep(0.5)
        btn_done = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#done-button"))
        )

        btn_done.click()
        time.sleep(2)

        while True:
            label_percent_process = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "paper-progress.ytcp-video-upload-progress"))
            )
            val = label_percent_process.get_attribute("value")

            if int(val) >= 100:
                time.sleep(1)
                break

            time.sleep(1)


def upload(profile, file_name, title, file_thumb):
    web = FirefoxBrowser(profile)
    driver = web.get_driver()

    yt = Youtube(driver, file_name, title, file_thumb)
    yt.init()

    driver.quit()


if __name__ == "__main__":
    profile = "C:\\Users\\noname\\Documents\\file\\firefox-profile\\j7nj8gnr.user1"
    file_name = "C:\\Users\\noname\\Downloads\\Thám Tử Lừng Danh Conan - Tập 43 - Vụ Án Mạng Ở Công Ty Vệ Sinh Mambo - Conan Lồng Tiếng Mới Nhất-ZUO5Kq8Odgc.mkv"
    title = "Thám Tử Lừng Danh Conan - Tập 43 - Vụ Án Mạng Ở Công Ty Vệ Sinh Mambo - Conan Lồng Tiếng Mới Nhất"
    file_thumb = "C:\\Users\\noname\\Downloads\\thumb.png"

    upload(profile, file_name, title, file_thumb)
