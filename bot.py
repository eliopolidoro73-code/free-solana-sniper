import os
from telegram.ext import Updater, CommandHandler, CallbackContext

# Remplace par ton token BotFather
TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN n'est pas défini.")

# Fonction de démarrage
def start(update, context: CallbackContext):
    update.message.reply_text("Bienvenue sur FreeSolanaSniper !\n"
                              "Options : /signals, /snipe [contract_address]",
                              reply_markup={'inline_keyboard': [[{'text': 'Voir signaux', 'callback_data': 'signals'}],
                                                               [{'text': 'Sniper un token', 'callback_data': 'snipe'}]]})

# Liste des signaux (exemple)
def signals(update, context: CallbackContext):
    update.message.reply_text("Signaux Solana chauds :\n- Token1: 7xKX...\n- Token2: 9yLM...")

# Snipe un token (ajustement : vérification basique sans API fictive)
def snipe(update, context: CallbackContext):
    if len(context.args) != 1:
        update.message.reply_text("Usage : /snipe [contract_address]")
        return
    address = context.args[0]
    update.message.reply_text(f"Vérification de {address} en cours... (API non connectée)")

def button(update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'signals':
        signals(query.message, context)
    elif query.data == 'snipe':
        query.message.reply_text("Utilise /snipe [contract_address] pour sniper un token.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signals", signals))
    dp.add_handler(CommandHandler("snipe", snipe))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()