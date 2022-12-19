from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
chrome_options.add_argument("--force-device-scale-factor=1")

KEYWORD = "buy domain"

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
browser.get("https://google.com")


search_bar = browser.find_element(By.CLASS_NAME,"gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

shitty_elements = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"Wt5Tfe")))

for shitty_element in shitty_elements:
    browser.execute_script(
        """
        const shitty = arguments[0]
        shitty.parentElement.removeChild(shitty)
        """
    ,shitty_element)

search_results = browser.find_elements(By.CLASS_NAME,"g")

for index, search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{index}.png")
