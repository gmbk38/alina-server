import gspread
import random

def getAdmin(sheetname, cell):
    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
    file = conn.open('alina')
    ws = file.worksheet(sheetname)

    if ws.acell(cell).value != None and ws.acell(cell).value[:13] != 'Авторизуйтесь':
        conn.session.close()
        return int(ws.acell(cell).value), None
    else:
        letters = 'alina'
        command = ''.join([random.choice(letters) for i in range (8)])
        ws.update(cell, f'Авторизуйтесь с помощью /{command}')

        conn.session.close()
        return None, command


def getAdminParameters(sheetname, range):
    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
    file = conn.open('alina')
    ws = file.worksheet(sheetname)

    data = ws.row_values(range)
    BanTime = int(data[2])
    ChatAmount = int(data[3])
    SpamAmount = int(data[4])
    UpdateTime = int(data[5])

    conn.session.close()
    return BanTime, ChatAmount, SpamAmount, UpdateTime


def writeAdmin(sheetname, range, adminId, adminFirstName, adminLastName, adminNickName):
    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
    file = conn.open('alina')

    ws = file.worksheet(sheetname)
    ws.update(range, [[adminId], [adminFirstName], [adminLastName], [adminNickName]])

    conn.session.close()
    return True


# def writeAdmin(sheetname, cell, adminId):
#     conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
#     file = conn.open('alina')

#     ws = file.worksheet(sheetname)
#     ws.update(cell, adminId)

#     conn.session.close()
#     return True