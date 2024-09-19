from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urls = [
     "https://games.arcadebrilliance.com/en/stellar-conceptual-2048-forever/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-hidden-object-city/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-coffee-drip/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-superhero-memory-match-hd/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-ball-drop/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-sort-the-trash-drag-and-drop/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-omg-word-professor/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-word-finder-pro/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-sommelier-pour/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469",
"https://games.arcadebrilliance.com/en/stellar-conceptual-mini-crossword/index.html?m=57986295ed0a1b8145a3d8d8725edcabdbccd469"
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
