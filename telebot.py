import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import telegram
import main
import os

class telebot:
    
    token = os.getenv("my_token")
    chat_id = os.getenv("chat_id")
    data_class = main.main()
    
    def get_news(self, update, context, data_class) :
        bot = telegram.Bot(token=self.token)
        update.message.reply_text("잠시만 기다려 주세요!")
        text = data_class.restructure_data()
        bot.sendMessage(chat_id=self.chat_id, text=text)

   
    updater = Updater(token, use_context=True)

    get_news_handler = CommandHandler('get', get_news)
    updater.dispatcher.add_handler(get_news_handler)

    updater.start_polling(timeout=3)
    updater.idle()