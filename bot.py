from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from flask import Flask
from threading import Thread

app_web = Flask("")

TOKEN = '7939387490:AAF65XCR2KBpiZd77-6K2Ssiiex_PYHq8NA'

@app_web.route("/")
def home():
    return "Bot is running!"

def run_web():
    app_web.run(host="0.0.0.0", port=8080)

def simpan_ke_file(teks):
    with open("catatan.txt", "a") as file:
        file.write(teks + "\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Saya bot Telegram kamu 🎉")

async def bantuan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = (
        "Ini daftar perintah yang bisa kamu coba:\n"
        "/start - Mulai chat dengan bot\n"
        "/bantuan - Tampilkan daftar perintah\n"
        "/halo - Sapa bot\n"
    )
    await update.message.reply_text(pesan)

async def halo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo juga! Senang ngobrol denganmu 😊")

async def pesan_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teks = update.message.text.lower()
    if teks.startswith("/"):
        return
    if teks == "halo":
        await update.message.reply_text("Hai juga! 👋")
    elif teks == "siapa kamu":
        await update.message.reply_text("Saya adalah bot keren buat belajar Python! 🐍")
    else:
        simpan_ke_file(teks)
        await update.message.reply_text("Pesanmu sudah disimpan!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bantuan", bantuan))
app.add_handler(CommandHandler("halo", halo_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, pesan_handler))

if __name__ == "__main__":
    # Jalankan Flask di thread terpisah
    Thread(target=run_web).start()

    print("Bot berjalan... 🚀")
    # Jalankan polling di main thread
    app.run_polling()
