# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

def kall():

    import telebot
    from random import randint

    bot = telebot.TeleBot(
        "", parse_mode=None)

    znachenie = ''  # Текущее значение калькулятора
    old_znachenie = ''

    keyboard = telebot.types.InlineKeyboardMarkup()  # Клавиатура
    keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),  # Кнопки
                 telebot.types.InlineKeyboardButton('C', callback_data='C'),
                 telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                 telebot.types.InlineKeyboardButton('/', callback_data='/'),)

    keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
                 telebot.types.InlineKeyboardButton('8', callback_data='8'),
                 telebot.types.InlineKeyboardButton('9', callback_data='9'),
                 telebot.types.InlineKeyboardButton('*', callback_data='*'),)

    keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
                 telebot.types.InlineKeyboardButton('5', callback_data='5'),
                 telebot.types.InlineKeyboardButton('6', callback_data='6'),
                 telebot.types.InlineKeyboardButton('-', callback_data='-'),)

    keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
                 telebot.types.InlineKeyboardButton('2', callback_data='2'),
                 telebot.types.InlineKeyboardButton('3', callback_data='3'),
                 telebot.types.InlineKeyboardButton('+', callback_data='+'),)

    keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                 telebot.types.InlineKeyboardButton('0', callback_data='0'),
                 telebot.types.InlineKeyboardButton(',', callback_data='.'),
                 telebot.types.InlineKeyboardButton('=', callback_data='='),)

    @bot.message_handler(content_types=['text'])
    def vhod_soob(message):
        message.text = message.text.lower()
        if message.text == 'калькулятор':
            global znachenie
            if znachenie == '':
                bot.send_message(message.from_user.id, '0',
                                 reply_markup=keyboard)
            else:
                bot.send_message(message.from_user.id, znachenie,
                                 reply_markup=keyboard)

    # Возврат от нажатой кнопки

    @bot.callback_query_handler(func=lambda call: True)
    def vozvrat_ot_knopki(query):
        global znachenie, old_znachenie
        data = query.data

        if data == 'no':
            pass
        elif data == 'C':
            znachenie = ''
        elif data == '<=':
            if znachenie != '':
                znachenie = znachenie[:len(znachenie)-1]
        elif data == '=':
            try:
                znachenie = str(eval(znachenie))
            except:
                znachenie = 'Ошибка!'
        else:
            znachenie += data

        if (znachenie != old_znachenie and znachenie != '') or ('0' != old_znachenie and znachenie == ''):
            if znachenie == '':
                bot.edit_message_text(chat_id=query.message.chat.id,
                                      message_id=query.message.message_id, text='0', reply_markup=keyboard)
                old_znachenie = '0'
            else:
                bot.edit_message_text(chat_id=query.message.chat.id,
                                      message_id=query.message.message_id, text=znachenie, reply_markup=keyboard)
                old_znachenie = znachenie

        if znachenie == 'Ошибка!':
            znachenie = ''

    bot.infinity_polling()


# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

def ugaday():

    import telebot
    from random import randint

    bot = telebot.TeleBot(
        "", parse_mode=None)

    kount = 0
    b = 0

    @bot.message_handler(content_types=["text"])
    def igra(message):
        global a
        a = str(randint(1, 1))
        message.text = message.text.lower()
        if message.text == 'игра':
            bot.reply_to(
                message, 'Включен режим игры - «Угадай числа».\nОтгадайте число от 1 до 1000.')
            bot.register_next_step_handler(message, get_info)

    def get_info(message):
        global kount
        if message.text == a:
            kount += 1
            bot.reply_to(message, f"Угадали c {kount} попытки!\nКонец игры.")
            exit()
        if message.text != a:
            kount += 1
            bot.reply_to(message, 'Не угадали введите еще!')
            bot.register_next_step_handler(message, igra2)

    def igra2(message):
        global kount
        if message.text == a:
            kount += 1
            bot.reply_to(message, f"Угадали c {kount} попытки\nКонец игры.")
            exit()
        if message.text != a:
            kount += 1
            bot.reply_to(message, 'Не угадали введите еще!')
        bot.register_next_step_handler(message, get_info)

    bot.infinity_polling()
