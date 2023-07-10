from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file_path = 'C:/Users/DL-IVANOVSKIY/Desktop/Программы/site.html'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(file_path)

def run_script():
    time.sleep(20)
    driver.find_element("xpath", "//thead[@inputtype='checkbox']").click()
run_script()
