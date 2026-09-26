import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://vanishvili93-jpg.github.io/tg-webapp/sw.html", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Lesen", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Jetzt lesen", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Jetzt lesen", url="https://vanishvili93-jpg.github.io/tg-webapp/sw.html")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("📰 *Willkommen bei Tagesblick.*\n\n"
        "Jeden Tag eine Auswahl aus Kultur, Reisen, "
        "Kueche, Wissenschaft und Technologie — "
        "zum Lesen in Ruhe im Chat.\n\n"
        "Tippen Sie auf *Themen des Tages* "
        "um zu beginnen.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Kultur — Herbstausstellungen", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Kueche — Schweizer Rezepte", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Reisen — fuenf Doerfer", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("📋 *Themen des Tages*\n\n"
        "Drei Beitraege fuer heute. "
        "Jeder vollstaendig im Chat.\n\n"
        "*Kultur* — Herbstausstellungen: fuenf "
        "Termine in Schweizer Museen.\n\n"
        "*Kueche* — Schweizer Klassiker: vier "
        "traditionelle Rezepte.\n\n"
        "*Reisen* — fuenf Schweizer Doerfer "
        "fuer ein Herbstwochenende.\n\n"
        "Tippen Sie auf einen Titel.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("🎨 *Herbstausstellungen: fuenf Termine "
        "in Schweizer Museen*\n\n"
        "Die Museen starten in die neue Saison.\n\n"
        "*Zuerich — Kunsthaus*\n"
        "Eine grosse Retrospektive vereint Werke "
        "der bedeutendsten Schweizer Maler des "
        "letzten Jahrhunderts. Archivmaterial "
        "und unveroffentlichte Fotografien.\n\n"
        "*Basel — Fondation Beyeler*\n"
        "Impressionismus und Moderne in einem "
        "neuen Dialog. Restaurierte Meisterwerke "
        "mit bisher unsichtbaren Details.\n\n"
        "*Bern — Zentrum Paul Klee*\n"
        "Zeichnungen und Skizzen von Paul Klee "
        "neben zeitgenoessischen Arbeiten. "
        "Eine seltene Gelegenheit.\n\n"
        "*Luzern — Verkehrshaus*\n"
        "Neue interaktive Ausstellung ueber "
        "die Zukunft der Mobilitaet. "
        "Fuer Familien besonders geeignet.\n\n"
        "*Genf — MAMCO*\n"
        "Zeitgenoessische Kunst aus der Schweiz "
        "und Europa. Installationen und Video "
        "im Dialog mit der Sammlung.\n\n"
        "_Oeffnungszeiten auf den Museumswebsites._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("🍳 *Schweizer Klassiker: vier "
        "traditionelle Rezepte*\n\n"
        "*Kaesefondues*\n"
        "Gruyere und Vacherin, Weisswein, "
        "Knoblauch und Kirschwasser. Langsam "
        "schmelzen lassen und mit Brot geniessen. "
        "Der Schweizer Klassiker schlechthin.\n\n"
        "*Roesti*\n"
        "Gekochte Kartoffeln, gerieben und in "
        "Butter goldbraun gebraten. Einfach, "
        "knusprig und perfekt als Beilage "
        "oder Hauptgericht.\n\n"
        "*Zuercher Geschnetzeltes*\n"
        "Kalbfleisch in Rahmsauce mit Champignons. "
        "Dazu Roesti. Ein Zuercher Original "
        "das in zwanzig Minuten fertig ist.\n\n"
        "*Buendner Nusstorte*\n"
        "Muerbe Teigschale gefuellt mit "
        "karamellisierten Walnuessen und Rahm. "
        "Das suesse Souvenir aus Graubuenden.\n\n"
        "_Mengen und Zeiten nach Geschmack._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("🏠 *Fuenf Schweizer Doerfer "
        "fuer den Herbst*\n\n"
        "*Gruyeres (Fribourg)*\n"
        "Mittelalterliches Staedtchen mit Schloss "
        "und Kaeserei. Die Herbstfarben machen "
        "den Spaziergang unvergesslich.\n\n"
        "*Morcote (Tessin)*\n"
        "Am Ufer des Luganersees. Arkaden, "
        "Zypressen und eine Kirche mit "
        "Panoramablick. Mediterranes Flair.\n\n"
        "*Guarda (Graubuenden)*\n"
        "Engadiner Dorf mit Sgraffiti-Haeusern. "
        "Wanderwege, Stille und das Licht "
        "der Berge.\n\n"
        "*Stein am Rhein (Schaffhausen)*\n"
        "Bemalte Fassaden am Rheinufer. "
        "Kloster, Altstadt und ein Flussufer "
        "das zum Verweilen einlaedt.\n\n"
        "*Iseltwald (Bern)*\n"
        "Kleines Dorf am Brienzersee. "
        "Tuerkisblaues Wasser, Holzhaeuser "
        "und absolute Ruhe.\n\n"
        "_Unterkunft vorab buchen._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossar", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Haeufige Fragen", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Ueber uns", callback_data="about"))
    text = ("🏛 *Zusammenfassung*\n\n"
        "Von diesem Menu aus koennen Sie:\n\n"
        "• Die *Themen des Tages* lesen.\n"
        "• Rubriken durchblaettern: Kultur, "
        "Reisen, Kueche, Wissenschaft.\n"
        "• Glossar und haeufige Fragen ansehen.\n"
        "• Ueber uns erfahren und Kontakt aufnehmen.\n\n"
        "Fuer die vollstaendige Ausgabe "
        "nutzen Sie die Schaltflaeche.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("📖 *Kleines Glossar*\n\n"
        "*Redaktion* — das Team, das Texte "
        "auswaehlt und vorbereitet.\n\n"
        "*Leitartikel* — Meinungsbeitrag, "
        "der eine Rubrik eroeffnet.\n\n"
        "*Fotoreportage* — Bericht, aufgebaut "
        "auf einer Fotoserie.\n\n"
        "*Zeitloser Inhalt* — Text, dessen "
        "Aktualitaet nicht von der Tagesnachricht "
        "abhaengt.\n\n"
        "*Korrespondent* — Journalist, der "
        "vor Ort berichtet.\n\n"
        "*Rubrik* — feste Spalte zu einem "
        "bestimmten Thema.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"))
    text = ("❓ *Haeufige Fragen*\n\n"
        "*Ist dieser Bot offiziell?*\n"
        "Tagesblick ist ein unabhaengiges "
        "redaktionelles Projekt.\n\n"
        "*Wie oft wird aktualisiert?*\n"
        "Die Auswahl wird saisonweise erneuert.\n\n"
        "*Wie schalte ich Benachrichtigungen aus?*\n"
        "In den Telegram-Chat-Einstellungen.\n\n"
        "*Kann ich einen Artikel teilen?*\n"
        "Ja, ueber die Telegram-Teilfunktion.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Ueber uns", callback_data="about"))
    text = ("✏️ *Kontakt*\n\n"
        "Fuer redaktionelle Anfragen:\n"
        "• E-Mail: redaktion@tagesblick.ch\n\n"
        "*Herausgeber*\n"
        "Tagesblick GmbH\n"
        "Bahnhofstrasse 42\n"
        "8001 Zuerich\n"
        "Schweiz\n\n"
        "Leserhinweise an Werktagen.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Zusammenfassung", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Kontakt", callback_data="contact"))
    text = ("🏛 *Ueber Tagesblick*\n\n"
        "Tagesblick ist ein unabhaengiges "
        "redaktionelles Projekt fuer Kultur, "
        "Reisen, Kueche und Technologie.\n\n"
        "Die Redaktion waehlt taeglich "
        "hochwertige Inhalte fuer eine "
        "informierte Pause vom Alltag.\n\n"
        "Diese Telegram-Ausgabe ist fuer "
        "bequemes Lesen im Chat gedacht.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Themen des Tages", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Willkommen! Tippen Sie auf *Themen des Tages* um zu beginnen.", parse_mode="Markdown", reply_markup=markup)


print("Tagesblick Bot is running...")
bot.infinity_polling()
