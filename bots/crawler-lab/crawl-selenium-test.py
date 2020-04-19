from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/linuxlite/dev-tools/chrome-driver/chromedriver")

url = "https://www.artstation.com/search?q=fantasy&sort_by=relevance"

driver.get(url)

time.sleep(35)
driver.save_screenshot("screenshot.png")
projects = driver.find_elements_by_css_selector('.gallery-grid-link')
print(projects)
images = [ proj.find_element_by_css_selector('.d-block') for proj in projects ]
print(images)

images_urls = [el.get_attribute('src') for el in images]
print(images_urls)

driver.close()



