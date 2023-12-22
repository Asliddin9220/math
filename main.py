import telebot
import requests
import random
from telebot import types
bot = telebot.TeleBot('6763167572:AAF5kFLBLtd-Gonl_TeEiyslKSkhDrVQnTk')
@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✖ ko'paytirish")
    btn2 = types.KeyboardButton("➗bo'lish")
    btn3 = types.KeyboardButton("➕qo'shish")
    btn4 = types.KeyboardButton("➖ayirish")
    markup.add(btn1, btn2,btn3,btn4)
    bot.send_message(message.chat.id,"salom!rejimni tanlang".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "✖ko'paytirish":
        a=random.randint(1,10)
        b=random.randint(1,10)
        bot.send_message(message.chat.id,str(a) + "x" + str(b) + "=" )
        if message.text == str(a*b):
         bot.send_message(message.chat.id, "barakalla! to'g'ri!")
def get_text_messages(message):
    if message.text == "✖bo'lish":
        a=random.randint(1,10)
        b=random.randint(1,10)
        bot.send_message(message.chat.id,str(a) + "/" + str(b) + "=" )
        if message.text == str(a/b):
         bot.send_message(message.chat.id, "barakalla! to'g'ri!")         
def get_text_messages(message):
    if message.text == "✖qo'shish":
        a=random.randint(1,10)
        b=random.randint(1,10)
        bot.send_message(message.chat.id,str(a) + "+" + str(b) + "=" )
        if message.text == str(a+b):
         bot.send_message(message.chat.id, "barakalla! to'g'ri!")
def get_text_messages(message):
    if message.text == "✖ayirish":
        a=random.randint(1,10)
        b=random.randint(1,10)
        bot.send_message(message.chat.id,str(a) + "-" + str(b) + "=" )
        if message.text == str(a-b):
         bot.send_message(message.chat.id, "barakalla! to'g'ri!")

bot.polling(none_stop=True, interval=0)