from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
btnMain = KeyboardButton("Главное меню")

btnPhoto = KeyboardButton('Раздел Фото')
btnOther = KeyboardButton("Другое")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPhoto, btnOther)


btnHelp = KeyboardButton("Помощь")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHelp, btnMain)

btnPh = KeyboardButton('Личные фотографии')
BackToMainMenuFromPhoto = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPh, btnMain)

Drugoe = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHelp, btnMain)

Pass = KeyboardButton('Что такое пароль?!')
Authorization_Photo = ReplyKeyboardMarkup(resize_keyboard=True).add(Pass, btnMain)

BackToMainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)


btnAllPh = KeyboardButton("Показать все фотографии")
btnLastPh = KeyboardButton("Последние 10 загруженных фото")
Suc_Ph = ReplyKeyboardMarkup(resize_keyboard=True).add(btnLastPh, btnAllPh, btnMain)