from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# API github
import github

import bd
import user
import const

def loadList():
    const.USERS = bd.get()

def setList():
    bd.put(const.USERS)

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
        print("Okay la ca a donner")   
        await update.message.reply_text("Salut Prainsseuh Mairvaye comment tu vas?")
   else:
       print("Ca n'a pas gui")
       return

async def repos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loadList()
    
    for i in range(len(const.USERS)):
        if const.USERS[i].user_name == update.message.from_user.username:
            await update.message.chat.send_message("Choisissez le repos entrez un nombre")
            const.IS_REPOS = True
            const.INDEX = i
            return
        
    await update.message.reply_text("Veuillez passer par la premiere etape")
    
    
    
        
    # else:
    #     IS_REPOS = False

async def doc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_message("""Ce bot vous donne des stats assez utiles sur un compte Github de votre choix.

PROCESS
- Taguez le bot et dans le même message mettez y votre nom d'utilisateur de votre compte Github : comme ceci "@Giteyebot <user_name>"
- En suite, entrez la commande "/bot". Le bot vas vous demander de choisir le repos pour lequel vous voulez avoir plus de précision vous le choisissez selon l'ordre afficher dans les premières stats")
""")
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
    
    if const.IS_REPOS == True:
        j = int(update.message.text)
        print(const.USERS[const.INDEX])
        lag = github.get_lang_list(const.USERS[const.INDEX].r_data[j]['languages_url'])
        print(lag)
        await update.message.chat.send_message("Veuillez e")
        const.IS_REPOS = False
        return
        
            
    if message_type == 'group':
        # 
        if const.BOT_USERNAME in text:
            print("On m'a taguer")
            user_name: str = text.replace(const.BOT_USERNAME, "").replace(" ", "").strip()
            user_data = github.get_github_user(user_name)
            print("1")
            response = f"User name:  {user_data['login']}  \nName:  {user_data['name'] } \nLocation: {user_data['location']} \nDescription: {user_data['bio']}  \nRepository: "
            print("11")
            list_repos = github.get_repos_list(user_data['repos_url'])
            le = []
            [le.append(list_repos[i]['name']) for i in range(len(list_repos))]
            print("2")

            const.USERS.append(user.User(update.message.from_user.username, user_data, list_repos))
            setList()
            loadList()
            # response += ["\n" + str(elt) for elt in list_repos ]
    
            for i in range(len(le)):
                response += "\n -" + le[i]
        else:
            if(update.message.from_user.username == "sanguoledoux"):
                response = "Tes noyaux"
            elif(update.message.from_user.username == "KengniJohan"):
                response = "Enfin je retrouve mon ami robot😂😂"
        det = int(update.message.text) #verifier
        loadList()
        rep = const.USERS[det]
        lang = github.get_lang_list(rep['languages_url'])
        print(lang)        
    else:
        response: str = handle_response(text)
     
    

    
    print("Bot", response)
    await update.message.reply_text(response) 
    const.IS_REPOS = True

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.error)
    
    
if __name__ == "__main__":
    
    print("Lancement du bot")
    loadList()
     
    
    # commands
    app = Application.builder().token(const.TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("prince", prince_command))
    app.add_handler(CommandHandler("repos", repos_command))
    app.add_handler(CommandHandler("doc", doc_command))
    
    # message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    #Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3)