from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

wb = webdriver.Chrome()
wb.implicitly_wait(10)

wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=1')
all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')
s = len(all)
filename = 'changpei.txt'
for i in range(s):
    all[i].click() # 获取列表元素的索引，元素索引从0开始依次点击
    sleep(1)
    wb.back()
    sleep(1)
    all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')
wb.find_element_by_xpath('//a[@class="layui-laypage-next"]').click()
               
        
        
        
        
             

    
    
   
    

