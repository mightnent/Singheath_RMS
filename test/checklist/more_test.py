#create checklist and pass in script like input into the comment box
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome('D:\\python\chromedriver.exe')
browser.get('https://app.savourapp.co/login')
username = browser.find_element_by_id('id_username')
username.send_keys('admin')
password = browser.find_element_by_id('id_password')
password.send_keys('savourpassword')
submit = browser.find_element_by_id('sign-in')
submit.click()
time.sleep(1)
coupon = browser.find_element_by_link_text("Coupons")
coupon.click()
time.sleep(1)