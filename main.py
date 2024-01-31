import telebot
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

from site_api.core import site_api, url, headers, params

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(token="your-token", state_storage=state_storage)


class MyStates(StatesGroup):
    # Just name variables differently
    state_get_movie = State()  # creating instances of State class is enough from now
    state_top100_movies = State()
    state_series_data = State()
    state_top100_series = State()


@bot.message_handler(commands=['start'])
def start(message):
    bot.set_state(message.from_user.id, MyStates.state_get_movie, message.chat.id)
    bot.send_message(message.chat.id, 'Hello! What movie would you like to inspect? Just write number')


@bot.message_handler(state=MyStates.state_get_movie, is_digit=True)
def get_movie_by_id(message):
    movie_id = int(message.text.strip())
    movie_by_id = site_api.get_movie_data_by_id()
    response = movie_by_id("GET", url, headers, params, movie_id, timeout=3)
    response = response.json()
    bot.reply_to(message,
                 f"Place: {movie_id} \n{response['title']} \nRating: {response['rating']}"
                 f"\nYear: {response['year']} \n {response['image']}")


@bot.message_handler(commands=['exit'])
def exit(message):
    bot.send_message(message.chat.id, "Your state was cancelled.")
    bot.delete_state(message.from_user.id, message.chat.id)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())


if __name__ == '__main__':
    bot.infinity_polling()
