# Загрузчик видео с YouTube (в видео и аудио версиях)
from controller import * 
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = '5766062444:AAFio0sBZ20a8Z-7ATc67j_xG_BNi39OMH8'
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('hi', start))
updater.dispatcher.add_handler(CommandHandler('res', get_resolution))
updater.dispatcher.add_handler(CommandHandler('bit', get_bitrate))
updater.dispatcher.add_handler(CommandHandler('video', get_video))
updater.dispatcher.add_handler(CommandHandler('audio', get_audio))
updater.dispatcher.add_handler(CommandHandler('help', help))

print('server start')
updater.start_polling()
updater.idle()