from threading import Thread
import time
import gspread

badWords = []
spamExamples = []

def th_update(name, sheetName, range, freq):

    global badWords
    global spamExamples

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')

    file = conn.open('alina')
    ws = file.worksheet(sheetName)

    if name == 'badWords':
        badWords = ws.col_values(range)
    elif name == 'spamExamples':
        spamExamples = ws.col_values(range)

    conn.session.close()

    time.sleep(freq)
    
    th_update(name, sheetName, range, freq)


def update(name, sheetName, range, freq=900):
    th = Thread(target=th_update, args=(name, sheetName, range, freq))
    th.start()

def bootUpdate(name, sheetName, range):
    time.sleep(10)
    global badWords
    global spamExamples

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')

    file = conn.open('alina')
    ws = file.worksheet(sheetName)

    if name == 'badWords':
        badWords = ws.col_values(range)
    elif name == 'spamExamples':
        spamExamples = ws.col_values(range)

    conn.session.close()