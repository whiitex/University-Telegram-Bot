import telebot
from sedute.sedute_markup import *

TOKEN = "5887892548:AAGvwWOAY-8gHodUFfF4FkrRe5r4BaXWmZs"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


def invia_link(call, url, dipartimento):
    link = InlineKeyboardMarkup()
    link.row_width = 1
    link.add(InlineKeyboardButton("Sedute di Laurea " + dipartimento, url=url))
    bot.send_message(call.from_user.id, "Ecco il link ufficiale PoliBa per la sedute di laurea del dipartimento "
                     + dipartimento, reply_markup=link)
########################################################################################################################


def sedute_1(message):
    bot.send_message(message.from_user.id, "Qual è il tuo corso di laurea?", reply_markup=markup_sedute())


def callback_sedute_1(call):
    match call.data:
        case "sedute_dei":
            invia_link(call, "http://dei.poliba.it/sedute-di-laurea-2/", "DEI")
        case "sedute_dmmm":
            invia_link(call, "https://www.dmmm.poliba.it/index.php/it/calendario-sedute-di-laurea", "DMMM")
        case "sedute_dicatech":
            invia_link(call, "https://www.dicatechpoliba.it/it/dicatech-sedute-di-laurea", "DICATECh")
        case "sedute_arcod":
            invia_link(call, "https://www.dipartimentoicar.it/calendari-sedute-di-laurea/", "ArCoD")
    bot.delete_message(call.from_user.id, call.message.message_id)
