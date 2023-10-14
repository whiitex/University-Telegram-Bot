from random import choice

from orario.orario_functions import *
from adisu.adisu_functions import *
from sedute.sedute_functions import *

# my very secret (!) token is stored in a json file having this template:
# { "token" : "abc123abc123" }
import json
token_json = json.load(open("telegram_token.json"))
TOKEN = token_json["token"]


bot = telebot.TeleBot(TOKEN, parse_mode=None)
# chat_id = message.chat.id (int)
# chat_id = call.from_use.id (int)

bot.delete_my_commands(scope=None, language_code=None)
bot.set_my_commands(commands=[
        telebot.types.BotCommand("start", "Inizia ad usare il bot"),
        # telebot.types.BotCommand("getid", "Scopri il tuo id"),
        telebot.types.BotCommand("orario", "Orario del tuo cdl"),
        # telebot.types.BotCommand("howto", "Come usare il bot?"),
        # telebot.types.BotCommand("close", "Termina il bot"),
        telebot.types.BotCommand("sedute", "Calendario sedute di laurea"),
        telebot.types.BotCommand("adisu", "Domande frequenti Adisu")]
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Benvenuto, chiedimi ciò di cui hai bisogno o scegli nel menu in basso a sinistra.")


@bot.message_handler(commands=['getid'])
def get_chat_user_id(message):
    bot.send_message(message.chat.id, "Il tuo ID è: " + str(message.from_user.id))


@bot.message_handler(commands=['howto'])
def get_chat_user_id(message):
    bot.send_message(message.chat.id, "Informazioni sul bot")


# just for fun
@bot.message_handler(func=lambda m: "white" in m.text.lower())
def get_chat_user_id(message):
    bot.send_message(message.chat.id, "Lo sviluppatore 😎🦦🦍")


'''
# TEMPORARY rispondere al messaggio
@bot.message_handler(func=lambda m: m.content_type == "text" )
def prova_text(message):
    bot.reply_to(message, "Questo messaggio posso capirlo. \nIt is a " + message.content_type)
'''


# HANDLING NON-UNDERSTANDABLE MESSAGES
@bot.message_handler(content_types=["audio", "voice", "sticker", "photo", "video", "document", "contact", "location", "contact"])
def handle_non_understandable_message(message):
    if message.content_type in ["audio", "voice"]:
        bot.reply_to(message, choice(["Non capisco messaggi vocali", "Trascrivi il messaggio, per favore", "Non posso ascoltare!"]))
    else:
        bot.reply_to(message, choice(["Non capisco...", "Non posso capire questo messaggio", "Capisco solo messaggi testuali"]))
########################################################################################################################
# ORARIO


@bot.message_handler(func=lambda m: ("orario" in m.text.lower()) and ("triennale" in m.text.lower() or "magistrale" in m.text.lower()))
def orario_triennale_magistrale_handler(m):
    if "triennale" in m.text.lower():
        bot.send_message(m.chat.id, "Qual è il tuo corso di laurea?", reply_markup=markup_orario_tr_dip())
    else: bot.send_message(m.chat.id, "Qual è il tuo corso di laurea?", reply_markup=markup_orario_mg_dip())


@bot.message_handler(commands=["orario"])
@bot.message_handler(func=lambda m: "orario" in m.text.lower())
@bot.message_handler(func=lambda m: "orario" in m.text.lower() and "semestre" in m.text.lower())
def message_handler_orario(message):
    orario_1(message)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_cc_data())
def callback_orario(call):
    callback_orario_cc_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_cc_tr_data())
def callback_orario_cc_tr(call):
    callback_orario_cc_tr_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_cc_mg_data())
def callback_orario_cc_mg(call):
    callback_orario_cc_mg_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_tr_dei_data())
def callback_orario_tr_dei(call):
    callback_orario_tr_dei_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_tr_dmmm_data())
def callback_orario_tr_dmmm(call):
    callback_orario_tr_dmmm_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_tr_dicatech_data())
def callback_orario_tr_dicatech(call):
    callback_orario_tr_dicatech_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_tr_dicar_data())
def callback_orario_tr_dicar(call):
    callback_orario_tr_dicar_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_mg_dei_data())
def callback_orario_mg_dei(call):
    callback_orario_mg_dei_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_mg_dmmm_data())
def callback_orario_mg_dmmm(call):
    callback_orario_mg_dmmm_1(call)


@bot.callback_query_handler(func=lambda call: call.data in markup_orario_mg_dicatech_data())
def callback_orario_mg_dicatech(call):
    callback_orario_mg_dicatech_1(call)
########################################################################################################################
# ADISU


@bot.message_handler(commands=["adisu"])
def message_handler_adisu(message):
    adisu_1(message)


@bot.callback_query_handler(func=lambda call: call.data in markup_adisu_data())
def callback_adisu_quest(call):
    callback_adisu_quest_1(call)


########################################################################################################################
@bot.message_handler(func=lambda m: "sedute" in m.text.lower())
@bot.message_handler(commands=["sedute"])
def message_handler_sedute_di_laurea(message):
    sedute_1(message)


@bot.callback_query_handler(func=lambda call: call.data in markup_sedute_data())
def callback_sedute(call):
    callback_sedute_1(call)
########################################################################################################################


bot.infinity_polling(timeout=60)
