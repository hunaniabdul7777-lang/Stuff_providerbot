from telegram.ext import Updater, CommandHandler
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def start(update, context):
    args = context.args

    if args:
        key = args[0]

        if key == "p1":
            update.message.reply_text("🎬 Product 1 Demo")
            update.message.reply_video(video=open("demo1.mp4", "rb"))
            return

        if key == "p2":
            update.message.reply_text("🎬 Product 2 Demo")
            update.message.reply_video(video=open("demo2.mp4", "rb"))
            return

        update.message.reply_text("❌ Invalid demo link")
        return

    update.message.reply_text("Welcome! Demo sirf link se milta hai.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
