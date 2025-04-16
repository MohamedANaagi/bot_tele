from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7718089015:AAEl7w8MCy5iIEhYVmP-53wVQ9Cb5VvmOVY"  # يفضل تخليه في ملف .env أو متغير بيئي عشان الأمان

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("رياضيات ➗")],
        [KeyboardButton("كيمياء 🧪")],
        [KeyboardButton("فيزياء ⚡")],
        [KeyboardButton("أحياء 🌿")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("👋 مرحبًا بك! اختر القسم من القائمة:", reply_markup=reply_markup)

# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "رياضيات" in text:
        await update.message.reply_text("➗ قسم الرياضيات:\nفيه شروحات وتمارين قوية جدًا تساعدك تفهم بسرعة.\nادخل الجروب من هنا 👇\nhttps://t.me/+9kRyaX2EMFRlNDc0")
    elif "كيمياء" in text:
        await update.message.reply_text("🧪 قسم الكيمياء:\nهتلاقي شرح التفاعلات، المعادلات، وأهم الأسئلة المتكررة.")
    elif "فيزياء" in text:
        await update.message.reply_text("⚡ قسم الفيزياء:\nتعلم قوانين الحركة، الشحنات، والطاقة بطريقة بسيطة وسهلة.")
    elif "أحياء" in text:
        await update.message.reply_text("🌿 قسم الأحياء:\nمعلومات عن جسم الإنسان، الخلايا، والأنظمة الحيوية مع أسئلة تدريبية.")
    else:
        await update.message.reply_text("😅 لم أفهم ذلك. اختر من الأزرار أو اكتب /start لإعادة القائمة.")

# تشغيل البوت
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ البوت شغال... روح على تليجرام وجرب /start")
    application.run_polling()

if __name__ == "__main__":
    main()
