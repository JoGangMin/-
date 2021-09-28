from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

def create_folder():
    pass

def waite_element(css_selector):
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )


def move_target_page(url):
    driver.get(url)