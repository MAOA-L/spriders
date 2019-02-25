import requests
from lxml import etree
import json


class QZone3:
    def __init__(self, targetUrl):
        self.scheme = "3qzone"
        self.server = "https://www.3qzone.com/"
        self.targetUrl = targetUrl
        self.sections = {}
        self.sectionsFile = "./" + self.scheme + "_sections" + ".txt"
        self.name = ""
        self.headers = {
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept - Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               'Connection': 'Keep-Alive',
               'Host': 'www.3qzone.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/71.0.3578.98 Safari/537.36'}

    def getSection(self):
        sections_html = requests.get(url=self.targetUrl, headers=self.headers).content.decode("GBK")
        sections_parse_html = etree.HTML(sections_html)
        sections = sections_parse_html.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
        for _ in sections:
            if _.xpath("./@href"):
                self.sections[_.xpath("./@href")[0]] = _.text
        with open(self.sectionsFile, "w+", encoding="UTF-8")as f:
            f.write(json.dumps(self.sections, ensure_ascii=False))


    # def

Q = QZone3(targetUrl="https://www.3qzone.com/27_27003/")
Q.getSection()
