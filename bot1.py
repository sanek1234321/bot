import telebot
import time
import argparse
parser = argparse.ArgumentParser()

import requests

parser.add_argument("token", help = "token")
args = parser.parse_args()

bot = telebot.TeleBot(args.token)

@bot.message_handler(commands=['get'])
def start_message(message):
    bot.send_message(message.chat.id, 'напиши название валюты (USD,EUR...)')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, data['Valute'][message.text]['Value'])

bot.polling()

i=1
while i==1:
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    time.sleep(3600)
