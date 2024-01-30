# import telebot
# from config_data import config
#
# bot = telebot.TeleBot(token=config.BOT_TOKEN)
# url = r'https://imdb-top-100-movies.p.rapidapi.com/'
# api_host = "imdb-top-100-movies.p.rapidapi.com"
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Hello world!")
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#
# if __name__ == '__main__':
#     bot.infinity_polling()

from site_api.core import site_api, url, headers, params

movie_by_id = site_api.get_movie_data_by_id()

response = movie_by_id("GET", url, headers, params, 5, timeout=3)
response = response.json()

print(response)
