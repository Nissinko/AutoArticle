#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from docx_simple_service import SimpleDocxService

options = Options()
driver = webdriver.Chrome(chrome_options=options)

def getsearch(word):

    docx = Writedocx(word)

    googleurl = 'https://www.google.co.jp/'
    searchurl = googleurl + 'search?q=' + word
    driver.get(searchurl)

    all_search = driver.find_elements_by_class_name('rc')
    for data in all_search:
        title = data.find_element_by_tag_name('h3').text
        url = data.find_element_by_css_selector('h3 > a').get_attribute('href')

        try:
            h2list, h3list = geth2h3(url)

            print title
            for h2 in h2list:
                print h2
            for h3 in h3list:
                print h3

            docx.write(title, url, h2list, h3list)
        except:
            continue
        time.sleep(3)

    # chromeを閉じる
    driver.quit()

    filename = "./data/" + word + "/" + word + "_検索.docx"
    docx.save(filename)


def geth2h3(url):
    # resp = requests.get(url)
    # html = resp.text
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    time.sleep(3)

    h2list = []
    h3list = []

    h2tag = soup.find_all("h2")
    for h2t in h2tag:
        # print h2t.text
        if h2t.text != "":
            h2list.append(h2t.text)

    h3tag = soup.find_all("h3")

    for h3t in h3tag:
        # print h3t.text
        if h3t.text != "":
            h3list.append(h3t.text)

    return h2list, h3list


class Writedocx:
    def __init__(self, word):
        #docxファイル作業
        self.docx = SimpleDocxService()
        #フォント設定
        self.docx.set_normal_font("Courier New", 9)
        self.docx.add_head(word.decode('utf-8'), 0)

    def write(self, title, url, h2list, h3list):
        self.docx.add_head(title, 1)
        self.docx.open_text()
        self.docx.add_text("URL:\n")
        self.docx.add_text(url.decode('utf-8'))
        self.docx.add_text("\n\n")

        self.docx.add_text("h2:\n")
        for h2 in h2list:
            self.docx.add_text(h2)
            self.docx.add_text("\n")

        self.docx.add_text("\n")
        self.docx.add_text("h3:\n")

        for h3 in h3list:
            self.docx.add_text(h3)
            self.docx.add_text("\n")
        self.docx.close_text()

    def save(self, name):
        self.docx.save(name)


if __name__ == '__main__':
    getsearch('第二新卒 ')




