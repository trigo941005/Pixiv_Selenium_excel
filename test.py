import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import re
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image

def next_page():
    global driver
    # 查找具有特定 class 的元素
    elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'sc-d98f2c-0') and contains(@class, 'sc-xhhh7v-2') and contains(@class, 'cCkJiq') and contains(@class, 'sc-xhhh7v-1-filterProps-Styled-Component') and contains(@class, 'kKBslM')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", elements[1])
    elements[1].click()

chrome_options = Options()
driver = webdriver.Chrome()
headers = {
    'Referer': 'https://www.pixiv.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://www.pixiv.net/tags/%E3%83%8E%E3%83%A9%E3%82%AC%E3%83%9F/illustrations'
driver.get(url)
driver.maximize_window()

for i in range(9):
    time.sleep(1)
    next_page()
