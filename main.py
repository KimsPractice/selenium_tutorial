from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

browser.get("https://google.com")