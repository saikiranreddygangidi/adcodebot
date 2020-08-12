import nltk
import telebot
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from flask import Flask, request,redirect
import os
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
API_TOKEN = '1095762894:AAH1y_gd31l3qimubyq0fYFNRYkeTPi-HCI'
from pymongo import MongoClient

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://saikiran:saikiran0074@codebotdb.vok7o.mongodb.net/codebotdb?retryWrites=true&w=majority")
db=client.codebotdb



    #Step 4: Print to the console the ObjectID of the new document

#Step 5: Tell us that you are done
         
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)
PORT = int(os.environ.get('PORT', '8443'))   

@bot.message_handler(commands=['start'])
def send_welcome(message):
 tid = str(message.from_user.id)
 msg=bot.send_message(tid,"To start bot can please enter the fullname and gmail in format fullname:gmail")
 bot.register_next_step_handler(msg, userdetails)
def userdetails(message):
 tid = str(message.from_user.id)
 details=message.text
 details=details.split(":")
 regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
 if(len(details)==2):
    if len(details[0])>3:
      if(re.search(regex,details[1])):
        if db.user_details.find_one({'fullname':details[0],'gmail':details[1]}) is None:
          result=db.user_details.insert_one({'fullname':details[0],'gmail':details[1]})
        bot.reply_to(message, "Hi "+details[0]+" 👋, Welcome to Codebot. \n I'm here to help you in find_oneing the code you want.\n To begin tap /search\n if you want any help type '/help' command")
      else:
        msg=bot.send_message(tid,"enter vaild gmail reenter data in format fullname:gmail")
        bot.register_next_step_handler(msg, userdetails)
    else:
     msg=bot.send_message(tid,"enter vaild fullname reenter data in format fullname:gmail")
     bot.register_next_step_handler(msg, userdetails)
 else:
    msg=bot.send_message(message, "please enter the details in specified format, correct details")
    bot.register_next_step_handler(msg, userdetails)

  # Handle '/start' and '/help'
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#  bot.reply_to(message, "Hi 👋, Welcome to Codebot. \n I'm here to help you in finding the code you want.\n To begin tap /search\n if you want any help type '/help' command")

@bot.message_handler(commands=['help'])
def help(message):
 bot.reply_to(message,"""
      'tap on /search' 
     command to search code.""")
filename="c.txt"
@bot.message_handler(commands=['c'])
def c(message):
 global f
 global filename
 #bot.reply_to(message,"hello world")
 tid = str(message.from_user.id)
 filename="c.txt"
 f=open(filename,'r',errors = 'ignore')
 msg=bot.send_message(tid,"Enter program name")
 bot.register_next_step_handler(msg, codename)
@bot.message_handler(commands=['cpp'])
def cpp(message):
 global f
 global filename
 #bot.reply_to(message,"hello world")
 tid = str(message.from_user.id)
 filename="c++.txt"
 f=open(filename,'r',errors = 'ignore')
 msg=bot.send_message(tid,"Enter program name")
 bot.register_next_step_handler(msg, codename)
@bot.message_handler(commands=['java'])
def java(message):
 global f
 #bot.reply_to(message,"hello world")
 tid = str(message.from_user.id)
 filename="java.txt"
 f=open(filename,'r',errors = 'ignore')
 msg=bot.send_message(tid,"Enter program name")
 bot.register_next_step_handler(msg, codename)
@bot.message_handler(commands=['python'])
def python(message):
 global f
 global filename
 #bot.reply_to(message,"hello world")
 tid = str(message.from_user.id)
 filename="python.txt"
 f=open(filename,'r',errors = 'ignore')
 msg=bot.send_message(tid,"Enter program name")
 bot.register_next_step_handler(msg, codename)
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
keyboard = [[InlineKeyboardButton("c",url='/c'),
             InlineKeyboardButton("Java", url='/java'), 
             InlineKeyboardButton("Python", url='/python'),
             InlineKeyboardButton("c++", url='/cpp')]]

reply_markup =str(InlineKeyboardMarkup(keyboard))

reply_markup=json.dumps(reply_markup)
@bot.message_handler(commands=['search'])
def search(message):
 tid = str(message.from_user.id)
 bot.reply_to(message,'select a program a language among the following' ,reply_markup=reply_markup)


