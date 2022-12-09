import requests
from bs4 import BeautifulSoup
import gspread
import symbolSpam
import wordsAmount
import time

conn = gspread.service_account('C:\\Users\\User\\Desktop\\system\\alina\\ChatExport_M\\alina-368013-2b53c4cdae8d.json')

sh = conn.open('alina')

wks = sh.worksheet("Чат маг")

last_cell = 1
info = []
info2 = []

for el in range (11):
    html_text = ''
    if el == 0:
        el = ''
    if el == 1:
        pass
    else:
        file_check = open(f"messages{el}.html","r",encoding='utf-8')
        lines = file_check.readlines()
        file_check.close()

    for line in lines:
        html_text = html_text + line

    # print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')

    # for link in soup("div", class_="text"):
    #     b = str(link.get_text()).replace(' ', '', 1)
    #     b = str(link.get_text()).replace('       ', '', 1)
    #     b = str(link.get_text()).replace('\n','', 1)
    #     # a = [b]
    #     # if not wordsAmount.wordsAmount(b) and not symbolSpam.symbolSpam(b):
    #     info.append(b)

    # for link in soup("div", class_="from_name"):
    #     c = str(link.get_text()).replace(' ', '')
    #     c = c.replace('\n','')
    #     c = c.replace('        ', '')
    #     print(c)
    #     info2.append(c)

    # print(el)
    # print(soup.find_all('div', "from_name"))
    # print(len(info2))
    # print(len(info))
    flag = 0
    for link in soup.findAll(True, {'class':['from_name', 'text']}):
        if str(link["class"][0]) == 'from_name':
            c = str(link.get_text())
            c = c.replace('       ', '')
            c = c.replace('        ', '')
            c = c.replace('\n','')
            if c == 'Магистратура и Аспирантура Финунивера ' or c == 'Служба поддержки Финунивер' or c[:15] == 'Вестник приёмки':
                flag = 1
                pass
            else:
                flag = 0
                pass
        if flag == 1 and str(link["class"][0]) != 'from_name':
            pass
        elif flag == 0 and str(link["class"][0]) != 'from_name':
            b = str(link.get_text()) 
            b = b.replace('       ', '')
            b = b.replace('        ', '')
            b = b.replace('\n','')
            if not wordsAmount.wordsAmount(b) and not symbolSpam.symbolSpam(b) and not [b] in info:
                info.append([b])
        # if flag == 1 and not link["class"] == 'from_name':
        #     pass
        # elif flag == 0 and not link["class"] == 'from_name':
        #     b = str(link.get_text()).replace(' ', '',1)
        #     b = b.replace('       ', '')
        #     b = b.replace('        ', '')
        #     b = b.replace('\n','')
        #     info.append([b])
        # elif flag == 0 and link["class"] == 'from_name':
        #     c = str(link.get_text()).replace(' ', '',1)
        #     c = c.replace('       ', '')
        #     c = c.replace('        ', '')
        #     c = c.replace('\n','')
        #     if c == "Магистратураи Аспирантура Финунивера ":
        #         flag = 1
        #         pass
        #     else:
        #         flag = 0
        #         pass
    # last_cell = len(wks.col_values(1)) + 1
    print(el)

# print(len(info))
wks.update(f'A{last_cell}:A{len(info)}', info)

# # print(wks.row_count, wks.col_count)
# print(wks.acell('A1').value)
# print(wks.acell('A20').value)
# print(wks.cell(1, 1).value)
# print(wks.get('A1:A9'))
# print(wks.get('A1:A9'))