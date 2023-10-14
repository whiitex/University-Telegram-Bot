from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# FUNCTIONS INLINE BUTTONS - 'ORARIO'
def markup_orario_cc():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
            InlineKeyboardButton("Triennale", callback_data="o_cc_tr"),
            InlineKeyboardButton("Magistrale", callback_data="o_cc_mg"))
    return markup


def markup_orario_cc_data():
    return ["o_cc_tr", "o_cc_mg"]


########################################################################################################################
########################################################################################################################
def markup_orario_tr_dip():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("DEI", callback_data="o_dip_tr_dei"),
        InlineKeyboardButton("DMMM", callback_data="o_dip_tr_dmmm"),
        InlineKeyboardButton("DICATECh", callback_data="o_dip_tr_dicatech"),
        InlineKeyboardButton("DICAR", callback_data="o_dip_tr_dicar"),
        InlineKeyboardButton("Corsi Comuni", callback_data="o_corsicomuni"),
        InlineKeyboardButton("🔙 back", callback_data="o_tr_dip_back"))
    return markup


def markup_orario_cc_tr_data():
    return ["o_dip_tr_dei", "o_dip_tr_dmmm", "o_dip_tr_dicatech", "o_dip_tr_dicar", "o_corsicomuni", "o_tr_dip_back"]


########################################################################################################################
def markup_orario_mg_dip():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("DEI", callback_data="o_dip_mg_dei"),
        InlineKeyboardButton("DMMM", callback_data="o_dip_mg_dmmm"),
        InlineKeyboardButton("DICATECh", callback_data="o_dip_mg_dicatech"),
        #InlineKeyboardButton("DICAR", callback_data="o_dip_mg_dicar"),
        InlineKeyboardButton("🔙 back", callback_data="o_mg_dip_back"))
    return markup


def markup_orario_cc_mg_data():
    return ["o_dip_mg_dei", "o_dip_mg_dmmm", "o_dip_mg_dicatech", "o_dip_mg_dicar", "o_mg_dip_back"]


########################################################################################################################
########################################################################################################################
def markup_orario_tr_dei():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Elettronica e Telecomunicazioni", callback_data="o_dei_tr_tlc"),
        InlineKeyboardButton("Elettrica", callback_data="o_dei_tr_eta"),
        InlineKeyboardButton("Informatica e dell'Automazione", callback_data="o_dei_tr_inf"),
        InlineKeyboardButton("Sistemi Medicali", callback_data="o_dei_tr_sm"),
        InlineKeyboardButton("🔙 back", callback_data="o_tr_dei_back"))
    return markup


def markup_orario_tr_dei_data():
    return ["o_dei_tr_tlc", "o_dei_tr_eta", "o_dei_tr_inf", "o_dei_tr_sm", "o_tr_dei_back"]


########################################################################################################################
def markup_orario_tr_dmmm():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Gestionale", callback_data="o_dmmm_tr_ges"),
        InlineKeyboardButton("Meccanica", callback_data="o_dmmm_tr_mec"),
        InlineKeyboardButton("Sistemi Aerospaziali", callback_data="o_dmmm_tr_aero"),
        InlineKeyboardButton("🔙 back", callback_data="o_tr_dmmm_back"))
    return markup


def markup_orario_tr_dmmm_data():
    return ["o_dmmm_tr_ges", "o_dmmm_tr_mec", "o_dmmm_tr_aero", "o_tr_dmmm_back"]


########################################################################################################################
def markup_orario_tr_dicatech():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Costruzione e Gestione Ambientale", callback_data="o_dicatech_tr_cost"),
        InlineKeyboardButton("Edile", callback_data="o_dicatech_tr_edi"),
        InlineKeyboardButton("Civile e Ambientale", callback_data="o_dicatech_tr_cic"),
        InlineKeyboardButton("TA Civile e Ambientale", callback_data="o_dicatech_tr_cic_ta"),
        #InlineKeyboardButton("Ing. dell'Ambiente", callback_data="o_dicatech_tr_amb"),
        InlineKeyboardButton("🔙 back", callback_data="o_tr_dicatech_back"))
    return markup


