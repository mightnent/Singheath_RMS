import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


pw = "password1.1"
auditor_user = "testAuditor1"
admin_user = "admin"
   
def test_Correct_login():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys(admin_user)
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    time.sleep(1)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin/"
    assert currentURL == targetUrl
    
def test_Wrong_username1():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys("admi")
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin"
    assert currentURL != targetUrl
    
def test_Wrong_username2():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys("admi'0'")
    driver.find_element_by_name("password").send_keys(pw)
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin"
    assert currentURL != targetUrl
    
def test_Wrong_password1():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys(admin_user)
    driver.find_element_by_name("password").send_keys("password1.")
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin"
    assert currentURL != targetUrl
    
def test_Wrong_password2():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys(admin_user)
    driver.find_element_by_name("password").send_keys("Password1.1")
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin"
    assert currentURL != targetUrl
    
def test_Wrong_password3():
    driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
    driver.get("http://13.250.116.16:8000/")
    driver.find_element_by_name("username").send_keys(admin_user)
    driver.find_element_by_name("password").send_keys("Password11")
    driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)
    currentURL = driver.current_url
    driver.close()
    targetUrl = "http://13.250.116.16:8000/admin"
    assert currentURL != targetUrl