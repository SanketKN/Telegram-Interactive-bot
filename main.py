from telegram import update
from telegram.ext import updater, InlineQueryHandler, CommandHandler, Updater, run_async
import requests
import re
def get_url():
   contents = requests.get('https://random.dog/woof.json').json()
   url = contents['url']
   return url
def get_image_url():
    allowed = ['jpg','jpeg','png']
    filext = ''
    while filext not in allowed :
        url = get_url()
        filext = re.search("([^.]*)$",url).group(1).lower()
        return url
@run_async
def pic(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send = update.message.chat_id
    bot.send_photo(chat_id=chat_id,photo=url)
def hello(bot,update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id,text='HeY what\'s up. if ya want a pic , say /pic')

def main():
    updater = Updater('YOUR_TOKEN');
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pic',pic))
    dp.add_handler(CommandHandler('hello',hello))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
