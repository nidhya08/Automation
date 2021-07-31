from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import os

driver = webdriver.Chrome()
driver.get(os.environ['web_addrress'])
login_button = driver.find_element_by_xpath(os.environ['login_button_xpath'])
login_button.click()

wait = WebDriverWait(driver, 5)
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, os.environ['submit_button_xpath'])))
emp_id_field = driver.find_element_by_xpath(os.environ['user_text_xpath'])
emp_id_field.send_keys('124580')
emp_pwd_field = driver.find_element_by_xpath(os.environ['password_xpath'])
emp_pwd_field.send_keys(os.environ['temp_password'])

submit_button.click()

wait2 = WebDriverWait(driver, 6)
report_button = wait2.until(EC.element_to_be_clickable((By.XPATH, os.environ['report_button_xpath'])))
messagefield = driver.find_element_by_xpath(os.environ['temp_field_xpath'])
# If you want to randomly choose temperature, then uncomment below lines otherwise this code
# will open the site and login for you, then you can enter your temperature and save it

# temp_value = round(random.uniform(35.8, 36.8),1)
# messagefield.send_keys(temp_value)
# report_button.click()

