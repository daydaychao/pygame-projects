import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


# 取得專案資料夾的絕對路徑
project_folder = project_folder = os.getcwd()
print('folder:=====')
print(project_folder)

# 生成 ChromeDriver 路徑
chrome_driver_path = os.path.join(
    project_folder, '\driver\chromedriver.exe')  # 或其他作業系統的對應檔案

# 设置 PC Chrome 浏览器的选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面模式运行

# 启动 PC Chrome 浏览器
driver = webdriver.Chrome(service=Service(
    chrome_driver_path), options=chrome_options)
print(driver)


def get_weather_data():
    # 發送GET請求獲取網頁內容
    url = 'https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=64'
    driver.get(url)

    # 等待天氣資料生成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.text')))

    # 提取天氣資料
    title = driver.find_element(By.CSS_SELECTOR, '.title').text
    temperature = driver.find_element(By.CSS_SELECTOR, '.tem .tem-C').text
    description = driver.find_element(By.CSS_SELECTOR, '.text').text

    rainDom = driver.find_element(By.CSS_SELECTOR, '.rain').text
    rain = re.search(r'\d+%', rainDom).group()

    # 顯示提取的資料
    print("地區:", title)
    print("溫度:", temperature)
    print("降雨機率:", rain)
    print("天氣狀況:", description)

    return title, temperature, rain, description
