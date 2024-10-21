import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# 設置無痕模式
chrome_options = Options()
chrome_options.add_argument("referer=https://www.pixiv.net/tags")

# 啟動無痕模式的瀏覽器
driver = webdriver.Chrome(options=chrome_options)
headers = {
    'Referer': 'https://www.pixiv.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://www.pixiv.net/tags/%E3%83%8E%E3%83%A9%E3%82%AC%E3%83%9F/illustrations?order=date&p=8'
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 3)

# 等待頁面載入
time.sleep(5)

# 等待並查找所有 img 標籤元素，即使不可見
image_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# 創建目錄存放圖片
if not os.path.exists('images'):
    os.makedirs('images')

# 下載圖片
for i, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute("src")
    if image_url and image_url.startswith('http'):
        img_data = requests.get(image_url, headers = headers).content
        with open(f'images/image_{i}.jpg', 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image {i}: {image_url}")
    else:
        print(f"Invalid URL for image {i}")

# 關閉瀏覽器
driver.quit()
