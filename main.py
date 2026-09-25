import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://www.skai.gr", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Διαβάστε", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Διαβάστε τώρα", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Διαβάστε τώρα", url="https://www.skai.gr")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📰 *Καλώς ήρθατε στα Καθημερινά Θέματα.*\n\n"
        "Κάθε μέρα μια επιλογή από πολιτισμό, ταξίδια, "
        "κουζίνα, επιστήμη και τεχνολογία, για ανάγνωση "
        "με ηρεμία στο chat.\n\n"
        "Για να ξεκινήσετε, πατήστε *Τα θέματα της ημέρας*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Πολιτισμός — εκθέσεις φθινοπώρου", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Κουζίνα — συνταγές με κυδώνι", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Ταξίδια — πέντε χωριά", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📋 *Τα θέματα της ημέρας*\n\n"
        "Τρία κείμενα επιλεγμένα για σήμερα. "
        "Κάθε ένα ολόκληρο στο chat.\n\n"
        "*Πολιτισμός* — εκθέσεις φθινοπώρου: "
        "πέντε ραντεβού στα ελληνικά μουσεία.\n\n"
        "*Κουζίνα* — η εποχή του κυδωνιού: "
        "τέσσερις κλασικές συνταγές.\n\n"
        "*Ταξίδια* — πέντε ελληνικά χωριά "
        "για φθινοπωρινά Σαββατοκύριακα.\n\n"
        "Πατήστε έναν τίτλο για το πλήρες κείμενο.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("🎨 *Εκθέσεις φθινοπώρου: πέντε ραντεβού στα ελληνικά μουσεία*\n\n"
        "Τα μουσεία ανοίγουν ξανά με νέα σεζόν.\n\n"
        "*Αθήνα — τέχνη του 20ού αιώνα*\n"
        "Μια μεγάλη αναδρομική στην Εθνική Πινακοθήκη "
        "συγκεντρώνει έργα κορυφαίων Ελλήνων ζωγράφων. "
        "Αρχειακό υλικό και αδημοσίευτες φωτογραφίες.\n\n"
        "*Θεσσαλονίκη — βυζαντινή κληρονομιά*\n"
        "Το Μουσείο Βυζαντινού Πολιτισμού παρουσιάζει "
        "ψηφιδωτά και εικόνες. Μοναδική ευκαιρία.\n\n"
        "*Ηράκλειο — μινωικός πολιτισμός*\n"
        "Νέα ευρήματα από τις ανασκαφές στην Κνωσό "
        "εκτίθενται για πρώτη φορά.\n\n"
        "*Ναύπλιο — φωτογραφία νεοελληνικής ιστορίας*\n"
        "Ασπρόμαυρα ρεπορτάζ αφηγούνται την πόλη "
        "στα χρόνια της ανασυγκρότησης.\n\n"
        "*Ιωάννινα — σύγχρονη γλυπτική*\n"
        "Νέες εγκαταστάσεις στους υπαίθριους χώρους "
        "δίπλα στη λίμνη.\n\n"
        "_Ημερομηνίες στους ιστότοπους των μουσείων._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("🍳 *Η εποχή του κυδωνιού: τέσσερις κλασικές συνταγές*\n\n"
        "*Κυδώνι ψητό στον φούρνο*\n"
        "Κόβετε τα κυδώνια στα τέσσερα, βάζετε "
        "ζάχαρη, κανέλα και γαρίφαλο. Ψήνετε "
        "στους 180 για μία ώρα.\n\n"
        "*Κυδωνόπαστο*\n"
        "Βράζετε τα κυδώνια, πολτοποιείτε "
        "με ζάχαρη και χυμό λεμονιού. "
        "Το κλασικό γλυκό κουταλιού.\n\n"
        "*Κυδώνι με κρέας*\n"
        "Μοσχάρι κοκκινιστό με κυδώνια. "
        "Κρεμμύδι, ντομάτα, κανέλα — "
        "σιγοβράζει για δύο ώρες.\n\n"
        "*Μαρμελάδα κυδώνι*\n"
        "Κυδώνια τριμμένα με ζάχαρη και βανίλια. "
        "Ιδανική για πρωινό με ψωμί.\n\n"
        "_Δοσολογίες κατά βούληση._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("🏠 *Πέντε ελληνικά χωριά για το φθινόπωρο*\n\n"
        "*Ζαγοροχώρια (Ήπειρος)*\n"
        "Πέτρινα γεφύρια, μονοπάτια και "
        "παραδοσιακοί ξενώνες.\n\n"
        "*Δημητσάνα (Πελοπόννησος)*\n"
        "Χτισμένη πάνω από το φαράγγι του Λούσιου. "
        "Μουσείο Υδροκίνησης και ήσυχα καφενεία.\n\n"
        "*Μέτσοβο (Ήπειρος)*\n"
        "Ορεινό κεφαλοχώρι με τυροκομικά "
        "και κρασιά. Ιδιαίτερη ατμόσφαιρα.\n\n"
        "*Μονεμβασιά (Πελοπόννησος)*\n"
        "Βυζαντινή καστροπολιτεία κρυμμένη "
        "πίσω από τον βράχο. Μαγεία.\n\n"
        "*Νυμφαίο (Μακεδονία)*\n"
        "Αρχοντικά, το καταφύγιο αρκούδων "
        "και απόλυτη ησυχία.\n\n"
        "_Κράτηση εντός εβδομάδας._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Γλωσσάριο", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Συχνές ερωτήσεις", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Πληροφορίες", callback_data="about"))
    text = ("🏛 *Περίληψη*\n\n"
        "Από αυτό το μενού μπορείτε:\n\n"
        "• Να διαβάσετε *τα θέματα της ημέρας*.\n"
        "• Να δείτε τις στήλες: Πολιτισμός, "
        "Ταξίδια, Κουζίνα, Επιστήμη.\n"
        "• Να δείτε το γλωσσάριο και τις "
        "συχνές ερωτήσεις.\n"
        "• Να μάθετε για εμάς και να επικοινωνήσετε.\n\n"
        "Για πλήρη έκδοση, πατήστε το κουμπί.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📖 *Μικρό γλωσσάριο*\n\n"
        "*Σύνταξη* — η ομάδα που επιλέγει "
        "και προετοιμάζει τα κείμενα.\n\n"
        "*Κύριο άρθρο* — άρθρο γνώμης που "
        "ανοίγει μια ενότητα.\n\n"
        "*Φωτορεπορτάζ* — κείμενο χτισμένο "
        "γύρω από φωτογραφίες.\n\n"
        "*Διαχρονικό περιεχόμενο* — κείμενο "
        "που δεν εξαρτάται από την επικαιρότητα.\n\n"
        "*Στήλη* — μόνιμη ενότητα αφιερωμένη "
        "σε ένα θέμα.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("❓ *Συχνές ερωτήσεις*\n\n"
        "*Είναι επίσημο αυτό το bot;*\n"
        "Τα Καθημερινά Θέματα είναι ανεξάρτητο "
        "εκδοτικό εγχείρημα.\n\n"
        "*Πόσο συχνά ενημερώνεται;*\n"
        "Η επιλογή ανανεώνεται εποχιακά.\n\n"
        "*Πώς σιγάζω τις ειδοποιήσεις;*\n"
        "Από τις ρυθμίσεις του chat στο Telegram.\n\n"
        "*Μπορώ να μοιραστώ άρθρο;*\n"
        "Ναι, μέσω των επιλογών κοινής χρήσης "
        "του Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Πληροφορίες", callback_data="about"))
    text = ("✏️ *Επικοινωνία*\n\n"
        "Για εκδοτική αλληλογραφία:\n"
        "• E-mail: info@kathimerinathemata.gr\n\n"
        "*Εκδότης*\n"
        "Καθημερινά Θέματα\n"
        "Αθήνα, Ελλάδα\n\n"
        "Παρατηρήσεις και σχόλια αναγνωστών "
        "τις εργάσιμες ημέρες.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact"))
    text = ("🏛 *Πληροφορίες για τα Καθημερινά Θέματα*\n\n"
        "Τα Καθημερινά Θέματα είναι ένα ανεξάρτητο "
        "εκδοτικό εγχείρημα αφιερωμένο στον πολιτισμό, "
        "τα ταξίδια, την κουζίνα και την τεχνολογία.\n\n"
        "Η σύνταξη επιλέγει κάθε μέρα περιεχόμενο "
        "για μια ενημερωμένη παύση από την καθημερινότητα.\n\n"
        "Αυτή η έκδοση Telegram σχεδιάστηκε για "
        "άνετη ανάγνωση μέσα από το chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Τα θέματα της ημέρας", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Καλώς ήρθατε! Πατήστε *Τα θέματα της ημέρας* για να ξεκινήσετε.", parse_mode="Markdown", reply_markup=markup)


print("Daily Topics Greece Bot is running...")
bot.infinity_polling()
