from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
messagefield = driver.find_element_by_xpath('//*[@id="user-message"]')
messagefield.send_keys("God is good!")
showbutton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showbutton.click()

additionfield1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionfield1.send_keys(802)
additionfield2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionfield2.send_keys(1508)
totalbutton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
totalbutton.click()
