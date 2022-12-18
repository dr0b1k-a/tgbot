import telebot
from telebot import types
import random
from YandexImagesParser.ImageParser import YandexImage

parser = YandexImage()
arrImages = []

for item in parser.search("Шрек"):
    arrImages.append(item.url)


bot = telebot.TeleBot('5967913131:AAHb0hitjiIFJ9lDcfUBHGfLAdwVEAqLuWI')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("DOG")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, я готов к работе, пожалуйста не пишите никаких сообщений".format(message.from_user), reply_markup=markup)
    
            
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'DOG' :
            answer = random.choice(arrImages)
    bot.send_photo(message.chat.id, answer)
    

bot.polling(none_stop=True, interval=0)