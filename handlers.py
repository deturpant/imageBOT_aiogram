from main import bot, dp

from aiogram import types
from config import MY_ID
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
import markups as nav
import sqlite3
import re







async def send_to_admin(dp):
    await bot.send_message(chat_id=MY_ID, text="Bot is started")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!\nЭтот бот позволит тебе получить доступ к веб-архиву\nВыбери раздел!', reply_markup= nav.mainMenu)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды: '),
               '/photo''\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(Text(equals='Главное меню'))
async def process_go_to_main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы успешно вернулись в главное меню.', reply_markup=nav.mainMenu)

@dp.message_handler(Text(equals='Раздел Фото'))
async def process_photo_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Отлично! Выбери нужный раздел.\nПри необходимости вернись в главное меню.", reply_markup=nav.BackToMainMenuFromPhoto)

@dp.message_handler(Text(equals='Другое'))
async def process_drugoe_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы перешли в раздел другое!', reply_markup=nav.Drugoe)

@dp.message_handler(Text(equals='Личные фотографии'))
async def process_authorization(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для доступа к фотографиям введите пароль:', reply_markup=nav.Authorization_Photo)
@dp.message_handler(Text(equals='260693'))
async def process_succes(message:types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id,'Авторизация прошла успешно.\nВыбирай нужный раздел.', reply_markup=nav.Suc_Ph)


@dp.message_handler(Text(equals='Что такое пароль?!'))
async def process_whatfuck(message: types.Message):
    await bot.send_message(message.from_user.id, 'Тебе не сюда! Возвращайся обратно',reply_markup=nav.BackToMainMenu)


@dp.message_handler(Text(equals='Показать все фотографии'))
async def process_group_command(message: types.Message):
    con = sqlite3.connect('pic.db')
    cur = con.cursor()
    query = 'SELECT * FROM Media'
    cur.execute(query)
    data = cur.fetchall()
    mm = []
    for i in data:
        mm.append(i)
    ww = len(data)
    idph = []
    for z in range(0, ww):
        idph.append(data[z][1])
    media = []
    idph2 = idph
    idphh = []
    if len(idph2) > 10:
        await bot.send_message(message.from_user.id, 'Найдено более 10 фотографий. Лови!')
    while len(idph2) > 10:
        media = []
        idphh = idph2[0:10]
        for photo_id in idphh:
            media.append(InputMediaPhoto(photo_id))
        await bot.send_media_group(message.from_user.id, media)
        del idph2[0:10]
    if len(idph2) <= 10:
        media = []
        for photo_id in idph2:
            media.append(InputMediaPhoto(photo_id))
        await bot.send_media_group(message.from_user.id, media)



@dp.message_handler(Text(equals='Последние 10 загруженных фото'))
async def last_10_photo_command(message: types.Message):
    con = sqlite3.connect('pic.db')
    cur = con.cursor()
    query = 'SELECT * FROM Media'
    cur.execute(query)
    data = cur.fetchall()
    mm = []
    for i in data:
        mm.append(i)
    ww = len(data)
    idph = []
    for z in range(0, ww):
        idph.append(data[z][1])
    media = []
    idph2 = idph[-10:]
    idphh = []
    if len(idph2) == 10:
        await bot.send_message(message.from_user.id, 'Последние 10 фото уже у тебя :)')
    if len(idph2) == 10:
        media = []
        for photo_id in idph2:
            media.append(InputMediaPhoto(photo_id))
        await bot.send_media_group(message.from_user.id, media)



@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что ты можешь вернуться в главное меню')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=nav.BackToMainMenu)