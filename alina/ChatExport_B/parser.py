import requests
from bs4 import BeautifulSoup
import gspread
import symbolSpam
import wordsAmount
import time

conn = gspread.service_account('C:\\Users\\User\\Desktop\\system\\alina\\ChatExport_B\\alina-368013-2b53c4cdae8d.json')

sh = conn.open('alina')

wks = sh.worksheet("Чат бак")

last_cell = 1
info = []

for el in range (53):
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

    for link in soup("div", class_="text"):
        b = str(link.get_text()).replace(' ', '', 1)
        b = str(link.get_text()).replace('       ', '', 1)
        b = str(link.get_text()).replace('\n','', 1)
        a = [b]
        if not wordsAmount.wordsAmount(b) and not symbolSpam.symbolSpam(b):
            info.append(a)


    print(el)
    # last_cell = len(wks.col_values(1)) + 1

wks.update(f'A{last_cell}:A{len(info)}', info)
