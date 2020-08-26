from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

wb = webdriver.Chrome()

wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=3')
all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')
s = len(all)

for i in range(s):
    all[i].click()
    sleep(1)
    wb.back()
    all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')

