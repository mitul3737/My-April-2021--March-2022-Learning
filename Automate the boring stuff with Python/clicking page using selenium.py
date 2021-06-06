"""Link for the geckodriver : https://github.com/mozilla/geckodriver/releases"""
from selenium import webdriver
browser=webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')
linkElem=browser.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()
