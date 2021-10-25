# from telegram.user import User
# from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.update import Update
import requests
from telegram.ext.filters import Filters

updater  = Updater(token="2018662360:AAHdagKDMGy008qb5_dxvGev6xbxYjGc-qY")


def start(update: Update, context:CallbackContext):
    update.message.reply_text('Assalom alaykum Wiki Search bot ga xush kelibsiz.'
    'Qidirish uchun /search kalit so`zidan keyin qidiralayotgan terminni kiriting. Misol uchun: /search Amir Temur ')
    # context.bot.send_message(chat_id=update.message.chat_id,text='Salom yana bir bor ')

def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args)==0:
        update.message.reply_text('Hech bo`lmasa nimadir kiriting. Masalan: /search Wilyam Shakespear')

    else :

        search_text  =' '.join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php',{
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace' : 0,
            'format': 'json',
        })
        result = response.json()
        link =result[3]
        if len(link):
            update.message\
                    .reply_text('Sizning so`rovingiz bo`yicha havola: '+ link[0])
        else:
            update.message\
                    .reply_text('Sizning so`rovingiz bo`yicha havola yo`q')

dispatcher  = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('search',search))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()
