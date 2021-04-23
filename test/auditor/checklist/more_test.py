#create checklist and pass in script like input into the comment box
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome('D:\\python\chromedriver.exe')
browser.get('http://13.250.116.16:8000/')
username = browser.find_element_by_name('username')
username.send_keys('auditor')
password = browser.find_element_by_id('pw')
password.send_keys('password1.1')
submit = browser.find_element_by_name("login")
submit.click()
time.sleep(1)
browser.get("http://13.250.116.16:8000/new-audit")
time.sleep(1)
select_tenant = Select(browser.find_element_by_class_name('tenants'))
select_tenant.select_by_index(1)
select_checklist = Select(browser.find_element_by_name('checklist'))
select_tenant.select_by_index(2)
create_button = browser.find_elements_by_id("b1")
create_button.click()
time.sleep(1)
comment = browser.find_element_by_name("comment")
#pass in script
comment.send_keys("<script>alert(‘XSS’)</script>")
nextBtn = browser.find_elements_by_class_name("next")
nextBtn.click()
#pass in non-photo
upload = browser.find_element_by_id("actual-btn")
upload.send_keys("D:\\document.pdf")
nextBtn.click()