'''def select_lang(message):
  global f
  global language

  tid = str(message.from_user.id)
  language=message.text
  language=language.lower()
  language_list=["c","c++","java","python"]
  if language not in language_list:
    bot.reply_to(message,"we don't do it here for now")
  else:
    filename=language+".txt"
    f=open(filename,'r',errors = 'ignore')
    msg=bot.send_message(tid,"Enter program name")
    bot.register_next_step_handler(msg, codename)'''
def codename(message):
  
  global f
  global filename
  reply='loading'
  tid = str(message.from_user.id)
  c_name = message.text
  lemmer = nltk.stem.WordNetLemmatizer()
    #Wo#rdNet is a semantically-oriented dictionary of English included in NLTK.
  '''file1 = open("data.txt", "a") 
  file1.write(c_name)'''
  raw=f.read()
  raw=raw.lower()# converts to lowercase
  nltk.download('punkt') # first-time use only
  nltk.download('wordnet') # first-time use only
  sent_tokens = raw.split("etp")# converts to list of sentences 
  word_tokens = nltk.word_tokenize(raw)# converts to list of words

  def LemTokens(tokens):
      return [lemmer.lemmatize(token) for token in tokens]
  remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
  def LemNormalize(text):
      return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
  GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
  GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
  def greeting(sentence):

      for word in sentence.split():
          if word.lower() in GREETING_INPUTS:
              return random.choice(GREETING_RESPONSES)

  def response(user_response):
      robo_response=''
      sent_tokens.append(user_response)
      TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
      tfidf = TfidfVec.fit_transform(sent_tokens)
      
      vals = cosine_similarity(tfidf[-1], tfidf)

      idx=vals.argsort()[0][-2]

      flat = vals.flatten()

      flat.sort()
      req_tfidf = flat[-2]
      if(req_tfidf==0):
          language=filename.split('.')[0]
          if db.userkeywords.find_one({'language':language,'programname':user_response}) is None :
            result=db.userkeywords.insert_one({'language':language,'programname':user_response})
          robo_response=robo_response+"Oops🙁 ,  seems like you entered incorrect program name or this program is available here , to try again please type Y or else type N... "

          return robo_response
      else:
          robo_response = robo_response+sent_tokens[idx]
          #robo_response1 = re.find_oneall("%%(.*)%%",robo_response)[0]
          program_name=robo_response.split("eopn")[0]
          if len(robo_response.split("eokw")) > 1 :
           program_code=robo_response.split("eokw")[1]
           return program_name+program_code
          else:
           return "Oops🙁 ,  seems like you entered incorrect program name or this program is available here , to try again please type Y or else type N... "
          '''list1=nltk.word_tokenize(robo_response)
          program_name=' '.join(list1[:list1.index('=')])
          program_code=' '.join(list1[list1.index('eokw')+4:])'''
          
          #return robo_response
  flag=True
  #print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
  if(flag==True):
      user_response = c_name
      user_response=user_response.lower()
      if(user_response!='bye'):
          if(user_response=='thanks' or user_response=='thank you' ):
              flag=False
              reply="ROBO: You are welcome.."
          else:
              if(greeting(user_response)!=None):
                  reply="ROBO: "+greeting(user_response)
              else:
                  reply=(response(user_response))
                  sent_tokens.remove(user_response)
      elif(user_response=='bye'):
          flag=False 
          reply="ROBO: Bye! take care.."
      else:
          reply=response(user_response)
  #bot.reply_to(message,reply+'\n-----------------------------------------------------------\n "IF YOU WANT TO CONTIUE TO SEARCH PRESS Y OR N"')                  
  msg=bot.send_message(tid,reply+"\n--------------------------\n \033[91m If you want to continue please type \033[92m Y or else type  \033[92m N")
  bot.register_next_step_handler(msg, recheck_lang)
def recheck_lang(message):
  global f
  global filename
  tid=str(message.from_user.id)
  value=message.text
  if value=='y' or value=='Y':
    f=open(filename,'r',errors = 'ignore')
    msg=bot.send_message(tid,"Enter a program name")
    bot.register_next_step_handler(msg, codename)
  elif value=='N' or value=='n':
    bot.reply_to(message,'select a program a language among the following' ,reply_markup=reply_markup)
  else:
    bot.reply_to(message,'you entered wrong key to search a code tap /search')

  # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  value=message.text
  tid=str(message.from_user.id)
 
  for word in value.split():
    if word.lower() in GREETING_INPUTS:
      
      bot.reply_to(message,GREETING_RESPONSES)
      break
  else:
    bot.reply_to(message, 'If you want search a program .\nPlease select a programming language to continue 😄..! \nTo select tap /search ')
                   
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
