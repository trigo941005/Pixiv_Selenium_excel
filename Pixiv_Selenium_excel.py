import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import re

# 設置無痕模式
chrome_options = Options()
chrome_options.add_argument("referer=https://www.pixiv.net/tags")

# 启动无痕模式的浏览器
driver = webdriver.Chrome(options=chrome_options)
headers = {
    'Referer': 'https://www.pixiv.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://www.pixiv.net/tags/%E3%83%8E%E3%83%A9%E3%82%AC%E3%83%9F/illustrations?order=date&p=8'
driver.get(url)
driver.maximize_window()

# 等待頁面載入
time.sleep(5)

# 創建目錄存放圖片
if not os.path.exists('images'):
    os.makedirs('images')

# 設定滾動等待時間
scroll_pause_time = 1

# 獲取當前滾動高度
last_height = driver.execute_script("return window.scrollY;")
count = 0
while True:
# 滾動一小段
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(scroll_pause_time)
    
    # 檢查滾動後的高度
    new_height = driver.execute_script("return window.scrollY;")
    if new_height == last_height:
        break  # 已經到頁面底部

    last_height = new_height
    # 查找所有 img 標籤元素
    #image_elements = driver.find_elements(By.TAG_NAME, 'img')
    image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'sc-rp5asc-10') and contains(@class, 'jBxEmj')]")
    
    image_elements = image_elements[4:]

    title = driver.find_elements(By.XPATH,"//*[contains(@class, 'sc-d98f2c-0') and contains(@class, 'sc-iasfms-6') and contains(@class, 'gqlfsh')]")
print(len(title))
    # 下載圖片
for i in range(len(image_elements)):
    image_url = image_elements[i].get_attribute("src")
    if image_url and ("jpg" in image_url or "png" in image_url):
        img_data = requests.get(image_url, headers=headers).content
        valid_filename = re.sub(r'[<>:"/\\|?*]', '', title[i].text)  # 使用正則表達式替換無效字符
        filename = f'images/{valid_filename}.jpg'
        with open(filename, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image {i}: {image_url}")
    else:
        print(f"Invalid URL for image {i}")

# 關閉瀏覽器
driver.quit()
