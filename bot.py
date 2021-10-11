from telegram.ext import Updater, CommandHandler
def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет")
token = "1993640056:AAHqynug_2tGrNZe4wlbn6Sz_UlYPYzX-Sg"
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
updater.start_polling()
updater.idle()
