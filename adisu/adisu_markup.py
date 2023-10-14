from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup_adisu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
            InlineKeyboardButton("Importi borsa di studio", callback_data="a_bdsprimarata"),
            InlineKeyboardButton("Pendolare diventato \"in sede\"", callback_data="a_pendsede"),
            InlineKeyboardButton("Rimborso alloggio", callback_data="a_rimballoggio"),
            InlineKeyboardButton("Rimborso tassa regionale", callback_data="a_rimbtassareg"),
            InlineKeyboardButton("\"beneficiario sospeso\"", callback_data="a_bensospeso"),
            InlineKeyboardButton("Richiesta borsa in 2 rate", callback_data="a_borsa2rate"),
            InlineKeyboardButton("Chiedi a noi - Supporto", callback_data="a_link")
    )
    return markup

def markup_adisu_data():
    return ["a_bdsprimarata", "a_pendsede", "a_rimballoggio", "a_rimbtassareg", "a_bensospeso", "a_borsa2rate", "a_link"]