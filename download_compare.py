#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from docx_simple_service import SimpleDocxService
from getURL_compare import getURL_compare
import commands

options = Options()
# ブラウザ立ち上げを無効にする
# options.set_headless(True)

def download_compare(word, download_directory):
    url = getURL_compare(word)

    print url

    loginurl = 'https://app.mieru-ca.com/faber-extract/'

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(loginurl)

    # ID/PASSを入力
    id = driver.find_element_by_id("txt_email_login")
    id.send_keys("cyattky@gmail.com")
    password = driver.find_element_by_id("txt_password")
    password.send_keys("Cyattky!01b")

    time.sleep(1)

    #ボタン押す
    driver.find_element_by_xpath('//*[@id="frm_login"]/div[3]/button').click()

    time.sleep(3)

    driver.get(url)

    time.sleep(7)

    driver.find_element_by_xpath('//*[@id="div_btn_action"]/a[2]').click()

    time.sleep(10)

    driver.quit()

    movefile(word, download_directory)


def movefile(word, directory):
    res = commands.getoutput("ls -tl " + directory)
    filename = res.split("\n")[1].split(" ")[-1]

    res = commands.getoutput("mv " + directory + filename.replace("&", "\&") + " ./data/" + word)
    print res


if __name__ == "__main__":
    movefile("電通　過労死", "~/Downloads/")