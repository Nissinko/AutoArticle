#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from docx_simple_service import SimpleDocxService
from getURL import getURL
from getsearch import getsearch
from download_compare import download_compare
import commands

# to be set
download_directory = "~/Download"

options = Options()
# ブラウザ立ち上げを無効にする
# options.set_headless(True)

word = '電通　過労死'

# make directory
commands.getoutput('mkdir ./data/' + word)

url = getURL(word)

print url

splitword = word.split('　')


#アクセスするURL
# url = 'https://app.mieru-ca.com/faber-extract/suggest-keyword-network?keyword=%E9%9B%BB%E9%80%9A&input=google_JP&action=view'
# url = 'https://app.mieru-ca.com/faber-extract/suggest-keyword-network?keyword=%E5%B0%B1%E6%B4%BB%E3%80%80%E8%85%95%E6%99%82%E8%A8%88&input=google_JP&action=view'
loginurl = 'https://app.mieru-ca.com/faber-extract/'

driver = webdriver.Chrome(chrome_options=options)
driver.get(loginurl)

# ID/PASSを入力
id = driver.find_element_by_id("txt_email_login")
id.send_keys("hoge")
password = driver.find_element_by_id("txt_password")
password.send_keys("hoge")

time.sleep(1)

#ボタン押す
driver.find_element_by_xpath('//*[@id="frm_login"]/div[3]/button').click()

time.sleep(3)

driver.get(url)

time.sleep(3)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")

# print soup.select_one('#hub-terms > a:nth-of-type(2)')
Hub = [l.text for l in soup.select('#hub-terms > a')]
for h in Hub:
    print h

Hubstr = [h.encode('utf-8') for h in Hub]
# Hubstr.remove(word)

# Keyword = [l.text for l in soup.select('#url_modal_body > a')]
# for k in Keyword:
#     print k

time.sleep(1)

key = driver.execute_script('return idKeywordGlobal;')

# driver.execute_script("getSuggestWord({});".format(key))

script = ''.join(open('test.txt').readlines())
script = script.replace('Number', key)

res = driver.execute_script(script).encode('utf-8')
reslist = res.rstrip(']').lstrip('[').split(",")

# print reslist

for r in reslist:
    print r.strip('"')

time.sleep(3)

# chromeを閉じる
driver.quit()

#docxファイル作業
docx = SimpleDocxService()
#フォント設定
docx.set_normal_font("Courier New", 9)
docx.add_head(word.decode('utf-8'), 0)

#キーワードリストの整理 & タグ化
keywordlist = [r.strip('"').split(" ") for r in reslist]

#ノードの羅列
nodelist = []

for key in keywordlist:
    for k in key:
        nodelist.append(k)

node_unique = list(set(nodelist))

for w in splitword:
    node_unique.remove(w)

docx.open_text()

for n in node_unique:
    print n
    docx.add_text(n.decode('utf-8'))
    docx.add_text("\n")

docx.close_text()

filename = "./data/" + word + "/" + word + "_mieruca.docx"
docx.save(filename)

getsearch(word)

download_compare(word, download_directory)


# for Hs in Hubstr:
#     headword = word + " " + Hs
#     docx.add_head(headword.decode('utf-8'), 1)
#     docx.open_text()
#     for key in keywordlist:
#         if (Hs in key) and (word in key):
#             key.remove(Hs)
#             key.remove(word)
#             if len(key) != 0:
#                 text = ' '.join(key)
#                 docx.add_text(text.decode('utf-8'))
#                 docx.add_text("\n")
#     docx.close_text()
#
# docx.save("test.docx")






