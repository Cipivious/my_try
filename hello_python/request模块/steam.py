import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import csv

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 启用无头模式
# options.add_argument("--disable-gpu")  # 禁用 GPU 加速
# options.add_argument("--window-size=1920,1080")  # 设置窗口大小
options.add_argument(r"--start-maximized")
options.add_experimental_option("detach", True)
options.add_argument(
    r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
)
options.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=options)

driver.get(
    "https://steamcommunity.com/profiles/76561199349975453/games/?tab=all"
)


time.sleep(2)

# 滚动到底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

items = driver.find_elements(by=By.XPATH, value='//*[@id="responsive_page_template_content"]/div[3]/div/div[6]/div')

info = []
for item in items:
    name = item.find_element(by=By.XPATH, value='./div/span/a').text
    print(name)
    try:
        play_time = item.find_element(by=By.XPATH, value='./div/div[1]/span[1]').text.split('\n')[1]
    except:
        play_time = ''
    try:
        storage = item.find_element(by=By.XPATH, value='./div/div[4]/div/span').text
    except:
        storage = ''
    info.append([name, play_time, storage])


driver.quit()
with open("./info.csv", "w", encoding="utf-8") as f:
    csvfile = csv.writer(f)
    csvfile.writerow(["游戏名称", "游戏时间", "游戏大小"])
    csvfile.writerows(info)


