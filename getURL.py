#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import common

def getURL(word):
    options = Options()
    # ブラウザ立ち上げを無効にする
    # options.set_headless(True)

    searchurl = 'https://app.mieru-ca.com/faber-extract/suggest-keyword-network'
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(searchurl)

    # ID/PASSを入力
    id = driver.find_element_by_id("txt_email_login")
    id.send_keys("cyattky@gmail.com")
    password = driver.find_element_by_id("txt_password")
    password.send_keys("Cyattky!01b")

    time.sleep(1)

    # ボタン押す
    driver.find_element_by_xpath('//*[@id="frm_login"]/div[3]/button').click()

    time.sleep(10)

    id = driver.find_element_by_id("txt_keyword")
    id.send_keys(word.decode('utf-8'))

    time.sleep(3)

    # ボタン押す
    driver.find_element_by_xpath('//*[@id="btn_search"]').click()
    time.sleep(3)

    try:
        driver.find_element_by_xpath('//*[@id="frm_reload_old_search"]/div[3]/button[1]').click()
        print '-------Reuse old search results-------'
        time.sleep(15)

    except common.exceptions.ElementNotVisibleException:
        print '-------Make new results-------'
        time.sleep(60)

    targeturl = driver.find_elements_by_xpath('//*[@id="tbody_result"]/tr[1]/td[5]/a')[0].get_attribute('href')

    # time.sleep(20)
    #
    # targeturl = driver.current_url
    driver.quit()

    return targeturl

if __name__ == "__main__":
    getURL("電通　年収")



