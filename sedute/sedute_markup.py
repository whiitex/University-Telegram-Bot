from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup_sedute():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("DEI", callback_data="sedute_dei"),
        InlineKeyboardButton("DMMM", callback_data="sedute_dmmm"),
        InlineKeyboardButton("DICATECh", callback_data="sedute_dicatech"),
        InlineKeyboardButton("ArCoD", callback_data="sedute_arcod"),
    )
    return markup

def markup_sedute_data():
    return ["sedute_dei", "sedute_dmmm", "sedute_dicatech", "sedute_arcod"]