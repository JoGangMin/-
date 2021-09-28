from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src import driver

import time

def cycle_products(action):
    
    for product in driver.find_elements(By.CSS_SELECTOR, "#body_div > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > div > div")[:1]:
        product.click()

        time.sleep(3)

        action(product)

def get_product_info(product:webdriver.Chrome):
    name, price = driver.execute_script("""
    
    name = document.querySelector("#body_div > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td > span").innerText
    price = document.querySelector("#ptable > tbody > tr:nth-child(2) > td.pricediv").childNodes[0].data


    return [name, price]
    
    """)
    
    # 옵션들
    # option_element_list = product.find_elements_by_css_selector("#psel > tbody > tr > td.livlue > select")
    option_element_list = driver.execute_script("""return document.querySelectorAll("#psel > tbody > tr > td.livlue > select")""")

    # option_value_list 

    for option_element in option_element_list:

        option_value = option_element.get_attribute("dataset")['htmlText']
        print(option_value)
        pass
    print(f"{name}, {price}")
