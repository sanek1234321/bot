import telebot

import argparse
parser = argparse.ArgumentParser()

import requests

parser.add_argument("token", help = "token234567")
args = parser.parse_args()

bot = telebot.TeleBot(args.token)

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
@bot.message_handler(commands=['get'])
def start_message(message):
    bot.send_message(message.chat.id, data['Valute']['USD']['Value'])

bot.polling()
