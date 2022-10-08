import functions.functions as func
#import gui.gui as g
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет! Я умею скачивать аудио и видео файлы с Youtube")

def get_resolution(update: Update, context: CallbackContext):
    msg = update.message.text 
    items = msg.split()
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=func.get_resolution_list(items[1]))

def get_bitrate(update: Update, context: CallbackContext):
    msg = update.message.text 
    items = msg.split()
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=func.get_bitrate_list(items[1]))

def get_video(update: Update, context: CallbackContext):
    msg = update.message.text 
    items = msg.split()
    func.download_video(items[1], items[2], items[3])
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Видео успешно загружено')

def get_audio(update: Update, context: CallbackContext):
    msg = update.message.text 
    items = msg.split()
    func.download_audio(items[1], items[2], items[3])
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text='Аудио успешно загружено')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('''Инструкция для работы с загрузчиком Youtube:
/hi - приветствие перед началом работы

Перед скачиванием файлов необходимо определить доступное качество для загрузки с помощью команд:
/res_'ссылка на видео' - узнать доступное качество видео для скачивания 
/bit_'ссылка на видео' - узнать доступный битрейт аудио для скачивания

Далее, определившись с качеством, можно скачать файл с помощью команд:
/video_'ссылка на видео'_'путь для сохранения'_'разрешение видео (например, 360p)' - скачать видеофайл с Youtube
/audio_'ссылка на видео'_'путь для сохранения'_'битрейт аудио (например, 144kbps)' - скачать аудиофайл с Youtube

/help - справка по боту''')