def markup_orario_tr_dicatech_data():
    return ["o_dicatech_tr_cost", "o_dicatech_tr_edi", "o_dicatech_tr_cic", "o_dicatech_tr_amb", "o_dicatech_tr_cic_ta", "o_tr_dicatech_back"]


########################################################################################################################
def markup_orario_tr_dicar():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Architettura", callback_data="o_dicar_tr_arch"),
        InlineKeyboardButton("Disegno Industriale", callback_data="o_dicar_tr_disindu"),
        InlineKeyboardButton("Indstrial Design", callback_data="o_dicar_tr_inddesign"),
        InlineKeyboardButton("🔙 back", callback_data="o_tr_dicar_back"))
    return markup


def markup_orario_tr_dicar_data():
    return ["o_dicar_tr_arch", "o_dicar_tr_disindu", "o_dicar_tr_inddesign", "o_tr_dicar_back"]


########################################################################################################################
########################################################################################################################
def markup_orario_mg_dei():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Elettronica", callback_data="o_dei_mg_eto"),
        InlineKeyboardButton("Elettrica", callback_data="o_dei_mg_eta"),
        InlineKeyboardButton("Ing. dell'Automazione", callback_data="o_dei_mg_auto"),
        InlineKeyboardButton("Telecomunicazioni (EN)", callback_data="o_dei_mg_tlc"),
        InlineKeyboardButton("Informatica (EN)", callback_data="o_dei_mg_inf"),
        InlineKeyboardButton("Sistemi Medicali", callback_data="o_dei_mg_sm"),
        #InlineKeyboardButton("Trasformazione Digitale", callback_data="o_dei_mg_trdig"),
        InlineKeyboardButton("🔙 back", callback_data="o_mg_dei_back"))
    return markup


def markup_orario_mg_dei_data():
    return ["o_dei_mg_eto", "o_dei_mg_eta", "o_dei_mg_auto", "o_dei_mg_tlc", "o_dei_mg_inf", "o_dei_mg_sm", "o_dei_mg_trdig", "o_mg_dei_back"]


########################################################################################################################
def markup_orario_mg_dmmm():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Energetica", callback_data="o_dmmm_mg_ene"),
        InlineKeyboardButton("Meccanica", callback_data="o_dmmm_mg_mec"),
        InlineKeyboardButton("TA Meccanica", callback_data="o_dmmm_mg_mec_ta"),
        InlineKeyboardButton("Mechanical Engineering", callback_data="o_dmmm_mg_mecen"),
        InlineKeyboardButton("Gestionale", callback_data="o_dmmm_mg_ges"),
        InlineKeyboardButton("🔙 back", callback_data="o_mg_dmmm_back"))
    return markup


def markup_orario_mg_dmmm_data():
    return ["o_dmmm_mg_ene", "o_dmmm_mg_mec", "o_dmmm_mg_mec_ta", "o_dmmm_mg_mecen", "o_dmmm_mg_ges", "o_mg_dmmm_back"]


########################################################################################################################
def markup_orario_mg_dicatech():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("Civile", callback_data="o_dicatech_mg_civ"),
        InlineKeyboardButton("Sistemi Edilizi", callback_data="o_dicatech_mg_sised"),
        InlineKeyboardButton("Ambiente e Territorio", callback_data="o_dicatech_mg_amb"),
        InlineKeyboardButton("TA Ambiente e Territorio", callback_data="o_dicatech_mg_amb_ta"),
        InlineKeyboardButton("Gestione Infrastrutture Civili", callback_data="o_dicatech_mg_infrciv"),
        InlineKeyboardButton("🔙 back", callback_data="o_mg_dicatech_back"))
    return markup


def markup_orario_mg_dicatech_data():
    return ["o_dicatech_mg_civ", "o_dicatech_mg_sised", "o_dicatech_mg_amb", "o_dicatech_mg_amb_ta", "o_dicatech_mg_infrciv", "o_mg_dicatech_back"]


########################################################################################################################
########################################################################################################################
