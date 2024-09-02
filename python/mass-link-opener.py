from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urls = [
     "https://link1.com",
     "https://link2.com"
]

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(urls[0])
time.sleep(0.001)

for url in urls[1:]:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    time.sleep(0.001)

print("All tabs are opened.")

# Infinte loop to keep the tabs open
while True:
    time.sleep(1)
