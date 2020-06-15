import requests
import json
from lxml import html
import re

class Website:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.thumbnail = ""
        self.video_id = ""
        self.series_id = ""
        self.video_url = ""

    def my_request(self, method, url, params=None, verify=True, headers="", response_type="text"):
        if method == "GET":
            req = requests.get(url, verify=verify, headers=headers)
        else:
            req = requests.post(url, data=params, verify=verify, headers=headers)

        if response_type == 'text':
            return req.text
        elif response_type == 'html':
            return html.fromstring(req.text)

        return json.loads(req.content)


class Cimaclub(Website):
    def __init__(self):
        super().__init__()

    def get_info(self, root):
        title_ele = root.xpath("//div[@class='SingleContentTitle']/a/h1/text()")
        self.title = title_ele[0]
        self.description = self.title
        thumbnail_ele = root.xpath("//div[@class='BGCover']/@style")
        thumbnail = thumbnail_ele[0].replace("background-image:url(", "")
        thumbnail = thumbnail.replace(");", "")
        self.thumbnail = thumbnail
        self.video_id = self.title
        bread_crumbs = root.xpath("//div[@class='Breadcrumbs']/ol/li")
        len_bread_crumbs = len(bread_crumbs)
        self.series_id = bread_crumbs[len_bread_crumbs - 2].xpath("a/span/text()")[0]

    def get_list_server(self, root):
        pass

    def download_video(self):


    def get_video_from_iframe(self, url):
        root = self.my_request("GET", url, None, True, "", "html")
        source = root.xpath("//video/source/@src")[0]
        content = self.my_request("GET", source, None, False, "", "text")
        arr = re.findall("https(.*?)\n", content)
        self.video_url = "https" + arr[0]

    def get_video_from_series(self, url):
        root = self.my_request("GET", url, None, True, "", "html")
        self.get_info(root)
        root = self.my_request("GET", url + "/watch", None, True, "", "html")
        url_iframe = root.xpath("//iframe/@src")[0]
        self.get_video_from_iframe(url_iframe)


ci = Cimaclub()

ci.get_video_from_series("https://www.cimaclub.cam/%D9%81%D9%8A%D9%84%D9%85-the-balkan-line-2019-bluray-%D9%85%D8%AA%D8%B1%D8%AC%D9%85")