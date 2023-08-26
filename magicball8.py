import telebot
import random

bot = telebot.TeleBot('6457055794:AAHObLLgjZRVy7jUB3e_I0LFYa_yZNFA9zU')


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, f"<b>Привет</b> {message.from_user.first_name}<b>!</b>\n<b>Для начала работы напиши</b> /ball", parse_mode='html')

@bot.message_handler(commands='ball'])
def ball(message):
  bot.send_message(message.chat.id, f"<b>Задай мне вопрос.</b>", parse_mode='html')

@bot.message_handler(content_types=['text'])
def question(message):
  answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - «да»", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - «да»", "Да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не расссказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - «нет»", "По моим данным - «нет»", "Перспективы не очень хорошие", "Весьма сомнительно"]
  question1 = message.text
  bot.reply_to(message,
    f'<b>Твой вопрос:</b> "{question1}"\n\n'
    f'<b>Мой ответ:</b> {random.choice(answer)}',
    parse_mode='html'
    )

bot.infinity_polling()
