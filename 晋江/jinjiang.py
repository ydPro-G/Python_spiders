from selenium import webdriver
from time import sleep
import os
print(os.getcwd())

wb = webdriver.Chrome()
wb.get('http://www.jjwxc.net/fenzhan/yq/')

# elements = wb.find_elements_by_xpath('//div[@class="b4box"]//ul[@id="mmain3"]//li//dl//dt//a')  # 月榜第一页
# elements = wb.find_elements_by_xpath('//div[@class="b4box"]//ul[@id="mmain3"]//li[@class="jason2"]//dl//dt//a') # 月榜第二页
elements = wb.find_elements_by_xpath('//div[@class="b4box"]//ul[@id="mmain2"]//li//dl//dt//a') # 新晋榜第一页
# elements = wb.find_elements_by_xpath('//div[@class="b4box"]//ul[@id="mmain2"]//li[@class="jason2"]//dl//dt//a')# 新晋榜第二页


mainWindow = wb.current_window_handle
filename = 'article.txt'

for element in elements:
    wb.switch_to_window(mainWindow)
    element.click()
    sleep(0.5)
    for handle in wb.window_handles:
        wb.switch_to_window(handle)
        if '晋江文学城' in handle:
            break
        

    tag = wb.find_elements_by_xpath(
        '//div[@class="smallreadbody"]//span/a')  # 获取作品的标签信息
    with open(filename, 'a', encoding='utf-8') as f_n:
        for t in tag:
            file_t = t.text
            f_n.write(file_t)
        f_n.write('\n')
        wb.close()

    # tag = wb.find_elements_by_xpath('//meta[@name="Keywords"]')  # 获取排行作品的全部信息
    # with open(filename,'a',encoding='utf-8') as f_n:
    #     for t in tag:
    #         file_t = t.get_attribute('content')
    #         f_n.write(file_t + '\n' + '\n')
    #     wb.close()
