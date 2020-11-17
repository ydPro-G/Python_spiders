# 获取网页标签，点击下一页 
from selenium import webdriver
from time import sleep

wb = webdriver.Chrome()

driver = wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=3') # 获取网址

page = 0
while page < 9:
    filename = 'CP.txt'

    # 获取标签，写入文件
    with open(filename,'a') as f_obj:
        elements = wb.find_elements_by_xpath('//span[@class="cp-novel-type"] | //span[@class="cp-novel-tag"]')
        for element in elements:
            f_obj.write(element.text + '\n')
            
    # 下一页 循环+1
    wb.find_element_by_xpath('//a[@class="layui-laypage-next"]').click()  
    page = page + 1
    sleep(2)


