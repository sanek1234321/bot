import telebot

import requests

bot = telebot.TeleBot('5177078876:AAFKp_WSaFclvIhNdSqbSND6xIectqd5jF0')

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
@bot.message_handler(commands=['get'])
def start_message(message):
    bot.send_message(message.chat.id, data['Valute']['USD']['Value'])

bot.polling()
