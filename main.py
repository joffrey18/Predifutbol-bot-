import telebot
import time

# Token de tu bot
TOKEN = "7718775955:AAEkbK0MwfCsI83uFGoxT-xmzeGuAtwi--I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 ¡Hola! Soy el bot de pronósticos de Joffrey.\nPronto enviaré los pronósticos del día ⚽️🔥")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Recibí tu mensaje. Pronto te enviaré los pronósticos 📊")

print("🤖 Bot ejecutándose...")
while True:
    try:
        bot.polling()
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
      
