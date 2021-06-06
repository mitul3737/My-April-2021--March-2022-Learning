"""Link for the geckodriver : https://github.com/mozilla/geckodriver/releases"""
from selenium import webdriver
browser=webdriver.Firefox()
print(type(browser))
browser.get('https://login.metafilter.com')
userElem=browser.find_element_by_id('user_name')
userElem.send_keys('Shahriyar_3737') #use your username here which wilbe displayed at the page
passwordElem=browser.find_element_by_id('user_pass')
passwordElem.send_keys('1234567') # your password here
passwordElem.submit()

