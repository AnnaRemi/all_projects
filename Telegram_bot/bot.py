import requests
import telebot
from multiprocessing import Process
import datetime
import time
from telebot import types
from database import Database
from constant import *


class Bot(object):
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.db = Database()

        @self.bot.message_handler(content_types=['sticker'])
        def sticker(message):
            self.bot.send_message(message.from_user.id, "Буквами пиши, они бесплатные")

        @self.bot.message_handler(content_types=['voice'])
        def voice(message):
            self.bot.send_message(message.from_user.id, "Голосовухи это сложно, сорян")

        @self.bot.message_handler(content_types=['game'])
        def game(self, message):
            self.bot.send_message(message.from_user.id, "Давай не")

        @self.bot.message_handler(content_types=['video_note'])
        def video_note(message):
            self.bot.send_message(message.from_user.id, "Огонб, но давай к теме разговора")

        @self.bot.message_handler(content_types=['venue'])
        def venue(message):
            self.bot.send_message(message.from_user.id, "О, там клево")

        @self.bot.message_handler(content_types=['pinned_message'])
        def pinned_message(message):
            self.bot.send_message(message.from_user.id, "Я не понимаю((")

        @self.bot.message_handler(content_types=['audio'])
        def audio(message):
            self.bot.send_message(message.from_user.id, "О, моя любимая")

        @self.bot.message_handler(content_types=['document'])
        def document(message):
            self.bot.send_message(message.from_user.id, "фу убери")

        @self.bot.message_handler(content_types=['photo'])
        def photo(message):
            self.bot.send_message(message.from_user.id, "Огонб, но давай к теме разговора")

        @self.bot.message_handler(content_types=['video'])  # обработать все message
        def video(message):
            self.bot.send_message(message.from_user.id, "Посмотрю когда-нибудь потом")

        @self.bot.message_handler(content_types=['location'])
        def location(message):
            self.bot.send_message(message.from_user.id, "Чеее?")

        @self.bot.message_handler(content_types=['contact'])
        def contact(message):
            self.bot.send_message(message.from_user.id, "Понятно, что ниче не понятно")

        @self.bot.message_handler(commands=['start'])
        def info(message):
            keyboard = types.InlineKeyboardMarkup()
            key_reg = types.InlineKeyboardButton(text='Зарегистрироваться', callback_data='reg')
            keyboard.add(key_reg)
            self.bot.send_message(message.from_user.id, text='Привет, милашка)\nСкорее регистрируйся!',
                                  reply_markup=keyboard)

        @self.bot.message_handler(func=lambda message: message.text.lower() == 'список дел')
        def write_plans(message):
            plans = self.db.get_data(message.from_user.id, 'plans')
            if len(plans) == 0:
                self.bot.send_message(message.from_user.id, "Кажется, у тебя его еще нету((\n"
                                                            "Хочешь сделать сейчас?")
                self.bot.register_next_step_handler(message, self.answer)
            else:
                self.bot.send_message(message.from_user.id, '\n'.join(plans))

        @self.bot.message_handler(content_types=['text'])
        def start(message):
            if message.text.lower() == 'меню':
                keyboard = types.InlineKeyboardMarkup()
                key_talk = types.InlineKeyboardButton(text='Поболтать', callback_data='talk')
                keyboard.add(key_talk)
                key_plans = types.InlineKeyboardButton(text='Составить список дел', callback_data='plans')
                keyboard.add(key_plans)
                key_news = types.InlineKeyboardButton(text='Новости', callback_data='news')
                keyboard.add(key_news)
                key_hor_for_user = types.InlineKeyboardButton(text='Гороскоп для себя',
                                                              callback_data='hor_for_user')
                keyboard.add(key_hor_for_user)
                key_hor_not_for_user = types.InlineKeyboardButton(text='Гороскоп не для себя',
                                                                  callback_data='hor_not_for_user')
                keyboard.add(key_hor_not_for_user)
                self.bot.send_message(message.from_user.id, text='Что будем делать сегодня?',
                                      reply_markup=keyboard)
            else:
                self.bot.send_message(message.from_user.id, "Напиши 'меню', и я покажу тебе, что умею")

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == 'reg':
                self.reg(call.message, call.from_user.id)
            elif call.data == 'talk':
                self.bot.send_message(call.from_user.id, "Я бы с радостью, но чуть позже")
            elif call.data == 'plans':
                self.bot.send_message(call.from_user.id,
                                      "Работяга, какие планы на сегодня? Напиши 'все' в конце списка дел")
                self.bot.register_next_step_handler(call.message, self.get_plans)
            elif call.data == 'hor_for_user':
                self.check_have_zodiac(call.message, call.from_user.id, 'for_user')
            elif call.data == 'hor_not_for_user':
                self.check_have_zodiac(call.message, call.from_user.id, 'not_for_user')
            elif call.data == 'news':
                self.bot.send_message(call.from_user.id, self.get_news())

    def get_another_zodiac(self, message):
        if not isinstance(message.text, str):
            self.bot.send_message(message.from_user.id, "Пиши буквами, они бесплатные)")
            self.bot.register_next_step_handler(message, self.get_another_zodiac)
        elif message.text.lower() in const.HOROSCOPE.keys():
            self.bot.send_message(message.from_user.id, "Окей, погнали искать гороскоп)")
            self.bot.send_message(message.from_user.id, self.get_horoscope(message.text.lower()))
        else:
            self.bot.send_message(message.from_user.id, "Такого знака нет(\nПопробуй еще раз!")
            self.bot.register_next_step_handler(message, self.get_another_zodiac)

    def get_plans(self, message):
        if isinstance(message.text, str):
            if message.text.lower() == 'все':
                self.bot.send_message(message.from_user.id, "Отлично, работяга, удачного дня! "
                                                            "Ты всегда можешь посмотреть свой список дел,"
                                                            " просто написав мне 'список дел'. Для возврата к меню напиши 'меню'")
            else:
                self.db.update(message.from_user.id, 'plans', message.text)
                self.bot.send_message(message.from_user.id, "Что-то еще?")
                self.bot.register_next_step_handler(message, self.get_plans)
        else:
            self.bot.send_message(message.from_user.id, "Я тебя нЕ пОнИмАю, попробуй еще раз")
            self.bot.register_next_step_handler(message, self.get_plans)

    def get_time(self, message):
        if isinstance(message.text, str):
            data = message.text[0:2] + message.text[3:5]
            if data.isdigit() and int(data[0:2]) <= 24 and int(data[0:2]) >= 0 \
                    and int(data[2:4]) >= 0 and int(data[2:4]) < 60:
                self.db.update(message.from_user.id, 'time', str(datetime.time(int(data[0:2]), int(data[2:4]))))
                self.bot.send_message(message.from_user.id, "Ммм, а кто ты по гороскопу?")
                self.bot.register_next_step_handler(message, self.get_zodiac)
            else:
                self.bot.send_message(message.from_user.id, "Введи в правильном формате))")
                self.bot.register_next_step_handler(message, self.get_time)
        else:
            self.bot.send_message(message.from_user.id, "Попробуй еще раз)")
            self.bot.register_next_step_handler(message, self.get_time)

    def get_name(self, message):
        if isinstance(message.text, str):
            self.db.update(message.from_user.id, 'name', message.text)
            self.bot.send_message(message.from_user.id, "Класс) Сколько тебе лет?")
            self.bot.register_next_step_handler(message, self.get_age)
        else:
            self.bot.send_message(message.from_user.id, "Ааааа пиши буууквами")
            self.bot.register_next_step_handler(message, self.get_name)

    def reg_answer(self, message):
        if isinstance(message.text, str):
            if message.text.lower() == 'да':
                self.bot.send_message(message.from_user.id, "Хорошо, давай заново. Напиши мне свое имя")
                self.bot.register_next_step_handler(message, self.get_name)
        else:
            self.bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши 'да', если хочешь")
            self.bot.register_next_step_handler(message, self.get_name)

    def reg(self, message, user_id):
        if user_id in self.db.get_users_id():
            self.bot.send_message(user_id, "Ты ведь уже зарегистрирован!\n"
                                           "Хочешь сделать это заново?")
            self.bot.register_next_step_handler(message, self.reg_answer)
        else:
            self.bot.send_message(user_id, "Отлично, го знакомиться! Напиши мне свое имя")
            self.db.create_new_user(user_id)
            self.bot.register_next_step_handler(message, self.get_name)

    def get_news(self):
        html = requests.request(url='https://news.rambler.ru/world/', method='GET')
        news = {}  # tech -о науке
        begin_pos = 0
        begin = 'content="https://news.rambler.ru/world/'
        end = '"'
        while begin_pos != len(begin) - 1:
            begin_pos = html.text.find(begin, begin_pos) + len(begin)
            if begin_pos >= len(begin):
                end_pos = html.text.find(end, begin_pos)
                one_new = html.text[begin_pos:end_pos]
                if one_new.find('comments/') == -1 and one_new != '':
                    head_begin = 'title">'
                    head_end = '<'
                    head_begin_pos = html.text[begin_pos:].find(head_begin) + len(head_begin) + begin_pos
                    head_end_pos = html.text[head_begin_pos:].find(head_end) + head_begin_pos
                    one_headline = html.text[head_begin_pos + 1:head_end_pos]
                    news[one_headline] = one_new
                    begin_pos = end_pos
        message_news = ''
        for one_new in news.keys():
            message_news += one_new + ' ' + 'https://news.rambler.ru/world/' + news[one_new] + '\n\n'
        return message_news

    def answer(self, message):
        if isinstance(message.text, str):
            if message.text.lower() == 'да':
                self.bot.send_message(message.from_user.id,
                                      "Окей, какие у тебя планы на день? Напиши 'все' в конце списка дел")
                self.bot.register_next_step_handler(message, self.get_plans)
        else:
            self.bot.send_message(message.from_user.id, "Ответь буквами, пожалуйста)")
            self.bot.register_next_step_handler(message, self.answer)

    def get_age(self, message):
        if isinstance(message.text, str):
            if message.text.isdigit():
                self.db.update(message.from_user.id, 'age', message.text)
                self.bot.send_message(message.from_user.id, "Во сколько ты обычно просыпаешься?) Напиши в виде 09 00")
                self.bot.register_next_step_handler(message, self.get_time)
            else:
                self.bot.send_message(message.from_user.id, "Введи возраст цифрами плес")
                self.bot.register_next_step_handler(message, self.get_age)
        else:
            self.bot.send_message(message.from_user.id, "Попробуй ещеее")
            self.bot.register_next_step_handler(message, self.get_age)

    def get_zodiac(self, message):
        if isinstance(message.text, str):
            if message.text.lower() in const.HOROSCOPE.keys():
                # user['zodiac'] = message.text.lower()
                self.db.update(message.from_user.id, 'zodiac', message.text)
                self.bot.send_message(message.from_user.id,
                                      'Будем знакомы, {})'.format(self.db.get_data(message.from_user.id, 'name')))
                self.bot.send_message(message.from_user.id, "Напиши 'меню', и я покажу тебе, что умею")
            else:
                self.bot.send_message(message.from_user.id, "Упс, кажется, ты написал лажу, попробуй еще раз))")
                self.bot.register_next_step_handler(message, self.get_zodiac)
        else:
            self.bot.send_message(message.from_user.id, "Напиши буквами!")
            self.bot.register_next_step_handler(message, self.get_zodiac)

    def check_have_zodiac(self, message, user_id, type_of_hor):
        if self.db.get_data(user_id, 'zodiac') is None or type_of_hor == 'not_for_user':
            self.bot.send_message(user_id, "Какому знаку?")
            self.bot.register_next_step_handler(message, self.get_another_zodiac)
        else:
            self.bot.send_message(user_id, "Окей, погнали искать гороскоп)")
            self.bot.send_message(user_id, self.get_horoscope(self.db.get_data(user_id, 'zodiac').lower()))

    def get_horoscope(self, zodiac):
        horoscope = ''
        different_hor = {'': 'ТВОЙ ГОРОСКОП НА СЕГОДНЯ\n', 'erotic/': '\n\nЛЮБОВНЫЙ ГОРОСКОП\n',
                         'career/': '\n\nФИНАНСОВЫЙ ГОРОСКОП\n'}
        for kind in different_hor.keys():
            html = requests.request(url='https://horoscopes.rambler.ru' + const.HOROSCOPE[zodiac] + kind, method='GET')
            begin = '"PageContentData":{"items":[{"text":"'
            begin_pos = html.text.find(begin) + len(begin)
            end = '"}]},'
            end_pos = html.text.find(end, begin_pos)
            horoscope += different_hor[kind] + html.text[begin_pos:end_pos]
        return horoscope[0:len(horoscope) - 2]

    def check_user(self, user_id):  # ну не отправляет(((
        if str(datetime.datetime.now().time()).startswith('00:00'):
            for user in self.db.get_users_id():
                self.db.update(user, 'updated', False)
        if not self.db.get_data(user_id, 'updated') and \
                self.db.get_data(user_id, 'time').startswith(str(datetime.datetime.now().time())[0:5]):
            message_1 = 'Доброе утро, ' + self.db.get_data(user_id, 'name') + \
                        '! Просыпайся и улыбайся)\n\n' + self.get_horoscope(
                self.db.get_data(user_id, 'zodiac').lower())
            message_2 = 'Последние новости мира: ' + self.get_news(user_id)
            message_3 = 'Хорошего дня, и помни: сегодня у тебя все получится!'
            self.db.update(user_id, 'updated', True)
            self.bot.send_message(user_id, message_1)
            self.bot.send_message(user_id, message_2)
            self.bot.send_message(user_id, message_3)

    def play(self):
        self.bot.polling(none_stop=True, interval=0)

    def check_data(self):
        while True:
            for user_id in self.db.get_users_id():
                self.check_user(user_id)
            time.sleep(30)


if __name__ == '__main__':
    bot = Bot('740176362:AAEf13uvT3gGngaPB2XVraAPqTa00IdgBdc')
    #sending_message = Process(target=bot.check_data, args=())
    #sending_message.start()
    while True:
        try:
            bot.play()
        except Exception:
            time.sleep(15)
