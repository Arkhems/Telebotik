import requests
from bs4 import BeautifulSoup
import telebot
import lxml
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

pages = requests.get('https://www.kinopoisk.ru/lists/movies/top_1000/')
soup = BeautifulSoup(pages.text, 'lxml')
TOKEN = '6178487250:AAFI9D4GKTeuClzzJyKqJej2MQwvGAYnl0o'
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Смотреть фильм'))
keyboard.add(KeyboardButton('Топ-10 за месяц'))
keyboard.add(KeyboardButton('Оценка и описание фильма'))
ranking = soup.find_all('span', class_="desktop-list-main-info_secondaryTitle__ighTt")

@bot.message_handler(commands=['help','info'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Этот бот создан для предъявления информации о фильмах.', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    hiphoto = open('C:\Python\greetings.jpg','rb')
    bot.send_photo(message.chat.id, hiphoto)
    bot.send_message(message.chat.id, f'Доброе время суток {message.from_user.first_name}.\nВыберите интересующий вас вариант в меню.', reply_markup=keyboard)

@bot.message_handler(func=lambda s: 'Смотреть фильм' in s.text)
def send_input(message):
    bot.send_message(message.chat.id,'Введите название.', reply_markup=keyboard)
    bot.register_next_step_handler(message, on_click_search)

def on_click_search(message):
    film_name = message.text


    film_URL = 'https://www.kinopoisk.ru/film/927898/'
    bot.send_message(message.chat.id,f'\n<u>{film_URL}</u>', parse_mode='html',reply_markup=keyboard)

@bot.message_handler(func=lambda s: 'Оценка и описание фильма' in s.text)
def send_input(message):
    bot.send_message(message.chat.id,'Введите название.', reply_markup=keyboard)
    bot.register_next_step_handler(message, on_click_rate)

def on_click_rate(message):
    film_name = message.text
    soup.find('<span>', class_= 'styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')
    film_URL = 'https://www.kinopoisk.ru/film/927898/'
    bot.send_message(message.chat.id, f'\n<u>{film_URL}</u>', parse_mode='html', reply_markup=keyboard)
    bot.send_message(message.chat.id, str(soup.find('span', class_= 'styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')), parse_mode='html', reply_markup=keyboard)

@bot.message_handler(func=lambda s: 'Топ-10 за месяц' in s.text)
def send_input(message):


    bot.send_message(message.chat.id,f'', parse_mode='html',reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def search(message):
    film_name = message.text

    film_URL = 'https://www.kinopoisk.ru/film/927898/'
    bot.send_message(message.chat.id,f'\n<u>BRUH</u>', parse_mode='html',reply_markup=keyboard)



bot.infinity_polling()