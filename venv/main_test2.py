import telebot
from telebot import types
bot = telebot.TeleBot("5798604732:AAE39qStxR7ApjME0G0D0nwLOJf3nCH3zrQ")

#Команда start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_start = types.InlineKeyboardButton(text='Начать', callback_data='yes'); #кнопка «Начать»
    keyboard.add(key_start); #добавляем кнопку в клавиатуру
    bot.send_message(message.from_user.id, "Привет, это самый крутой ГДЗ", reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура

    key_physics = types.InlineKeyboardButton(text = 'Физика', callback_data = 'physics'); #кнопка «Физика»
    keyboard.add(key_physics); #добавляем кнопку в клавиатуру

    key_him = types.InlineKeyboardButton(text = 'Химия', callback_data = 'himiya');  # кнопка «Химия»
    keyboard.add(key_him)

    key_math = types.InlineKeyboardButton(text = 'Математика', callback_data = 'math'); #кнопка «Математика»
    keyboard.add(key_math)

    key_geometrya = types.InlineKeyboardButton(text = 'Геометрия', callback_data = 'geometrya');  # кнопка «Геометрия»
    keyboard.add(key_geometrya)

    key_ukr_litr = types.InlineKeyboardButton(text = 'Укр. язык/Литература', callback_data = 'ukr.yz/litra');  # Укр. язык/Литература»
    keyboard.add(key_ukr_litr)

    key_eng = types.InlineKeyboardButton(text = 'Английский язык', callback_data = 'eng');  #Англ»
    keyboard.add(key_eng)

    key_georhaph = types.InlineKeyboardButton(text = 'География', callback_data = 'georaph');  #География»
    keyboard.add(key_georhaph)

    key_bio = types.InlineKeyboardButton(text = 'Биология', callback_data = 'bio');  #Биология»
    keyboard.add(key_bio)

    bot.send_message(call.message.chat.id, "Выбери интересующий предмет ниже👇", reply_markup = keyboard);


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.send_message(call.message.chat.id, ('Прикрепи фото (чтобы было четко видно задание).  '
                                            'После отправки фото, нажми на кнопку "Отправлено!✅"'));

bot.polling(none_stop=True, interval=0)