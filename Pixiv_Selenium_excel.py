import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# 設置無痕模式
chrome_options = Options()
chrome_options.add_argument("referer=https://www.pixiv.net/tags")

# 啟動無痕模式的瀏覽器
driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.pixiv.net/tags/%E3%83%8E%E3%83%A9%E3%82%AC%E3%83%9F/illustrations?order=date&p=8'
driver.get(url)
driver.maximize_window()

# 等待頁面載入
time.sleep(5)

# 抓取所有圖片元素
image_elements = driver.find_elements(By.TAG_NAME, 'img')

# 創建目錄存放圖片
if not os.path.exists('images'):
    os.makedirs('images')

# 下載圖片
for i, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute("src")
    if image_url and image_url.startswith('http'):
        img_data = requests.get(image_url).content
        with open(f'images/image_{i}.jpg', 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image {i}: {image_url}")
    else:
        print(f"Invalid URL for image {i}")

# 關閉瀏覽器
driver.quit()
