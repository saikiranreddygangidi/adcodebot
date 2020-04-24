import nltk
import telebot
from flask import Flask, request
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
API_TOKEN = '1095762894:AAH1y_gd31l3qimubyq0fYFNRYkeTPi-HCI'
            
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)
PORT = int(os.environ.get('PORT', '8443'))                
            
  # Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message, "\nHi there, I am codeBot.\nI am here display code for you. Just send codename  and I'll display the code to you!\n if you want any help type/help command")

@bot.message_handler(commands=['help'])
def help(message):
 bot.reply_to(message,"""
      '/search' 
     command to search code.""")
@bot.message_handler(commands=['search'])
def search(message):
 tid = str(message.from_user.id)
 msg=bot.send_message(tid,"Enter program name")
 bot.register_next_step_handler(msg, codename)

def codename(message):
 c_name = message.text
 bot.reply_to(message,"hibady,"+c_name)
                        
            
  # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
 bot.reply_to(message, 'if you want search code please enter "\search" command ')
                   
@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
  bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
  return "!", 200
  
  
@server.route("/")
def webhook():
  bot.remove_webhook()
  bot.set_webhook(url='https://adcodebot.herokuapp.com/' + API_TOKEN)
  return "!", 200
  
  
if __name__ == "__main__":
  server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))