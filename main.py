import pafy, requests, json
import Constants as keys
from telegram.ext import *
import responses as R

print('Bot is starting')

def start_command(update, context):
	update.message.reply_text('Send the link of the video that you want to download. :)')


def handle_message(update, context):
	text = str(update.message.text)
	user = update.effective_user
	print(f'{user["username"]}: {text}')
	response = R.sample_responses(text)
	print(f'Bot: {response}')

	update.message.reply_text(response)

def error(update, context):
	print(f"Update {update} caused error {context.error}")

def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	# dp.add_handler(CommandHandler("help", help_command))
	# dp.add_handler(CommandHandler("vaccine", vaccine_command))
	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)


	updater.start_polling()
	updater.idle()

main()