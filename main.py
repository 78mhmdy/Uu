from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline

# تحميل النموذج المُدرَّب
model = pipeline("text-generation", model="./my_finetuned_model")

# دالة للتعامل مع الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أنا بوت متخصص في البرمجة. كيف يمكنني مساعدتك؟")

# دالة للتعامل مع الرسائل النصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = model(user_input, max_length=50, num_return_sequences=1)
    await update.message.reply_text(response[0]['generated_text'])

# دالة رئيسية لتشغيل البوت
def main():
    application = Application.builder().token("YOUR_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()

    
