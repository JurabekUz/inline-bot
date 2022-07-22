import logging

from telegram import __version__ as TG_VER

from tgbot.models import Post

from telegram.ext import (
    CallbackContext
)
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update


def post_handler(update: Update, context: CallbackContext) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=post.id,
            title=post.title,
            description = post.content,
            thumb_url = post.image,
            thumb_width = 5,
            thumb_height = 5,
            input_message_content=InputTextMessageContent(message_text=f"{post.content}\n{post.image}\n", parse_mode=None))
            for post in Post.objects.filter(title__icontains=query)
        
    ]

    return update.inline_query.answer(results)