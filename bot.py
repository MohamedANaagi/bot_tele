from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

<<<<<<< HEAD
TOKEN = "7718089015:AAEl7w8MCy5iIEhYVmP-53wVQ9Cb5VvmOVY"
=======
TOKEN = "7718089015:AAEl7w8MCy5iIEhYVmP-53wVQ9Cb5VvmOVY"  # يفضل تخليه في ملف .env أو متغير بيئي عشان الأمان
>>>>>>> fffaf25f186779e6c7e14ba98523ebe38a17b7dc


# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
<<<<<<< HEAD
        [KeyboardButton("بيسبسيسبيسبي ➗")],
        [KeyboardButton("gfdgdfgdfg 🧪")],
        [KeyboardButton("أحياء 🌿")],
        [KeyboardButton("فيزياء ⚡")]

    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("👋 مرحبًا بك! اختر القسم من القائمة:", reply_markup=reply_markup)

# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "رياضيات" in text:
        await update.message.reply_text("➗ قسم الرياضيات: شرح ومصادر مهمة، تقدر تشوف الرابط: https://t.me/+9kRyaX2EMFRlNDc0")
    elif "كيمياء" in text:
        await update.message.reply_text("🧪 قسم الكيمياء: هتلاقي فيه كل ما يخص الكيمياء بشكل مبسط.")
    elif "أحياء" in text:
        await update.message.reply_text("🌿 قسم الأحياء: معلومات شيقة ومفيدة تساعدك في المذاكرة.")
    elif "فيزياء" in text:
        await update.message.reply_text("⚡ قسم الفيزياء: فهم القوانين والمسائل بطريقة سهلة.")
    else:
        await update.message.reply_text("😅 لم أفهم ذلك. اختر من الأزرار تحت أو اكتب /start لإعادة القائمة.")

# تشغيل البوت
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ البوت شغال... روح على تليجرام وجرب /start")
    application.run_polling()

if __name__ == "__main__":
    main()
