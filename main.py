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

KEYWORD = "buy domain"

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

browser.get("https://google.com")


search_bar = browser.find_element(By.CLASS_NAME,"gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements(By.CSS_SELECTOR,".MjjYud")

shitty_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"Wt5Tfe")))

print(shitty_element)

# for index, search_result in enumerate(search_results):
#     class_name = search_result.get_attribute("class")
#     print(class_name)
#     if "ULSxyf" not in class_name:
#         capture = search_result.screenshot(f"screenshots/{KEYWORD}{index}.png")
    
browser.close()