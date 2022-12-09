import logging
import banHammer
import update
from admin import getAdmin, getAdminParameters, writeAdmin
from keyboards import spamkb
import add
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '5276719164:AAEtAt33tVLBf2DWBHTnIPlAFvbf4KVMang'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

adminId, command = getAdmin('Админ', 'B4')
BanTime, ChatAmount, SpamAmount, UpdateTime = getAdminParameters('Админ', 4)
# print(BanTime, ChatAmount, SpamAmount, UpdateTime)
spamData = {}
spamUserInfo = {}
# в spamData фиксируем связку {message.message_id : message.text}
spamAdditive = []
# spamAdditive хранит в себе 20 сообщений, после чего выгружает их
isSpam = []
myChat = []

update.bootUpdate('badWords', 'Запрещённые слова', 1)
update.bootUpdate('spamExamples', 'Примеры спама', 1)

update.update('badWords', 'Запрещённые слова', 1, UpdateTime)
update.update('spamExamples', 'Примеры спама', 1, UpdateTime)
add.getBannedUsers('Banned users')

if adminId == None:
    @dp.message_handler(commands=[command])
    async def botGetAdmin(message: types.Message):
        
        global adminId

        adminId = message.from_user.id
        writeAdmin('Админ', 'B4:B7', adminId, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
        await bot.send_message(adminId, 'Вы авторизировались')


@dp.message_handler(commands=['unban'])
async def botUnban(message: types.Message):

    # len(message.split())

    wasBanned = add.bannedUsersId
    isBanned = add.getBannedUsersNow('Banned users')

    toUnban = []

    for el in isBanned:
        if el in wasBanned:
            wasBanned.remove(el)

    toUnban = wasBanned

    # for value in add.bannedUsersId:
    #     if value not in isBanned:
    #         toUnban.append(value)

    # print(toUnban)

    for element in toUnban:
        try:
            chatId = add.bannedUsersChatId[add.bannedUsersId.index(element)]
            await bot.restrict_chat_member(chatId, element, types.ChatPermissions(can_send_messages=True))
        except Exception as ex:
            pass

    await bot.send_message(adminId, 'Пользователи разбанены')


@dp.message_handler(content_types=['text'])
async def botAnswer(message: types.Message):

    global adminId
    global spamData
    global spamUserInfo
    global isSpam
    global myChat

    if banHammer.banHammer(message.text ,update.badWords, 0.95):
        await message.delete()
        await message.answer(f"Уважаемы участники, напоминаем вам о правилах общения в чате:\nИспользовать ненормативную лексику нельзя")
    
    elif banHammer.spamHammer(message.text, update.spamExamples):
        spamData[message.message_id] = message.text
        spamUserInfo[message.message_id] = [message.from_user.first_name, message.from_user.last_name, message.from_user.username]
        isSpam.append(message.text)
        try:
            await bot.send_message(adminId, message.text, reply_markup=spamkb(message.chat.id, message.message_id, message.from_user.id))
        except Exception as ex:
            pass
    else:
        isSpam.append(message.text)
        # Структура банит за спам подряд
        if len([msg for msg in isSpam if msg == message.text]) > 2:
            await bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(can_send_messages=False), until_date=datetime.now() + timedelta(minutes=BanTime))
            await message.delete()
            # if not message.from_user.id in add.bannedUsersId:
            add.addBannedUser(message.chat.id, message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, str(datetime.now() + timedelta(minutes=BanTime)), 'Banned users')
        # await bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(can_send_messages=False), until_date=datetime.now() + timedelta(minutes=BanTime))
        # bannedUsersChatId, bannedUsersId = add.addBannedUser(message.chat.id, message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text, 'Banned users')
        # await message.answer(f"Ок") 
        if len(isSpam) >= 10:
            isSpam = []
        pass   
        if len(myChat) >= ChatAmount:
            add.addChat(message.chat.title, myChat, 1)
            myChat = []
        else:
            myChat.append(message.text)



@dp.callback_query_handler()
async def callback_handler(query: types.CallbackQuery):

    global spamAdditive
    global adminId
    global spamData
    global spamUserInfo
    global bannedUsersChatId

    data = query.data.split('_')
    if int(data[0]) == 0:
        # query.message.edit_text(reply_markup=None)
        await query.message.delete()
        spamData.pop(int(data[2]), None)
    else:
        await query.message.delete()
        try:
            # add('Примеры спама', data, 1)
            await bot.restrict_chat_member(int(data[1]), int(data[3]), types.ChatPermissions(can_send_messages=False), until_date=datetime.now() + timedelta(minutes=BanTime))
            await bot.delete_message(int(data[1]), int(data[2]))
            data3 = spamUserInfo.pop(int(data[2]), None)
            add.addBannedUser(int(data[1]), int(data[3]), data3[0], data3[1], data3[2], datetime.now() + timedelta(minutes=BanTime), 'Banned users')
        except Exception as ex:
            pass
        finally:
            msg = spamData.pop(int(data[2]), None)
            spamAdditive.append(msg)
            # ВАЖНО! 20 - количество сообщений, необходимое для запроса на выгрузку 
            if len(spamAdditive) >= SpamAmount:
                add.add('Примеры спама', spamAdditive, 1)
                spamAdditive = []
            # await bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(can_send_messages=False), until_date=datetime.now() + timedelta(minutes=BanTime))
            # bannedUsersChatId, bannedUsersId = add.addBannedUser(message.chat.id, message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text, 'Banned users')

        # await bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(can_send_messages=False), until_date=datetime.now() + timedelta(minutes=30))
        # Добавляем в примеры спама

executor.start_polling(dp, skip_updates=True)
