import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1020204415:AAGaHBZADh7arI7_Y5KPOUJULfsdmXTF3gY')


# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('🇺🇦')
    btn3 = types.KeyboardButton('🇷🇺')
    btn4 = types.KeyboardButton('🇧🇾')
    btn5 = types.KeyboardButton('🇺🇸')
    btn6 = types.KeyboardButton('🇮🇹')
    btn7 = types.KeyboardButton('🇪🇸')
    btn8 = types.KeyboardButton('🇩🇪')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    send_message = f"<b>{message.from_user.first_name}, здравствуйте!</b>\nЧтобы узнать данные про коронавируса напишите " \
                   f"Название страны, например: США, Россия, Беларусь и так далее\n\n Последние новости можно узнать нажав на символ <a href='https://sp.onliner.by/covid-19/'> 🦠 </a>"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша" or get_message_bot == "🇺🇸":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина" or get_message_bot == ("🇺🇦"):
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия" or get_message_bot == "🇷🇺":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь" or get_message_bot == "🇧🇾":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "италия" or get_message_bot == "🇮🇹":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция" or get_message_bot == "🇫🇷":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия" or get_message_bot == "🇩🇪":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония" or get_message_bot == "🇯🇵":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "испания" or get_message_bot == "🇪🇸":
        location = covid19.getLocationByCountryCode("ES")
    elif get_message_bot == "аргентина" or get_message_bot == "🇦🇷":
        location = covid19.getLocationByCountryCode("AR")
    elif get_message_bot == "польша" or get_message_bot == "🇵🇱":
        location = covid19.getLocationByCountryCode("PL")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)
