from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from TOKEN import TOKEN as tk
# API github
import github

TOKEN: Final = tk
BOT_USERNAME: Final = "@Giteye_bot"


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Pourquoi ca ne lance meme pas la fonction ci?")
    await update.message.reply_text("Hello! Thanks for chatting me i'm a bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sure i'm a bot but my development is on processing so I surely be able to help you next time")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")

async def prince_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   message_type: str = update.message.chat.type
   
   
   if message_type == "group":
       print(f"Je reconnais quand meme que c'est un groupe {update.message.from_user.name}")
       await update.message.reply_text(f"Salut {update.message.from_user.name} comment tu vas?")
       if update.message.from_user.name == "Prince":
        print("Okay la ca a prit")   
        await update.message.reply_text("Salut Prainsseuh Mairvaye comment tu vas?")
   else:
       print("Ca n'a pas gui")
       return


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
    
    print(f" User {update.message.from_user.username} in {message_type} : {text}")
    

    if BOT_USERNAME in text:
        print("On m'a taguer")
        user_name: str = text.replace(BOT_USERNAME, "").replace(" ", "").strip()
        user_data = github.get_github_user(user_name)
        print("1")
        response = f"User name:   {user_data['login']} \n +  Name:   {user_data['name'] }\n +  Location: {user_data['location']} \n Description: {user_data['bio']}  \nRepository: "
        response = ""
        print("11")
        list_repos = github.get_repos_list(user_data['repos_url'])
        print("2")
    
        # response += ["\n" + str(elt) for elt in list_repos ]
    
        for i in range(len(list_repos)):
            response += "\n -" + list_repos[i]
    else:
        if(update.message.from_user.username == "sanguoledoux"):
            response = "Tes noyaux"
        elif(update.message.from_user.username == "KengniJohan"):
            response = "Enfin je retrouve mon ami robot😂😂"

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
    app.add_handler(CommandHandler("prince", prince_command))
    
    # message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    #Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)