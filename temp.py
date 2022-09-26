import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import types

bot = AsyncTeleBot('5688753458:AAGad2R0DnWu1fla0zXTIfFERcF6e7FnTFg')

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """каламбетус""")


@bot.message_handler(commands=['button'])
async def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Открывается дверь...', callback_data='question_1')
    item2 = types.InlineKeyboardButton('пока', callback_data='goodbye')
    markup.add(item, item2)

    await bot.send_message(message.chat.id, 'привет', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
async def callback(call):
    if call.message:
        if call.data == 'question_1':
            await bot.send_message(call.message.chat.id, 'ставится каламбет')
        if call.data == 'goodbye':
            await bot.send_message(call.message.chat.id, 'пока кожанный ублюдок!')
asyncio.run(bot.polling())