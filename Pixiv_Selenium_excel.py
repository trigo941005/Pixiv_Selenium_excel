import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# 設置無痕模式
chrome_options = Options()
chrome_options.add_argument("--incognito")

# 啟動無痕模式的瀏覽器
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.pixiv.net/tags/%E3%83%8E%E3%83%A9%E3%82%AC%E3%83%9F/illustrations?order=date&p=8')
driver.maximize_window()
# 找到圖片元素
wait = WebDriverWait(driver, 3)
time.sleep(3)
#image_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "//img[@alt='#オリジナル ノラガミ - ゾディアック的插畫']")))
# 找到圖片元素
# 找到圖片元素
image_element = driver.find_element(By.XPATH,"#野良神【腐】 蠃蚌夜トログ - solenge的插畫']")
#image_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='#オリジナル ノラガミ - ゾディアック的插畫']")))
image_url = image_element.get_attribute("src")
print(image_url)
# 下載圖片
img_data = requests.get(image_url).content
with open('image.jpg', 'wb') as handler:
    handler.write(img_data)
"""image_elements = driver.find_elements(By.TAG_NAME, "img")
print(len(image_elements))
count = 0
for image_element in image_elements:
    # 取得圖片 URL
    image_url = image_element.get_attribute('src')
    print(image_url)
# 使用 requests 下載圖片
    img_data = requests.get(image_url).content
    # 將圖片保存到本地
    with open('downloaded_image%d.jpg'%count, 'wb') as handler:
        handler.write(img_data)
    count+=1"""
# 關閉瀏覽器
driver.quit()
