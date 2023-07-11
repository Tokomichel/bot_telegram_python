from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# API github
import github

TOKEN: Final = "6363168168:AAF4XlvuQQ3IGYp7hj1ap754alS_HATyk80"
BOT_USERNAME: Final = "@Giteye_bot"


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Pourquoi ca ne lance meme pas la fonction ci?")
    await update.message.reply_text("Hello! Thanks for chatting me i'm a bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sure i'm a bot but my development is on processing so I surely be able to help you next time")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


# Handle responses

def handle_response(text: str) -> str:
    lower = text.lower()
    
    if 'hello' in lower:
        return "Hello nice to meet you"
    else:
        return "I don't understand what you said"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f" User {update.message.chat.id} in {message_type} : {text}")
    
    if message_type == 'group':
        
        if BOT_USERNAME in text:
            user_name: str = text.replace(BOT_USERNAME, "").replace(" ", "").strip()
            user_data = github.get_github_user(user_name)
        else:
            return
    else:
        response: str = handle_response(text)
    
    response = user_data['login'] + "\n" +  user_data['name'] + "\n" +  user_data['location'] + "\n" + user_data['bio'] + "\nRepository: "
    list_repos = github.get_repos_list(user_data['repos_url'])
    
    # response += ["\n" + str(elt) for elt in list_repos ]
    
    for i in range(len(list_repos)):
        response += "\n -" + list_repos[i]
    
    print("Bot", response)
    await update.message.reply_text(response) 

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.error)
    
    

if __name__ == "__main__":
    
    print("Lancement du bot")
    
    # commands
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    
    # message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    #Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)