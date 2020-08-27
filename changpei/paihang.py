from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

wb = webdriver.Chrome()

wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=3')
all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')
s = len(all)
filename = 'changpei.txt'
for i in range(s):
    all[i].click() # 获取列表元素的索引，元素索引从0开始依次点击
    wb.back()
    sleep(1)
    all = wb.find_elements_by_xpath('//a[@class="cp-novel-name"]')

    for handle in wb.window_handles:
        wb.switch_to_window(handle)
        if '长佩文学网' in handle:
            break

    tag = wb.find_elements_by_xpath(
        '//div[@class="customTags"]//span')  # 获取作品的标签信息
    with open(filename, 'a', encoding='utf-8') as f_n:
        for t in tag:
            file_t = t.text
            f_n.write(file_t)
        f_n.write('\n')
