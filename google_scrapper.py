from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class GoogleKeywordScreenshooter:

    def __init__(self,keyword,screenshots_dir):
        self.options = Options()
        self.options.add_experimental_option("detach",True)
        self.options.add_experimental_option("excludeSwitches",["enable-logging"])
        self.options.add_argument("--force-device-scale-factor=1")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.screenshots_dir = screenshots_dir
        self.keyword = keyword
    
    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element(By.CLASS_NAME,"gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        shitty_elements = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"Wt5Tfe")))

        for shitty_element in shitty_elements:
            try:
                self.browser.execute_script(
                    """
                    const shitty = arguments[0]
                    shitty.parentElement.removeChild(shitty)
                    """
                ,shitty_element)
            except Exception:
                pass
        
        search_results = self.browser.find_elements(By.CLASS_NAME,"g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}{index}.png")
    
    def finish(self):
        self.browser.quit()

domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()






