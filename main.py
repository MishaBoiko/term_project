
import telebot

TOKEN = '7969813710:AAH4bBITrDqLHUNwSIxYPR8_kgmG-7a5Jqs'
bot = telebot.TeleBot(TOKEN)

user_buttons_message_id = {}
user_tip_message_id = {}


@bot.message_handler(commands=['start', 'help'])
def help (message):
    markup1 = telebot.types.InlineKeyboardMarkup()
    btn11 = telebot.types.InlineKeyboardButton('English', callback_data='11')
    btn12 = telebot.types.InlineKeyboardButton('Ukrainian', callback_data='12')
    btn13 = telebot.types.InlineKeyboardButton('Kazakh', callback_data='13')
    markup1.add(btn11, btn12, btn13)
    bot.send_message(message.chat.id,'Choose your language',reply_markup=markup1)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '11':
        bot.send_message(call.message.chat.id, 'Hi! If you (or somebody) are in trouble — follow my instructions :)')
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('headache', callback_data='1')
        btn2 = telebot.types.InlineKeyboardButton('leg fracture', callback_data='2')
        btn3 = telebot.types.InlineKeyboardButton('bleeding', callback_data='3')
        markup.add(btn1, btn2, btn3)
        sent = bot.send_message(call.message.chat.id, 'Choose your problem:', reply_markup=markup)
        user_buttons_message_id[call.message.chat.id] = sent.message_id
    elif call.data == '12':
        bot.send_message(call.message.chat.id, 'Привіт! Якщо у вас (або у когось) проблеми — дотримуйтеся моїх інструкцій :)')
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('головний біль', callback_data='4')
        btn2 = telebot.types.InlineKeyboardButton('перелом ноги', callback_data='5')
        btn3 = telebot.types.InlineKeyboardButton('кровотечі', callback_data='6')
        markup.add(btn1, btn2, btn3)
        sent = bot.send_message(call.message.chat.id, 'Виберіть свою проблему:', reply_markup=markup)
        user_buttons_message_id[call.message.chat.id] = sent.message_id
    elif call.data == '13':
        bot.send_message(call.message.chat.id, 'Сәлем! Егер сізде (немесе басқа біреуде) проблемалар болса, менің нұсқауларымды орындаңыз :)')
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('бас ауруы', callback_data='7')
        btn2 = telebot.types.InlineKeyboardButton('сынған аяқ', callback_data='8')
        btn3 = telebot.types.InlineKeyboardButton('қан кету', callback_data='9')
        markup.add(btn1, btn2, btn3)
        sent = bot.send_message(call.message.chat.id, 'Мәселеңізді таңдаңыз:', reply_markup=markup)
        user_buttons_message_id[call.message.chat.id] = sent.message_id

    chat_id = call.message.chat.id
    if call.data == '1':
        sent = bot.send_message(chat_id, '1) Rest in a quiet room\n2) Drink water\n3) Take pain relievers')
    elif call.data == '2':
        sent = bot.send_message(chat_id,
                                '1) Stay still and avoid moving the leg\n2) Call emergency services immediately\n3) Immobilize the leg using a splint or any available materials (like a board)')
    elif call.data == '3':
        sent = bot.send_message(chat_id,
                              '1) Elevate the leg if possible, to reduce swelling\n2) Call for Help\n3) Bandage – Wrap it to maintain pressure')

    if call.data == '4':
        sent = bot.send_message(chat_id, '1) Відпочиньте в тихій кімнаті\n2) Випийте води\n3) Прийміть знеболювальне')
    elif call.data == '5':
        sent = bot.send_message(chat_id,
                                '1) Залишайтеся нерухомо та не рухайте ногою\n2) Негайно викликайте службу екстреної допомоги\n3) Знерухоміть ногу за допомогою шини або будь-якого доступного матеріалу (наприклад, дошки)')
    elif call.data == '6':
        sent = bot.send_message(chat_id,
                              '1) Підніміть ногу, якщо це можливо, щоб зменшити набряк\n2) Викличте допомогу\n3) Перев’яжіть – замотайте, щоб підтримувати тиск')

    if call.data == '7':
        sent = bot.send_message(chat_id, '1) Тыныш бөлмеде демалыңыз\n2) Су ішіңіз\n3) Ауырсынуға қарсы дәрі ішіңіз')
    elif call.data == '8':
        sent = bot.send_message(chat_id,
                                '1) Қозғалмай отырыңыз және аяқты қозғалтпаңыз\n2) Жедел қызметтерді дереу шақырыңыз\n3) Аяқыңызды шпинатпен немесе кез келген қолжетімді материалмен (мысалы, тақтайша) қозғалтыңыз.')
    elif call.data == '9':
        sent = bot.send_message(chat_id,
                                '1) Ісінуді азайту үшін мүмкіндігінше аяқты көтеріңіз\n2) Көмек шақырыңыз\n3) Таңғыш – қысымды ұстап тұру үшін орау')

    if chat_id in user_tip_message_id:
        try:
            bot.delete_message(chat_id, user_tip_message_id[chat_id])
        except Exception:
            pass
    user_tip_message_id[chat_id] = sent.message_id


bot.polling(none_stop=True)