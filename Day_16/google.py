
import time
from selenium import webdriver

browser = webdriver.Chrome()

url = "https://www.google.com"
browser.get(url)

time.sleep(2)
name = 'q'
search_el = browser.find_element("name","q")
#print(search_el)
search_el.send_keys("selenium python")

submit_btn_ele = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_ele.get_attribute('name'))
time.sleep(2)
submit_btn_ele.click()