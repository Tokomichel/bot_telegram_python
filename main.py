from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from TOKEN import TOKEN as tk
# API github
import github

TOKEN: Final = tk
BOT_USERNAME: Final = "@Giteye_bot"
STACKS: Final = """Nos stack Front Web tourne autour de :
 -React js 
 -Next js : pour les projets a courtes dures
 -Vue js 

 Nos  stack back :
 - Node js  + express
 - Spring boot
 - Adonis js
 - Django + Flask

Nos stack Mobile :
 - Flutter
 - React Native
 - Kotlin : optionnel
 -Swift : optionnel 

Nos stack DevOps :
  -Docker
  - Kubernetes

Nos  stack Management de projet
  -  Agile + scrum

Nos stack coté cloud:
  - Aws
 - Google cloud
 - Azure cloud"""


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Pourquoi ca ne lance meme pas la fonction ci?")
    await update.message.reply_text("Hello! Thanks for chatting me i'm a bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sure I'm a bot but my development is on processing so I surely be able to help you next time")

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
   
#Bussiness functions

def get_user(user_name: str):
        
        response = ""
        
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

        return response

# Handle responses

def handle_response(text: str) -> str:
    lower = text.lower()

    if 'hello' in lower:
        return "Hello nice to meet you"
    else:
        return "I don't understand what you said"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message_type: str = update.message.chat.type
    print(update.message.text)
    print(f"Type: {message_type}, Message: {update.message.text}")


    new_text: str = update.message.text.replace(BOT_USERNAME, "").strip()
        
    if new_text == "remind":
        await update.message.reply_text(STACKS)
    await update.message.reply_text("Taguer moi et passer le code requis")

    # if message_type == "group":
    #     if BOT_USERNAME in update.message.text:
    #         new_text: str = update.message.text.replace(BOT_USERNAME, "").strip()

    #         if new_text == "remind":
    #             await update.message.reply_text(STACKS)

    #         await update.message.reply_text("Taguer moi et passer le code requis")
    # else:
    #     user_name: str = update.message.chat.username
    #     await update.message.reply_text(f"Hi {user_name} nice to meet you")  

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.error)
    
    
if __name__ == "__main__":
    
    print("Lancement du bot") # adding some shit words to my code
    
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