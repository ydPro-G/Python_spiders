import requests
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
 
def getHtmlText(url):
    try:
        kv = {'cookie': 'miid=392564041795602273; thw=cn; cna=BB3mFylX8TYCATzVDJqsTiGS; hng=CN%7Czh-CN%7CCNY%7C156; _gcl_aw=GCL.1604478710.EAIaIQobChMIvbu--Lzo7AIVmayWCh1Iewk5EAAYASAAEgKHXPD_BwE; _fbp=fb.1.1604478710445.1264933848; xlly_s=1; _m_h5_tk=68d408057c6ca061d89187424e9dd9eb_1610016792420; _m_h5_tk_enc=407a6b6fe5e9d07627613a6ed795377a; t=87bc119cfdca93b8c46438dae8e030f6; v=0; _tb_token_=eb67a34ee9ede; _samesite_flag_=true; cookie2=12fe83f5d0642c5c94e4fa48f4d9c2ff; sgcookie=E100NK%2FoUpD0rTfr9rDGem7JxgYL2zF6EHGiP%2FPn2cxDHyflkj%2BOrHZaxhVPvKElM1RmNBrgmeyHAlHFceSC%2Fku3Hw%3D%3D; unb=2782205861; uc3=vt3=F8dCuAAj2wldpkOneRQ%3D&nk2=2lP%2BQ4yJM6ab&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UU8A5Ay8ZLEWRg%3D%3D; csg=ff982dee; lgc=%5Cu7BA1%5Cu5B66%5Cu6D9Bgxt; cookie17=UU8A5Ay8ZLEWRg%3D%3D; dnk=%5Cu7BA1%5Cu5B66%5Cu6D9Bgxt; skt=4ca0673f7813d45e; existShop=MTYxMDAwOTY3Mg%3D%3D; uc4=nk4=0%402GkaTmdPpSca0RcSkzszhyR0vfo%3D&id4=0%40U22HuZKO11uQv9ZgDTJFfWNLuYUx; tracknick=%5Cu7BA1%5Cu5B66%5Cu6D9Bgxt; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=t19; _nk_=%5Cu7BA1%5Cu5B66%5Cu6D9Bgxt; cookie1=BxpT7G91ekMAwRkz%2B8B1mcDUr%2BeBVG8EdeEz7q5N%2BZc%3D; mt=ci=64_1; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&cookie14=Uoe1gqgjUmaedw%3D%3D&pas=0; l=eBEyO_qrO-3OusOKBOfwourza77OSIRAguPzaNbMiOCPOD5B5wkNWZ8rSJ86C3GVhs1XR3uKcXmQBeYBqQd-nxvtIosM_Ckmn; tfstk=cDBNBm0t6ReNJtJbwd9qG8LZROSOZusGmv-WssakAhh-5FRGiVuvxlfkYnT8KCf..; isg=BNvb6OEIAJQUIXy0273x911vaj9FsO-yqNlfbM0Yt1rxrPuOVYB_AvkqRgwijEeq'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "111"
 
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("222")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    """
    #创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0 ,"序号")
    worksheet.write(0, 1 ,"价格")
    worksheet.write(0, 2 ,"商品价格")"""
    wb = Workbook() #创建Workbook，并默认会创建一个空表，名称为sheet
    ws1 = wb.active #获取默认的sheet
    ws1.title = 'Sheet1'
    #写入单个单元格
    ws1['A1']='序号'
    ws1['B1']='价格'
    ws1['C1']='商品名称'
    print(tplt.format("序号","价格","商品名称"))
    count = 0 
    for g in ilt:
        count = count + 1
        """
        worksheet.write(count, 0 ,count)
        worksheet.write(count, 1 ,g[0])
        worksheet.write(count, 2 ,g[1])"""
        ws1.append([count,g[0],g[1]])
        print(tplt.format(count,g[0],g[1]))
    #workbook.save('D:\codeProgramFiles\CodeSpace\Excel_test.xls')    
    wb.save('D:\codeProgramFiles\CodeSpace\Excel_test.xlsx')
 
def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
 
main()