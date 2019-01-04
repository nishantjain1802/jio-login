from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

jio_id = "ENTER YOUR JIO-ID HERE"
pswd = "ENTER YOUR PASSWORD HERE"

driver = webdriver.Firefox()
driver.get("https://www.jio.com/JioWebApp/index.html?root=login")
time.sleep(2)

user_id = driver.find_element_by_id("jio-ui-id-3")
user_id.send_keys(jio_id)
time.sleep(2)

password = driver.find_element_by_id("jio-ui-id-4")
password.send_keys(pswd)
time.sleep(2)

login = driver.find_element_by_class_name("loginBtnEnable")
login.click()


