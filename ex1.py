import sqlite3
import telebot
from telebot import types

#my_id: 790987023
#Ann_id: 839912037
bot = telebot.TeleBot('874436637:AAGGrTywctZoUhvDntJVYauCvtDLRN0SFRQ')
markup = telebot.types.ReplyKeyboardMarkup(True,True)
#keyboard1.('C', 'D', 'E', 'F', 'G', 'A', 'B')
keyboard1 = types.KeyboardButton('MY ID')
keyboard2 = types.KeyboardButton('COFFEE')
keyboard3 = types.KeyboardButton('ACCOUNT')
keyboard4 = types.KeyboardButton('F')
keyboard5 = types.KeyboardButton('RECEIVE TEXT')
keyboard6 = types.KeyboardButton('A')
keyboard7 = types.KeyboardButton('B')
keyboard8 = types.KeyboardButton('/admin')
markup.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8)

#@bot.message_handler(commands=['start'])
#def start(message):
#    bot.send_message(message.chat.first_name + ', Hi')
#    print(message.chat.id, ', Привет')
#    bot.send_message(message.chat. + ', Hi')

#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'Hi, mr.')

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio', 'photo', ])
def handle_docs_audio(message):
    p = message.document
    print(p)
    save_dir = "D:\\"
    file_name = message.document.file_name
    print(file_name)
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    with open(save_dir + "/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)
    # bot.send_message(message.chat.id, "[*] File added:\nFile name - {}\nFile directory - {}".format(str(file_name), str(save_dir)))


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    print(user_id, message.chat.last_name, message.chat.first_name)



    bot.send_message(message.from_user.id, 'Howdy, ' + message.chat.first_name + '!')#'', your id is ' + str(user_id))
    bot.send_message(message.chat.id, "Ok, let's start! Choose a key", reply_markup=markup)
    #bot.send_location(chat_id=user_id, latitude=53.9006, longitude=27.5590)




"""
###TWO AUTORIZATION FUNCTIONS###
def getAccess(user_id):
  with sqlite3.connect('users.sqlite3') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT is_superuser FROM auth_user WHERE id=?',(user_id,))
    result = cursor.fetchone()
    return result

@bot.message_handler(commands=['admin'])
def repeat_all_message(message):
  print(message.chat.id)
  bot.send_message(message.chat.id,message.text)

  access = getAccess(message.chat.id)

  if access:
    if access == (1,):
      bot.send_message(message.chat.id,'Привет Admin!')
    else:
      bot.send_message(message.chat.id,'Привет User!')
  else:
    bot.send_message(message.chat.id,'Вы не зарегистрированны в системе!')
"""




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.upper() == 'MY ID':
        bot.send_message(790987023, 'Hi')
    elif message.text.upper() == 'ACCOUNT':
        bot.send_message(message.chat.id, ': ' + str(message.chat))

#    elif message.text.upper() == 'A':
 #           photo = open('C:\Program Files\FastStone Image Viewer\Callout\FSCallout_34_05079593.png', 'r')
  #      bot.send_photo(chat_id=790987023, photo=FSCallout_34_05079593)
        #bot.send_photo(chat_id=790987023, 'FILEID')

    elif message.text.upper() == 'COFFEE':
        #bot.send_message(message.chat.id, 'D A G / F#m Em Bm')
        #from serpapi.google_search_results import GoogleSearchResults
        #client = GoogleSearchResults({"q": "coffee", "location": "Minsk"})
        #result = client.get_dict()
        #bot.send_message(message.chat.id, result, link)
        #print(result)
        class Gsearch_python:
            def __init__(self, name_search):
                self.name = name_search
            def Gsearch(self):
                count = 0
                try:
                    from googlesearch import search
                except ImportError:
                    print("No Module named 'google' Found")
                for i in search(query=self.name, tld='co.in', lang='en', num=10, stop=1, pause=2):
                    count += 1
                    print(count)
                    print(i + '\n')
                    bot.send_message(message.chat.id, i + '\n')
        if __name__ == '__main__':
            gs = Gsearch_python("Top Cappuccino Minsk")
            gs.Gsearch()

    elif message.text.upper() == 'A':
        #bot.send_message(message.chat.id, '/CHOOSE')

        file = open("C:\\screen.jpg", "rb")
        if file:
            bot.send_document(790987023, file)
            #bot.send_document(message.chat.id, f)
            #bot.send_photo(790987023, file)
    elif message.text.upper() == '/CHOOSE':
        bot.send_message(790987023, '/it' '\n' '/is' '\n' '/hierarchy')


#def echo_all(message):
    #bot.reply_to(message, message.text)
    print(message.text)

@bot.message_handler(commands=['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='False', switch_inline_query="Telegram")
    markup.add(switch_button)



bot.polling()
