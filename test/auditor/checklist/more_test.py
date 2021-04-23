#create checklist and pass in script like input into the comment box
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome('D:\\python\chromedriver.exe')
browser.get('http://13.250.116.16:8000/')
username = browser.find_element_by_name('username')
username.send_keys('admin')
password = browser.find_element_by_id('password')
password.send_keys('password1.1')
submit = browser.find_element_by_css_selector("button[name='login']")
submit.click()
time.sleep(1)
browser.get("http://13.250.116.16:8000/new-audit")
time.sleep(1)
select_tenant = Select(browser.find_element_by_class_name('tenants'))
select_tenant.select_by_index(1)
select_checklist = Select(browser.find_element_by_class_name('checklist'))
select_tenant.select_by_index(1)
create_button = browser.find_element_by_css_selector("button[id='b1']")
time.sleep(1)
