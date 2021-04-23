import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import time
from selenium.webdriver.support.wait import WebDriverWait

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
number_list = "123456789"

input_list = list(alphabet_lower + alphabet_upper + number_list)

def gen_expr(Expr):
    return random.choice(["Expr+Term", "Expr-Term", "Expr!Term", "Expr@Term", "Expr&Term", "Expr{Term", "Expr}Term","Term" ])


def gen_term(Term):
    return random.choice(["Term*Factor", "Term/Factor", "Term$Factor", "Term^Factor", "Term(Factor", "Term)Factor", "Factor"])


def gen_factor(Factor):
    return random.choice(["-Integer", "Expr", "Integer", "Integer.Integer"])


def gen_integer(Integer):
    return random.choice(["Digit", "IntegerDigit"])


def gen_digit(Digit):
    return random.choice(input_list)


def fuzzer():
    output = "Expr"
    while "Expr" in output:
        output = gen_expr(output)
        while "Term" in output:
            output = output.replace("Term", gen_term("Term"), 1)
        while "Factor" in output:
            output = output.replace("Factor", gen_factor("Factor"), 1)
        while "Integer" in output:
            output = output.replace("Integer", gen_integer("Integer"), 1)
        while "Digit" in output:
            output = output.replace("Digit", gen_digit("Digit"), 1)
    return output

def String_generator():
    sGenerated = ""
    i=0
    while i<times:
        fuzzGen = fuzzer()
        sGenerated = sGenerated + fuzzGen
        i += 1
    return sGenerated

random.seed(datetime.now())
times = random.randint(3, 10)

driver = webdriver.Chrome('D:/Joon Kang/chromedriver.exe')
# driver.get("http://localhost:8000/")
driver.get("http://13.250.116.16:8000/");

admin_password = "password1.1"
auditor_user = "testAuditor1"


for i in range(times):
    uName = String_generator()
    time.sleep(2)
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(uName)
    driver.find_element_by_name("password").send_keys(admin_password)
    cBox = driver.find_element_by_id("cBox").click()
    time.sleep(2)
    submit_button = driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)

time.sleep(2)
driver.find_element_by_name("username").clear()
username = driver.find_element_by_name("username").send_keys(auditor_user)
password = driver.find_element_by_name("password").send_keys(admin_password)
cBox = driver.find_element_by_id("cBox").click()
time.sleep(2)
submit_button = driver.find_element_by_css_selector("button[name='login']").send_keys(Keys.RETURN)