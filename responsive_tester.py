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
browser.get("http://www.google.com")


