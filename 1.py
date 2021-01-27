from selenium import webdriver

wb = webdriver.Chrome()

url = wb.get("https://www.cdcxhl.com/news/16350.html")

elements = wb.find_elements_by_xpath('//div[@class="col-lg-8 col-md-11 col-sm-11 col-xs-11 bkleft"]')

for element in elements:
    print(element.text)