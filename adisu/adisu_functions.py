import telebot
from telebot import formatting
from adisu.adisu_markup import *

TOKEN = "5887892548:AAGvwWOAY-8gHodUFfF4FkrRe5r4BaXWmZs"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


def adisu_1(message):
    bot.send_message(message.chat.id, "Di seguito una lista delle domande frequenti riguardanti la questione ADISU,"
                                      "clicca sul topic che ti interessa per saperne di più. Questa lista di domande è"
                                      " stata realizzata per uso personale. NON ci assumiamo la responsabilità di "
                                      "eventuali errori contenuti in questo file. ", reply_markup=markup_adisu())


def callback_adisu_quest_1(call):
    match call.data:

        # Importi borsa di studio
        case "a_bdsprimarata":
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("Importi prima rata"), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, "Come riportato nel Comma 3, dedicato alle integrazioni della borsa di studio: "
                             "\"Le integrazioni di borsa di studio saranno corrisposte congiuntamente alla seconda rata"
                             " di borsa di studio, fatta eccezione per il premio di laurea e l'integrazione per la mobilità internazionale\"")
            bot.send_chat_action(call.from_user.id, "upload_photo")
            bot.send_photo(call.from_user.id, open("./adisu/file/importi_prima_rata.png", "rb"))

        # Pendolare diventato "in sede"
        case "a_pendsede":
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("Sono uno studente pendolare, ma ho ricevuto la borsa "
                                                                 "da studente in sede, come posso risolvere?"), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, "Se risulti pendolare perché rientri in una delle seguenti casistiche, allora puoi stare"
                             " tranquillo/a, ti sarà erogata la differenza tra la borsa da pendolare e quella da in sede"
                             " con la liquidazione della seconda rata.\nA.\t\tHo richiesto il posto letto presso una "
                             "residenza A.Di.S.U. ma non ho provveduto a compilare l’istanza per l’accettazione "
                             "dell’alloggio.\nB.\t\tNon ho presentato il contratto di locazione o non ho compilato "
                             "l’istanza del contratto entro i termini previsti dal bando")

        # Rimborso alloggio
        case "a_rimballoggio":
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("Quando arriverà il rimborso di ~1900€ della trattenura"
                                                                 " alloggio?"), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, "Anzitutto vi ricordiamo che il rimborso dei 1900€ saranno erogati esclusivamente agli "
                             "idonei non assegnatari di posto letto che hanno presentato il contratto di locazione che "
                             "rispetti i requisiti previsti dal bando. Il rimborso sarà erogato più o meno nello stesso"
                             " periodo in cui sarà erogata la seconda rata.")

        # Rimborso tassa regionale
        case "a_rimbtassareg":
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("Quando arriverà il rimborso della tassa regionale?"), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, "Il rimborso della tassa regionale sarà erogato entro i termini riportati nell’art.19, "
                             "comma 3 del bando (pagina 54) di seguito riportato.\n" + formatting.hbold("\nN.B.\t\tSe sei uno studente laureato"
                            " nella sessione invernale o che si laurea entro aprile 2023 e hai pagato la T1, allora ti"
                            "saranno date indicazioni sulle modalità per richiedere il rimborso."), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "upload_photo")
            bot.send_photo(call.from_user.id, open("./adisu/file/rimborso_tassa_regionale.png", "rb"))

        # "beneficiario sospeso"
        case "a_bensospeso":
            mrkplink = InlineKeyboardMarkup()
            mrkplink.add(InlineKeyboardButton("Leggi l'articolo 📚", url="https://www.aup.it/a-di-su-puglia/4738-liquidazione-prima-rata-a-di-s-u"))
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("A me risulta \"beneficiario sospeso\" e non risulto nei "
                                                                 "file allegati nell'articolo AUP. Perché?"), parse_mode="html", reply_markup=mrkplink)
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, "Ci potrebbero essere diverse cause per le quali è riportata quella "
                             "dicitura e non risulti in nessuno dei file allegati all’articolo "
                             "pubblicato sul sito AUP. Potrebbe essere perché:"
                             "\n•\t\tSei una matricola e quindi l’A.Di.S.U. è in attesa del conseguimento "
                             "dei 20 CFU e non hai richiesto l’erogazione in due rate;\n•\t\tNon hai comunicato "
                             "l’IBAN o hai fornito un codice IBAN difforme rispetto alle indicazioni;\n•\t\tHai richiesto "
                             "la borsa con i CFU di inglese ma li hai convalidati tramite una certificazione "
                             "linguistica ottenuta al di fuori della carriera universitaria;\n•\t\tHai presentato"
                             " un’attestazione ISEE valida per le prestazioni per il diritto allo studio con"
                             " annotazioni da parte dell'Agenzia delle Entrate relative ad omissioni e/o difformità;\n•\t\tSiano"
                             " sottoposti ad accertamento sulla veridicità dei dati e delle informazioni "
                             "fornite tramite autocertificazione e, in particolare, dei requisiti di reddito e merito;")

        # Richiesta borsa in 2 rate
        case "a_borsa2rate":
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("Erogazione della borsa in due rate"), parse_mode="html")
            bot.send_chat_action(call.from_user.id, "typing")
            bot.send_message(call.from_user.id, formatting.hbold("•\tSe sei uno studente del primo anno (triennale o magistrale)") + "\n\tTi consigliamo di contattare direttamente l’A.Di.S.U."
                              " Puglia tramite ticket oppure telefonicamente al numero 080 968 2000 oppure di recarti presso"
                              " gli uffici in Via Giustino Fortunato, 4/g, 70125 Bari BA perché potrebbe esserci"
                              " stato un errore (N.B. la dicitura “Beneficiario Sospeso” appare a tutte le "
                              "matricole poiché l’A.Di.S.U. attende il conseguimento dei 20 CFU).\n" + formatting.hbold("•\tSe sei uno "
                              "studente di anni successivi (NON FUORI CORSO)") + "\n\tTi consigliamo di contattare direttamente "
                              "l’A.Di.S.U. Puglia tramite ticket oppure telefonicamente al numero 080 968 2000 oppure "
                              "di recarti presso gli uffici in Via Giustino Fortunato, 4/g, 70125 Bari BA perché potrebbe esserci stato un errore.\n" +
                              formatting.hbold("•\tSe sei uno studente fuori corso") + "\n\tL’erogazione avverrà entro i "
                              "termini riportati nell’art. 6, comma 2 del bando (pagina 17).", parse_mode="html")
            bot.send_chat_action(call.from_user.id, "upload_photo")
            bot.send_photo(call.from_user.id, open("./adisu/file/fuori_corso_borsa2rate.png", "rb"))

        # Chiedi a noi - Supporto
        case "a_link":
            links = InlineKeyboardMarkup()
            links.row_width = 2
            links.add(
                InlineKeyboardButton("Canale Telegram", url="https://t.me/adisuinforma"),
                InlineKeyboardButton("Gruppo Discussione", url="https://t.me/+cXHlqGie7uQ2ZGZk")
            )
            bot.send_message(call.from_user.id, "Entra nei gruppi dedicati per trovare risposta ad eventuali dubbi.", reply_markup=links)

    bot.delete_message(call.from_user.id, call.message.message_id)
