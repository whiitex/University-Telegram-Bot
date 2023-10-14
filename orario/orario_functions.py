import telebot
from orario.orario_markup import *

TOKEN = "5887892548:AAGvwWOAY-8gHodUFfF4FkrRe5r4BaXWmZs"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


########################################################################################################################
def invia_file(call, nome_cdl, nome_file, is_triennale=1):
    bot.send_message(call.from_user.id, "Ecco l'orario per la " + ("triennale" if is_triennale else "magistrale") + " di " + nome_cdl + " che cercavi!")
    bot.send_chat_action(call.from_user.id, "upload_document")
    bot.send_document(call.from_user.id, open("./orario/file/" + nome_file, "rb"))
########################################################################################################################


# restituisce markup TRIENNALE - MAGISTRALE
def orario_1(message):
    bot.send_message(message.chat.id, "Qual è il tuo corso di laurea?", reply_markup=markup_orario_cc())


def callback_orario_cc_1(call):
    if call.data == "o_cc_tr":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dip())
    elif call.data == "o_cc_mg":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dip())


def callback_orario_cc_tr_1(call):
    match call.data:
        case "o_dip_tr_dei":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dei())
        case "o_dip_tr_dmmm":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dmmm())
        case "o_dip_tr_dicatech":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dicatech())
        case "o_dip_tr_dicar":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dicar())
        case "o_corsicomuni":
            bot.send_message(call.from_user.id, "Ecco l'orario per i corsi comuni che cercavi!")
            bot.send_chat_action(call.from_user.id, "upload_document")
            bot.send_document(call.from_user.id, open("./orario/file/corsi_comuni.pdf", "rb"))
            bot.delete_message(call.from_user.id, call.message.message_id)
        case "o_tr_dip_back":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_cc())


def callback_orario_cc_mg_1(call):
    match call.data:
        case "o_dip_mg_dei":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dei())
        case "o_dip_mg_dmmm":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dmmm())
        case "o_dip_mg_dicatech":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dicatech())
        case "o_dip_mg_dicar":
            bot.send_message(call.from_user.id, "**MANCANTE**")
            bot.delete_message(call.from_user.id, call.message.message_id)
        case "o_mg_dip_back":
            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_cc())


