import telebot
import random

bot = telebot.TeleBot('6457055794:AAHObLLgjZRVy7jUB3e_I0LFYa_yZNFA9zU')


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, f"<b>Привет</b> {message.from_user.first_name}<b>!</b>", parse_mode='html')

@bot.message_handler(commands='ball'])
def ball(message):
  bot.send_message(message.chat.id, f"<b>Задай мне вопрос.</b>", parse_mode='html')

@bot.message_handler(content_types=['text'])
def question(message):
