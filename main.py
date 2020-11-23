import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1487478340:AAFwUd_q49KcE5JuWJ2B2UZodUbZg6sJeJE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("У світі загалом")
    btn2 = types.KeyboardButton("Україна")
    btn3 = types.KeyboardButton("США")
    btn4 = types.KeyboardButton("Китай")
    markup.add(btn1, btn2, btn3, btn4)

    send_mess = f"<b>Привіт {message.from_user.first_name}!</b>Вкажіть країну або виберіть з поданих"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "україна":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "росія":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "індія":
        location = covid19.getLocationByCountryCode("IN")
    elif get_message_bot == "бразилія":
        location = covid19.getLocationByCountryCode("BR")
    elif get_message_bot == "польща":
        location = covid19.getLocationByCountryCode("PL")
    elif get_message_bot == "китай":
        location = covid19.getLocationByCountryCode("CN")
    else:
        location = covid19.getLatest()
        final_message = f"<u> Could not find this country. Here is the data about the whole world:</u>\nInfected: <b>{location['confirmed']}</b>"
    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Data about the country: </u>\n Population : {location[0]['country_population']} \n last update: {date[0]} {time[0]}\n Infected <b>{location[0]['latest']['confirmed']}</b>"
    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
