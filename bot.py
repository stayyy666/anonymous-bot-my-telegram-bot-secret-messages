import telebot

TOKEN = 7979103128:AAEkPNL-3TBZP_ChBgM_yANtynNH8WYBjoI
ADMIN_ID =7480275276

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id != ADMIN_ID:
        bot.send_message(message.chat.id, "سلام! پیام ناشناس خودتو همینجا بنویس و بفرست 😊")
    else:
        bot.send_message(message.chat.id, "ربات آماده دریافت پیام‌های ناشناسه ✨")

@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    if message.chat.id != ADMIN_ID:
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "✅ پیام ناشناس تو ارسال شد!")
    else:
        bot.send_message(message.chat.id, "📨 این پیام از طرف خودته!")

bot.polling()
