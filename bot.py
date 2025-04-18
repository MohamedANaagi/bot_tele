from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ⚠️ التوكن الخاص بالبوت - لا تنشره علنًا!
TOKEN = "7718089015:AAGBdkmDIRnEHURJLOKPLCCuCevz5K0Rgo4"

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("رياضيات ➗")],
        [KeyboardButton("كيمياء 🧪")],
        [KeyboardButton("أحياء 🌿")],
        [KeyboardButton("فيزياء ⚡")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("👋 مرحبًا بك! اختر القسم من القائمة:", reply_markup=reply_markup)

# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "رياضيات" in text:
        await update.message.reply_text("➗ قسم الرياضيات: شرح ومصادر مهمة، تقدر تشوف الرابط: https://t.me/+l4-SQ8LuiK81Y2Jk")
    elif "كيمياء" in text:
        await update.message.reply_text("🧪 قسم الكيمياء: هتلاقي فيه كل ما يخص الكيمياء بشكل مبسط، الرابط: https://t.me/+B4svSKu6mOEyZDk8")
    elif "أحياء" in text:
        await update.message.reply_text("🌿 قسم الأحياء: معلومات شيقة ومفيدة تساعدك في المذاكرة، الرابط: https://t.me/+gPZoFtzpfx0yODE0")
    elif "فيزياء" in text:
        await update.message.reply_text("⚡ قسم الفيزياء: فهم القوانين والمسائل بطريقة سهلة، الرابط: https://t.me/+3G-R9ZFtqgI5MWZk")
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
