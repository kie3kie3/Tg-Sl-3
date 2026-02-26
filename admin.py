import telebot
import secret
import handler

from cases import Case
from users import User
from roles import Roles


bot = telebot.TeleBot(secret.token)


def make_new(message: telebot.types.Message, which: str):
    if which == 'role':
        obj = Roles(message.text)
    elif which == 'case':
        obj = Case(message.text)
    obj.write()
    bot.send_message(
        message.from_user.id,
        'Хорошо, я создал. Теперь можешь отредактировать, кнопки ниже.'
    )


def new(which: str, id):
    msg = bot.send_message(id, 'Хорошо, теперь введи название')
    handler.registerNewInSettings(msg, which)


def show_new(id):
    markup = telebot.types.InlineKeyboardMarkup()
    roles = telebot.types.InlineKeyboardButton(
        text='Новая роль',
        callback_data='a_new!role'
    )
    case = telebot.types.InlineKeyboardButton(
        text='Новая ситуация(приход, чеклист и проч)',
        callback_data='a_new!case'
    )
    markup.add(roles)
    markup.add(case)
    bot.send_message(
        id,
        'Выбери, что созадть:',
        reply_markup=markup
    )


def settings(id):
    markup = telebot.types.InlineKeyboardMarkup()
    new = telebot.types.InlineKeyboardButton(
        'Создать новое',
        callback_data='a_new'
    )
    edit = telebot.types.InlineKeyboardButton(
        'Редактировать имеющееся',
        callback_data='a_e'
    )
    markup.add(new)
    markup.add(edit)
    bot.send_message(
        id, 
        'Выбирай:',
        reply_markup=markup
    )


def show_edit(id):
    markup = telebot.types.InlineKeyboardMarkup()
    role = telebot.types.InlineKeyboardButton(
        'Редкатировать роль',
        callback_data='a_er'
    )
    case = telebot.types.InlineKeyboardButton(
        'Редактировать ситуации',
        callback_data='a_ec'
    )
    markup.add(role)
    markup.add(case)
    bot.send_message(
        id,
        'Что будем редактировать?',
        reply_markup=markup
    )


def edit(id, call: str):
    if call.startswith('r'):
        Roles.edit(id, call[1:])
    elif call.startswith('c'):
        Case.edit(id, call[1:])
    elif call.startswith('u'):
        User.edit(id, call[1:])


def take_call(call: str, id: str):
    if call.startswith('new!'):
        new(call[call.index('!') + 1:], id)
    elif call == 'new':
        show_new(id)
    elif call == 'set':
        settings(id)
    elif call == 'e':
        show_edit(id)
    elif call.startswith('e'):
        edit(id, call[call.index('e') + 1:])


def main(id):
    markup = telebot.types.InlineKeyboardMarkup()
    settings = telebot.types.InlineKeyboardButton(
        'Настройки(роли, приходы и проч)',
        callback_data='a_set'
    )
    users = telebot.types.InlineKeyboardButton(
        'Поменять в пользователях',
        callback_data='a_eu'
    )
    markup.add(settings)
    markup.add(users)
    bot.send_message(
        id,
        'Выбери, что хочешь поменять:',
        reply_markup=markup
    )