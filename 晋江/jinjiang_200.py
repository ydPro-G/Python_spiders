from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


wb = webdriver.Chrome()

wb.get('http://www.jjwxc.net/topten.php?orderstr=5&t=0')
elements = wb.find_elements_by_xpath('//table[3]//tbody//tr//td//a[@class]')
mainWindow = wb.current_window_handle
filename = 'article.txt'

for element in elements:
    wb.switch_to_window(mainWindow)
    element.send_keys(Keys.ENTER)
    sleep(0.01)
    for handle in wb.window_handles:
        wb.switch_to_window(handle)
        if '晋江文学城' in handle:
            break

    tag = wb.find_elements_by_xpath('//div[@class="smallreadbody"]//span/a')  # 获取作品的标签信息
    with open(filename, 'a', encoding='utf-8') as f_n:
        for t in tag:
            file_t = t.text
            f_n.write(file_t)
        f_n.write('\n')
        wb.close()
