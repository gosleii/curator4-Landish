import telebot

bot = telebot.TeleBot('6893818501:AAFqXAHNFJGqZwjcfUW7yM_lcO_ZS7HsUfA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['read'])
def main(message):
    bot.send_message(message.chat.id, 'ЧИТАЙ!', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://pastebin.com/)', parse_mode='Markdown')

bot.infinity_polling()