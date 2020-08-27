from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

wb = webdriver.Chrome()
wb.implicitly_wait(10)

wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=1')


i = 0
for i in range(0,9):
    # 获取单击两次那个按钮
    button = wb.find_element_by_xpath('//a[@class="layui-laypage-next"]')
    # 点击按钮
    button.click()
    sleep(2)
    print("第", i, "次")