from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
updater=Updater ("5793317961:AAHYC0yBGd69UciYxdjmsEMnVkKlAXY0DrY")


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}!')


updater.start_polling()
updater.idle()
