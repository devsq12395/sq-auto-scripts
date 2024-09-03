from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urls = [
     "https://safesites.marketjs-cloud2.com/en/safesites-whats-grandma-hiding/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-coin-empire-advanced/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-omg-zombie-run/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-king-kong-kart-racing/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-idle-mole-empire/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-office-wrestling-royale/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-hercules-climb/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-ball-jump/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-snake-blockade/index.html",
"https://safesites.marketjs-cloud2.com/en/safesites-evade-the-missile/index.html",
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
