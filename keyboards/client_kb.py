from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #, ReplyKeyboardRemove


button1 = KeyboardButton('/Режим работы')
button2 = KeyboardButton('/Расположение')
button3 = KeyboardButton('/Меню')
button4 = KeyboardButton('Поделиться номером', request_contact=True)
button5 = KeyboardButton('Отправить где я', request_location=True)

keboard_client = ReplyKeyboardMarkup(resize_keyboard=True)

keboard_client.add(button1).row(button2, button3).row(button4, button5)
