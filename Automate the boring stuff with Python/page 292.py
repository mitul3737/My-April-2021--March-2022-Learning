"""Link for the geckodriver : https://github.com/mozilla/geckodriver/releases"""
from selenium import webdriver
browser=webdriver.Firefox()
print(type(browser))
browser.get('https://inventwithpython.com')