def callback_orario_tr_dei_1(call):
    if call.data == "o_tr_dei_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dip())
    else:
        match call.data:
            case "o_dei_tr_tlc":
                invia_file(call, "Elettronica e delle Telecomunicazioni", "elettronica_tlc_TR.pdf")
            case "o_dei_tr_eta":
                invia_file(call, "Elettrica", "elettrica_TR.pdf")
            case "o_dei_tr_inf":
                invia_file(call, "Informatica e Automazione", "info_auto_TR.pdf")
            case "o_dei_tr_sm":
                invia_file(call, "Sistemi Medicali", "sistemi_medicali_TR.pdf")
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_tr_dmmm_1(call):
    if call.data == "o_tr_dmmm_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dip())
    else:
        match call.data:
            case "o_dmmm_tr_ges":
                invia_file(call, "Gestionale", "gestionale_TR.pdf")
            case "o_dmmm_tr_mec":
                invia_file(call, "Meccanica", "meccanica_TR.pdf")
            case "o_dmmm_tr_aero":
                invia_file(call, "Sistemi Aerospaziali", "sis_aerospaziali_TR.pdf")
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_tr_dicatech_1(call):
    if call.data == "o_tr_dicatech_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dip())
    else:
        match call.data:
            case "o_dicatech_tr_cost":
                invia_file(call, "Costruzione e Gestione Ambientale e Territoriale", "costruzione_ambientale_TR.pdf")
            case "o_dicatech_tr_edi":
                invia_file(call, "Edile", "edile_TR.pdf")
            case "o_dicatech_tr_cic":
                invia_file(call, "Civile e Ambientale", "civile_ambientale_TR.pdf")
            case "o_dicatech_tr_cic_ta":
                invia_file(call, "Civile e Ambientale (TA)", "civile_ambientale_TA_TR.pdf")
            case "o_dicatech_tr_amb":
                bot.send_message(call.from_user.id, "**MANCANTE**")
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_tr_dicar_1(call):
    if call.data == "o_tr_dicar_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_tr_dip())
    else:
        match call.data:
            case "o_dicar_tr_arch":
                bot.send_message(call.from_user.id, "Ecco l'orario per il cdl in Architettura che cercavi!")
                bot.send_chat_action(call.from_user.id, "upload_document")
                bot.send_document(call.from_user.id, open("file/architettura.pdf", "rb"))
                bot.delete_message(call.from_user.id, call.message.message_id)
            case "o_dicar_tr_disindu":
                bot.send_message(call.from_user.id, "Ecco l'orario per il cdl in Disegno Industriale che cercavi!")
                bot.send_chat_action(call.from_user.id, "upload_document")
                bot.send_document(call.from_user.id, open("file/disegno_industriale.pdf", "rb"))
                bot.delete_message(call.from_user.id, call.message.message_id)
            case "o_dicar_tr_inddesign":
                bot.send_message(call.from_user.id, "Ecco l'orario per il cdl in Industrial Design che cercavi!")
                bot.send_chat_action(call.from_user.id, "upload_document")
                bot.send_document(call.from_user.id, open("file/industrial_design.pdf", "rb"))
                bot.delete_message(call.from_user.id, call.message.message_id)
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_mg_dei_1(call):
    if call.data == "o_mg_dei_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dip())
    else:
        match call.data:
            case "o_dei_mg_eto":
                invia_file(call, "Elettronica", "elettronica_MG.pdf", 0)
            case "o_dei_mg_eta":
                invia_file(call, "Elettrica", "elettrica_MG.pdf", 0)
            case "o_dei_mg_auto":
                invia_file(call, "Automazione", "automazione_MG.pdf", 0)
            case "o_dei_mg_tlc":
                invia_file(call, "Telecomunicazioni", "tlc_MG.pdf", 0)
            case "o_dei_mg_inf":
                invia_file(call, "Informatica", "informatica_MG.pdf", 0)
            case "o_dei_mg_sm":
                invia_file(call, "Sistemi Medicali", "sistemi_medicali_MG.pdf", 0)
            case "o_dei_mg_trdig":
                bot.send_message(call.from_user.id, "**MANCANTE**")
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_mg_dmmm_1(call):
    if call.data == "o_mg_dmmm_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dip())
    else:
        match call.data:
            case "o_dmmm_mg_ene":
                invia_file(call, "Energetica", "energetica_MG.pdf", 0)
            case "o_dmmm_mg_mec":
                invia_file(call, "Meccanica", "meccanica_MG.pdf", 0)
            case "o_dmmm_mg_mec_ta":
                invia_file(call, "Meccanica (TA)", "meccanica_TA_MG.pdf", 0)
            case "o_dmmm_mg_mecen":
                invia_file(call, "Mechanical Engineering", "mech_eng_MG.pdf", 0)
            case "o_dmmm_mg_ges":
                invia_file(call, "Gestionale", "gestionale_MG.pdf", 0)
        bot.delete_message(call.from_user.id, call.message.message_id)


def callback_orario_mg_dicatech_1(call):
    if call.data == "o_mg_dicatech_back":
        bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=markup_orario_mg_dip())
    else:
        match call.data:
            case "o_dicatech_mg_civ":
                invia_file(call, "Civile", "civile_MG.pdf", 0)
            case "o_dicatech_mg_sised":
                invia_file(call, "Sistemi Edilizi", "sistemi_edilizi_MG.pdf", 0)
            case "o_dicatech_mg_amb":
                invia_file(call, "Ambiente e Territorio", "amb_terr_MG.pdf", 0)
            case "o_dicatech_mg_amb_ta":
                invia_file(call, "Ambiente e Territorio (TA)", "amb_terr_TA_MG.pdf", 0)
            case "o_dicatech_mg_infrciv":
                invia_file(call, "Gestione Infrastrutture Civili", "infrastr_civ_MG.pdf", 0)
        bot.delete_message(call.from_user.id, call.message.message_id)
