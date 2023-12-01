from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from casos import T01, T02, T05, T03, T07, T08, T10, T13, T14, T15

chromedriver_exe = r'chromedriver.exe'
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(chromedriver_exe), options=options)
driver.get('https://type-shop.vercel.app/')

# T01(driver)

# T02(driver)

# T05(driver)

# T03(driver)

# T07(driver)

# T08(driver)

# T10(driver)

# T13(driver)

# T14(driver)

T15(driver)

sleep(5)

# sleep(5)