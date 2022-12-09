from threading import Thread
import time
import gspread

# conn = gspread.service_account('C:\\Users\\User\\Desktop\\system\\alina\\alina-368013-2b53c4cdae8d.json')
conn = gspread.service_account('alina/alina-368013-2b53c4cdae8d.json')

sh = conn.open('alina')

wks = sh.worksheet("Лист1")

root = 0

def part(root):
    return root

def wait():
    global root 
    
    root = wks.col_values(1)
    time.sleep(10)
    wait()

def starter():
    th = Thread(target=wait, args=( ))
    th.start()