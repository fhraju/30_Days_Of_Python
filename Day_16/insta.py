# import getpass



# my_password = getpass.getpass("Enter your password: ")
# print(my_password)
import time
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

browser = webdriver.Chrome()
url = "https://www.instagram.com"
browser.get(url)

time.sleep(2)
username_el = browser.find_element(by="name", value="username")
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element(by="name", value="password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(2)
submit_btn_ele = browser.find_element(by="css selector", value="button[type='submit']")
submit_btn_ele.click()



body_el = browser.find_element(by="css selector", value="body")
html_text = body_el.get_attribute("innerHTML")

#print(html_text)
def click_to_follow(browser):
    #my_follow_btn_xpath = "//a[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
    #my_follow_btn_xpath = "//*[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
    follow_btn_elements = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elements:
        time.sleep(2) # for self_throttle
        try:
            btn.click()
        except:
            pass

time.sleep(6)
the_rock_url = "https://www.instagram.com/therock/"
browser.get(the_rock_url)

post_url_pattern = "https://www.instagram.com/p/<post-slug-id>/"
post_xpath_str = "//a[contains(@href,'/p/')]"
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link_el = None
if len(post_links) > 0:
    post_link_el = post_links[0]

if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_elements_by_xpath("//video")

images_els = browser.find_elements_by_xpath("//img")

for img in images_els:
    print(img.get_attribute('src'))
