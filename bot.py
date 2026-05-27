from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8495671284:AAEfn-QHK1PHjoGrRvDKSvYkDRzk0dyLB1U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("InfoHub Bot is live 🔥")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("All systems working 👍")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))

app.run_polling()
