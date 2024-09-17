import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import csv

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 启用无头模式
# options.add_argument("--disable-gpu")  # 禁用 GPU 加速
# options.add_argument("--window-size=1920,1080")  # 设置窗口大小
options.add_argument(r"--start-maximized")
# options.add_experimental_option("detach", True)
options.add_argument(
    r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
)
options.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=options)

driver.get("https://pgy.xiaohongshu.com/")

