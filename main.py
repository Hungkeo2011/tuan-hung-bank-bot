import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏠 Trang chủ", callback_data="home")],
        [InlineKeyboardButton("📋 Dịch vụ", callback_data="services")],
        [InlineKeyboardButton("ℹ️ Giới thiệu", callback_data="about")],
        [InlineKeyboardButton("👨‍💻 Hỗ trợ", callback_data="support")]
    ]

    await update.message.reply_text(
        "👋 Chào mừng đến với TUẤN HÙNG BANK!\n\n"
        "Vui lòng chọn chức năng bên dưới:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "home": "🏠 Chào mừng đến với TUẤN HÙNG BANK!",
        "services": "📋 Danh sách dịch vụ hợp pháp đang được cập nhật.",
        "about": "ℹ️ Bot hỗ trợ thông tin và chăm sóc khách hàng.",
        "support": "👨‍💻 Vui lòng liên hệ quản trị viên."
    }

    await query.edit_message_text(messages.get(query.data, "Không tìm thấy chức năng."))

def main():
    if not TOKEN:
        raise RuntimeError("Chưa cấu hình BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    print("Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
