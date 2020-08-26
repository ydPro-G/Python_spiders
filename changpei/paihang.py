from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

wb = webdriver.Chrome()

wb.get('https://www.gongzicp.com/home/ranking?tid=75&id=1&rankList=2&date=3')
tag = len(wb.find_elements_by_xpath(
    '//div[@class="cp-novel-list"]//a[@class="cp-novel-name"]'))
filename = 'cp.txt'

for i in range(tag):
    wb.find_element_by_xpath('//div[@class="cp-novel-list"]//div[@class="right"]//div[@class="cp-over-hidden"]//a[i+1]').click()
    sleep(0.1)
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
    wb.back()
    sleep(5)
