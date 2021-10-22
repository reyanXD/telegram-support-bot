import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import TELEGRAM_SUPPORT_CHAT_ID

def start(update, context):

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=1926090919,
        text=f"""
📞 Connected {user_info}.
        """,
    )

def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    return dp
