import telebot
import secret
import admin
from cases import Case
from users import User
from roles import Roles


bot = telebot.TeleBot(secret.token)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Приветствую, представься пожалуйста!')
    bot.register_next_step_handler(msg, 'a')


@bot.message_handler()
def handle_message(message: telebot.types.Message):
    if message.text == 'a':
        admin.main(message.chat.id)


@bot.callback_query_handler()
def call_handler(callback: telebot.types.CallbackQuery):
    if callback.data.startswith('a_'):
        admin.take_call(callback.data[callback.data.index('_') + 1:], str(callback.from_user.id))


# Место для register_next_step_handler


def registerNewInSettings(msg, which):
    bot.register_next_step_handler(msg, admin.make_new, which)


def main():
    print('Запуск приема сообщений')
    bot.infinity_polling()