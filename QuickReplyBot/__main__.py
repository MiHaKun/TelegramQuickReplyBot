import json

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    ContextTypes,
    PicklePersistence,
    filters,
)
from . import bot_token, proxy_uri, admin_ids, logger, inline_cmd
import uuid


async def start(update: Update, context: ContextTypes):
    user = update.effective_user
    if not user.id in admin_ids:
        await update.effective_chat.send_message(
            "⚠️ You are not allowed to use this bot."
        )
        return
    await update.effective_chat.send_message(
        f"Hi, {user.first_name}, I am working now."
    )


def get_quickreply():
    with open("./quick_reply.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


async def on_inline_query(update: Update, context: ContextTypes):
    query = update.inline_query.query
    user = update.inline_query.from_user
    if not user.id in admin_ids:
        query.answer([])
    if not query:
        return

    result = []
    for idx, quick_reply in enumerate(get_quickreply()):
        params = {
            "id": uuid.uuid4().hex,
            "title": quick_reply["title"],
        }
        buttons = quick_reply.get("buttons", [])
        btn_matrx = []
        for btn_row in buttons:
            row = []
            for btn in btn_row:
                row.append(InlineKeyboardButton(btn["text"], url=btn["url"]))
            btn_matrx.append(row)
        keyboard = InlineKeyboardMarkup(btn_matrx)
        params["reply_markup"] = keyboard
        params["input_message_content"] = InputTextMessageContent(
            f"<b>{quick_reply['title']}</b>\n\n{quick_reply['msg']}", parse_mode="HTML"
        )

        result.append(InlineQueryResultArticle(**params))
    await update.inline_query.answer(result)


async def error_handler(update: Update, context: ContextTypes):
    logger.error(f"Update: {update} caused error: {context.error}")
    # await update.effective_chat.send_message(f"An error occurred: {context.error}")


if __name__ == "__main__":
    pickle_persistence = PicklePersistence(filepath=f"./cache.pickle")
    application = (
        ApplicationBuilder()
        .token(bot_token)
        .persistence(persistence=pickle_persistence)
    )
    if proxy_uri:
        application = application.proxy(proxy_uri).get_updates_proxy(proxy_uri).build()
    else:
        application = application.build()

    application.add_handler(
        CommandHandler(
            "start",
            start,
            filters.ChatType.PRIVATE,
        )
    )
    application.add_handler(
        InlineQueryHandler(on_inline_query, pattern=f"^{inline_cmd}")
    )
    application.add_error_handler(error_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
