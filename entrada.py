from time import sleep
from selenium import webdriver

url = ('https://wwww.instagram.com/')

browser = webdriver.Firefox()
browser.get (url)
sleep(5)
browser.close()