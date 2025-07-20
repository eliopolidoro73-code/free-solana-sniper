import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Remplace par ton token BotFather
TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN n'est pas défini.")

# Fonction de démarrage
async def start(update, context):
    await update.message.reply_text("Bienvenue sur FreeSolanaSniper !\n"
                                   "Options : /signals, /snipe [contract_address]",
                                   reply_markup={'inline_keyboard': [[{'text': 'Voir signaux', 'callback_data': 'signals'}],
                                                                    [{'text': 'Sniper un token', 'callback_data': 'snipe'}]]})

# Liste des signaux (exemple)
async def signals(update, context):
    await update.message.reply_text("Signaux Solana chauds :\n- Token1: 7xKX...\n- Token2: 9yLM...")

# Snipe un token (ajustement : vérification basique sans API fictive)
async def snipe(update, context):
    if len(context.args) != 1:
        await update.message.reply_text("Usage : /snipe [contract_address]")
        return
    address = context.args[0]
    await update.message.reply_text(f"Vérification de {address} en cours... (API non connectée)")

async def button(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == 'signals':
        await signals(update, context)
    elif query.data == 'snipe':
        await query.message.reply_text("Utilise /snipe [contract_address] pour sniper un token.")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signals", signals))
    application.add_handler(CommandHandler("snipe", snipe))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()