from threading import Thread
import gspread
import time

bannedUsersChatId = []
bannedUsersId = []
bannedUsersTime = []

def add(sheetName, newData, range):

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
    file = conn.open('alina')

    ws = file.worksheet(sheetName)
    spamExamples = ws.col_values(range)

    for i in newData:
        if i in spamExamples:
            newData.remove(i)

    data = [[element] for element in (newData + spamExamples)]
    ws.update(f'A1:A{len(data)}', data)


def addChat(title, newData, range):

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')
    file = conn.open('alina')

    if title == 'Бакалавриат Финунивера':
        sheetName = 'Чат бак'
    elif title == 'На уровень выше 🎓':
        sheetName = 'Чат маг'
    # elif title == 'Тестим Алину':
    #     sheetName = 'Лист8'

    # print(title)

    ws = file.worksheet(sheetName)
    Chat = ws.col_values(range)

    data = [[element] for element in (newData)]
    ws.update(f'A{len(Chat) + 1}:A{len(Chat) + len(data) + 1}', data)


def addBannedUser(chatId, userId, userName, userSurname, userNickname, time, sheetName):

    global bannedUsersChatId
    global bannedUsersId
    global bannedUsersTime

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')

    file = conn.open('alina')

    ws = file.worksheet(sheetName)
    UsersChatIdExcel = ws.col_values(1)
    UsersIdExcel = ws.col_values(2)
    UsersTimeExcel = ws.col_values(6)

    ws.update(f'A{len(UsersIdExcel) + 1}:G{len(UsersIdExcel) + 1}', [[chatId, userId, userName, userSurname, userNickname, time.split('.')[0]]])

    UsersChatIdExcel.append(chatId)
    UsersIdExcel.append(userId)

    bannedUsersChatId = UsersChatIdExcel
    bannedUsersId = UsersIdExcel
    bannedUsersTime = UsersTimeExcel

def th_getBannedUsers(sheetName, freq=900):
    global bannedUsersChatId
    global bannedUsersId
    global bannedUsersTime

    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')

    file = conn.open('alina')

    ws = file.worksheet(sheetName)
    UsersChatIdExcel = ws.col_values(1)
    UsersIdExcel = ws.col_values(2)
    UsersTimeExcel = ws.col_values(6)

    bannedUsersChatId = UsersChatIdExcel
    bannedUsersId = UsersIdExcel
    bannedUsersTime = UsersTimeExcel

    conn.session.close()

    time.sleep(freq)
    
    getBannedUsers(sheetName, freq)


def getBannedUsers(sheetName, freq=900):
    th = Thread(target=th_getBannedUsers, args=(sheetName, freq))
    th.start()


def getBannedUsersNow(sheetName):
    conn = gspread.service_account('./alina-368013-2b53c4cdae8d.json')

    file = conn.open('alina')

    ws = file.worksheet(sheetName)
    bannedUsersId = ws.col_values(2)

    return bannedUsersId