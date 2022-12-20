from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

options = Options()
options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches",["enable-logging"])
options.add_argument("--force-device-scale-factor=1")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("http://google.com")
browser.maximize_window()

sizes = [320,480,1024,1366,1920]

current_size = browser.get_window_size()

for size in sizes:
    browser.set_window_size(size,current_size["height"])
    print(browser.get_window_size())
