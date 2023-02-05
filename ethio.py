import time
import sqlite3 as sql
import wikipedia
import os
from googletrans import Translator
import telebot
from telebot import types
import logging
logging.basicConfig(filename="logs.txt",filemode="a",format="%(name)s - %(levelname)s - %(message)s - line:  %(lineno)d - time: %(asctime)s")
try:
    x=5/0
except Exception as e:
    logging.error(str(e))

print("running...")
PORT = int(os.environ.get('PORT', 5000))
callbackD = str
TOKEN = "1266716133:AAFDi43nrutIlrTGTcCgUqBMVBTXhc2k1wk"
bot = telebot.TeleBot("1266716133:AAFDi43nrutIlrTGTcCgUqBMVBTXhc2k1wk")
fileName = "./logs.txt"
currentCommand=""
searchCallbackD=str
globalContenList:list
globalPage:str
file="./UserInfo"
def MainMethod():
    global currentCommand
    @bot.message_handler(commands=['start'])
    def startText(message):
        global currentCommand
        global file
        currentCommand="start"
        bot.reply_to(message, 'ለመጀመር ከስር የ "/" ቁልፉን ይጫኑ ወይም ጽሁፍ መፃፊያው ላይ "/"ን ሲጽፉ ከሚመጣሎት አማራጭ ውስጥ የሚፈልጉትን ይምረጡ።\n\t\t @Ethiopedia_bot')
        localTime = time.asctime(time.localtime(time.time()))
        conn = sql.connect(file)
        try:

            curs=conn.cursor()
            curs.execute("insert into StartedCmd values ("+str(message.chat.id)+",'"+str(message.chat.first_name).replace("'",",")+"','"+str(localTime)+"')")
            conn.commit()
        except:
            pass
        conn.close()
    @bot.message_handler(commands=['help'])
    def helpText(message):
        global currentCommand
        toLeft=u'\U0001f449'

        currentCommand="help"

        bot.reply_to(message, 'ለመጀመር ከስር የ "/" ቁልፉን ይጫኑ ወይም ጽሁፍ መጻፊያው ላይ "/"ን ሲጽፉ ከሚመጣሎት አማራጭ ውስጥ የሚፈልጉትን ይምረጡ።\n'
                     +toLeft+" በቃል፣ በዓ.ነገር መረጃን ለመፈለግ (ከዊኪፒዲያ/wikipedia ወደ አማርኛ የተተረጎመ መረጃ ለማግኝት) /search ብለው ይላኩ\n"+toLeft+" አስተያየትዎን ለመላክ /comment ብለው ይላኩ\n"+toLeft+" እኛን ለማግኘት /contactus ብለው ይላኩ\n\t\t@Ethiopedia_bot")

    @bot.message_handler(commands=['contactus'])

    def contactText(message):
        global currentCommand
        currentCommand='contactus'
        bot.send_message(message.chat.id, 'Email: zolaashenafi48@gmail.com')

    @bot.message_handler(commands=['feedbackreply'])
    def sendFeedback(message):
        global currentCommand
        myChatID = "667272146"
        currentCommand="feedbackreply"
        bot.send_message(str(myChatID),"hmmmmmm.....")

        @bot.message_handler(func=lambda message: currentCommand == "feedbackreply")
        def thanks(message):
            global currentCommand
            myChatID = "667272146"
            feedback=message.text
            try:
                index=feedback.find("#")
                mes_ID=feedback[0:index]
                mes_reply=feedback[index+1:]
                bot.send_message(int(mes_ID),"ለአስተያየትዎ ምላሽ\n"+mes_reply)

            except:
                bot.send_message(myChatID,"not correct format")
            currentCommand = "start"
    @bot.message_handler(commands=['comment'])
    def commentBox(message):
        global currentCommand
        currentCommand="comment"
        bot.send_message(message.chat.id,"አስተያየትዎን ይፃፉልን!!!")
        @bot.message_handler(func=lambda message: currentCommand=="comment")
        def thanks(message):
            global currentCommand
            myChatID="667272146"
            bot.send_message(message.chat.id,"ለአስተያየትዎ እናመሰግናለን!!!")
            bot.send_message(myChatID,"(comment): "+message.text+"\nuserName: "+message.chat.first_name+"\nID: "+str(message.chat.id))
            currentCommand="start"
    @bot.message_handler(commands=['translator'])
    def translatorText(message):
        global currentCommand
        currentCommand="translator"
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("ከአማርኛ ወደ አንግሊዘኛ - Amh->Eng", callback_data="am-en")
        btn2 = types.InlineKeyboardButton("ከአንግሊዘኛ ወደ አማርኛ - Eng->Amh", callback_data="en-am")
        btn3 = types.InlineKeyboardButton("ከአማርኛ ወደ አረብኛ - Amh->Arabic", callback_data="am-ar")
        btn4 = types.InlineKeyboardButton("ከአረብኛ ወደ አማርኛ - Arabic->Amh", callback_data="ar-am")
        btn5 = types.InlineKeyboardButton("ከአማርኛ ወደ ስፓኒሽ - Amh->Spanish", callback_data="am-es")
        btn6 = types.InlineKeyboardButton("ከስፓኒሽ ወደ አማርኛ - Spanish->Amh", callback_data="es-am")
        btn7 = types.InlineKeyboardButton("ከአማርኛ ወደ ፍሬንች - Amh->French", callback_data="am-fr")
        btn8 = types.InlineKeyboardButton("ከፍሬንች ወደ አማርኛ - French->Amh", callback_data="fr-am")
        btn9 = types.InlineKeyboardButton("ከአማርኛ ወደ ሕንድኛ - Amh->Hindi", callback_data="am-hi")
        btn10 = types.InlineKeyboardButton("ከሕንድኛ ወደ አማርኛ - Hindi->Amh", callback_data="hi-am")
        btn11 = types.InlineKeyboardButton("ከአማርኛ ወደ ቻይንኛ - Amh->Chinese", callback_data="am-zh-cn")
        btn12 = types.InlineKeyboardButton("ከቻይንኛ ወደ አማርኛ - Chinese->Amh", callback_data="zh-cn-am")

        keyboard.row(btn1, btn2)
        keyboard.row(btn3, btn4)
        keyboard.row(btn5, btn6)
        keyboard.row(btn7, btn8)
        keyboard.row(btn9, btn10)
        keyboard.row(btn11, btn12)

        bot.send_message(message.chat.id, "ከስር ይምረጡ", reply_markup=keyboard)

    @bot.message_handler(commands=['search'])
    def searchCommand(message):
        inSearch=False
        FirstTry=True
        global currentCommand
        currentCommand = "search"
        bot.send_message(message.chat.id, "መረጃ የፈለጉበትን ቃል ያስገቡ(በአማርኛ ወይም በእንግሊዝኛ)")

        @bot.message_handler(func=lambda message: currentCommand == "search" and FirstTry)
        def SearchMethod(message):
            global inSearch
            inSearch=False
            global FirstTry
            global file
            FirstTry=True
            mes_id_pro=bot.send_message(message.chat.id,"ተዛማጅ ርዕሶችን በመፈለግ ላይ...").message_id
            localTime = time.asctime(time.localtime(time.time()))
            conn = sql.connect(file)
            try:
                curs=conn.cursor()
                curs.execute("insert into SearchCmd values ('" + str(message.chat.id) + "','" + str(
                    message.chat.first_name) + "','"+str(message.text).replace("'",",")+"','" + str(localTime)+"')")
                conn.commit()
            except:

                pass

            conn.close()
            # ifstream = open(fileName, "a")
            # info = ("*****************\nKeyword: "+message.text+"\n"+localTime+"\n*****************\n")
            # ifstream.write(info)
            # ifstream.close()
            global currentCommand
            #t_text = wordTranslator(message.text, "en")
            mes_id_fu:None
            resultList = WikiSearch(message.text,"am")
            if len(resultList) == 0:
                resultList=WikiSearch(message.text,"en")
                if len(resultList)==0:
                    bot.delete_message(message.chat.id,mes_id_pro)
                    bot.send_message(message.chat.id, "ምንም መረጃ አልተገኘም ቃሉን ቀይረው ይሞክሩ")
                else:
                    keyboard2 = types.InlineKeyboardMarkup()
                    btnList = []
                    i = 0
                    for r in resultList:
                        # r_translated = wordTranslator(str(r), "am")
                        btnList.append(types.InlineKeyboardButton(r, callback_data=r))
                        i += 1
                    for b in btnList:
                        keyboard2.row(b)
                    mes_id_fu = bot.send_message(message.chat.id, "አማርኛ ርዕስ አልተገኘም፣ከስር ይምረጡ",
                                                 reply_markup=keyboard2).message_id
            elif len(resultList)!=0:
                keyboard2 = types.InlineKeyboardMarkup()
                btnList=[]
                i = 0

                for r in resultList:

                    #r_translated = wordTranslator(str(r), "am")
                    if len(r.encode('utf-8'))<60:
                        btnList.append(types.InlineKeyboardButton(str(r), callback_data=str(r)))
                        i += 1
                for b in btnList:
                    keyboard2.row(b)
                mes_id_fu=bot.send_message(message.chat.id, "ከስር ይምረጡ፣ የሚፈልጉትን ርዕስ ካላገኙ ቃሉን ቀይረው ይሞክሩ", reply_markup=keyboard2).message_id



            @bot.callback_query_handler(func=lambda call3: currentCommand == "search" and not inSearch and FirstTry)
            def t_callback(call3):
                global inSearch
                global FirstTry

                inSearch=True
                FirstTry = False

                mes_id = bot.send_message(call3.message.chat.id, "በመፈለግ ላይ... - Searching...").message_id
                page = showPage(call3.data)
                pageIntro=page[0:page.find("==")]
                #t_page = wordTranslator(pageIntro, "am")
                bot.delete_message(message_id=mes_id,chat_id=call3.message.chat.id)
                if len(pageIntro) > 4000:
                    for x in range(0, len(pageIntro), 4000):
                        bot.send_message(call3.message.chat.id, pageIntro[x:x + 4000]+"\n\t\t@Ethiopedia_bot")
                else:
                    bot.send_message(call3.message.chat.id, pageIntro+"\n\t\t@Ethiopedia_bot")
                mes_id_art = bot.send_message(call3.message.chat.id, "ንዑስ ርዕሶችን በመፈለግ ላይ...").message_id
                contList=showContentList(page)

                keyboard3 = types.InlineKeyboardMarkup()
                btnList3 = []
                no=0
                for c in contList:

                    #c_translated = wordTranslator(str(contList[no][0]), "am")

                    btnList3.append(types.InlineKeyboardButton(contList[no][0], callback_data=str(no)))
                    no += 1
                for b2 in btnList3:
                    keyboard3.row(b2)
                bot.delete_message(message_id=mes_id_art,chat_id=call3.message.chat.id)
                bot.send_message(call3.message.chat.id, "ንዑስ ርዕሶች",
                                 reply_markup=keyboard3)
                setContList(contList,page)
                bot.send_message(call3.message.chat.id,"ፍለጋው ተጠናቋል።")
                @bot.callback_query_handler(func=lambda call2: currentCommand == "search" and inSearch)
                def article_callback(call2):
                    global inSearch
                    global FirstTry
                    FirstTry=False
                    if not call2.data.isdigit():
                        t_callback(call2)
                    else:
                        paragraph=getSplit(getContList(),int(call2.data),getPage())

                        #t_paragraph=wordTranslator(paragraph,"am")

                        if len(paragraph) > 4000:

                            for x in range(0, len(paragraph), 4000):

                                bot.send_message(call2.message.chat.id, paragraph[x:x + 4000] + "\n\t\t@Ethiopedia_bot")
                        else:

                            bot.send_message(call2.message.chat.id, paragraph + "\n\t\t@Ethiopedia_bot")



    # @bot.callback_query_handler(func=lambda call: currentCommand=="translatorbutnotworking")
    # def callback_inline(call):
    #     global callbackD
    #     callbackD = str(call.data)
    #     global currentCommand
    #     if call.message:
    #         if call.data == "am-en":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="አማርኛ ጽሑፉን ያስገቡ- Enter the 'Amharic' Text")
    #             wordReplyer(callbackD)
    #         elif call.data == "en-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'English' Text- እንግሊዘኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "am-ar":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Amharic' Text- አማርኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "ar-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Arabic' Text- አረብኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "am-es":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Amharic' Text- አማርኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "es-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Spanish' Text- ስፓኒሽ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "am-fr":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Amharic' Text- አማርኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "fr-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'French' Text- ፍሬንች ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "am-hi":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Amharic' Text- አማርኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "hi-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Hindi' Text- ሕንድኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "am-zh-cn":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Amharic' Text- አማርኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)
    #         elif call.data == "zh-cn-am":
    #             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                                   text="Enter the 'Chinese' Text- ቻይንኛ ጽሑፉን ያስገቡ")
    #             wordReplyer(callbackD)

    def wordReplyer(callbackData):
        global callbackD
        global currentCommand

        @bot.message_handler(func=lambda message: currentCommand=="translator")
        def wordReceiver(message):
            global currentCommand
            global mes
            global file
            localTime = time.asctime(time.localtime(time.time()))
            mes = message
            translateText = str(message.text)

            mes_id = bot.send_message(message.chat.id, "ትንሽ ይጠብቁ... - Please Wait...").message_id

            translatedText = str(tryTranslating(message.text, callbackD))
            bot.edit_message_text(chat_id=message.chat.id, message_id=mes_id,
                                  text="******\n" + translatedText + "\n******\n\t\t@Ethiopedia_bot")
            conn = sql.connect(file)
            try:
                curs = conn.cursor()
                curs.execute("insert into TranslatorCmd values ('" + str(message.chat.id) + "','" + str(
                    message.chat.first_name).replace("'",",") + "','"+ str(callbackD) +"','" + str(translateText).replace("'",",") +"','"+str(translatedText).replace("'",",") +"','"+ str(localTime)+"')")
                conn.commit()
            except:
                print("unsupported")
                pass
            conn.close()
            # ifstream = open(fileName, "a")
            # info = ("accName: " + message.chat.first_name + "\nfrom-to: " + str(
            #     callbackD) + "\n" + str(translateText) + " - " + str(translatedText) + "\n" + str(
            #     localTime) + "\n******************************************\n")

            # print("accName: " + message.chat.first_name + "\nfrom-to: " + str(
            #     callbackD) + "\n" + str(translateText) + " - " + str(translatedText) + "\n" + str(
            #     localTime) + "\n******************************************\n")
            # ifstream.write(info)
            # ifstream.close()

    @bot.message_handler(func=lambda message:currentCommand!="search" and currentCommand!="comment" and currentCommand!="feedbackreply")
    def wordReceiver2(message):
        bot.send_message(message.chat.id,"ይቅርታ ምንም ምርጫ አልመረጡም")

    def tryTranslating(string, callback):
        global Translatedlist
        global callbackD

        translator = Translator()
        translatedText = ""
        try:
            if callbackD == 'zh-cn-am':

                Translatedlist = translator.translate(string, src="zh-cn", dest="am")


            elif callbackD == 'am-zh-cn':
                Translatedlist = translator.translate(string, src="am", dest="zh-cn")
                return Translatedlist.text
            else:
                Translatedlist = translator.translate(string, src=callbackD[0:2], dest=callbackD[3:])


        except Exception as e:
            print(e)
            tryTranslating(string, callbackD)
        translatedText = Translatedlist.text

        return translatedText




    def wordTranslator(keyword,lang):
        global TransList
        translator = Translator()

        translatedText = ""
        try:

            TransList = translator.translate(keyword, dest=lang)


        except Exception as e:
            print(e)
            wordTranslator(keyword,lang)
        translatedText = TransList.text

        return translatedText

    def WikiSearch(keyword: str,lang):
        wikipedia.set_lang(lang)
        searchResult = wikipedia.search(keyword, results=5)

        return searchResult

    def showPage(keyword):
        try:
            pageResult = wikipedia.page(keyword)
            contentResult = pageResult.content
            return contentResult
        except:
            return "ይቅርታ በመረጡት ርዕስ መረጃ ማግኝት አልተቻለም"

    def showContentList(page):
        contentList = []
        wholeContent = page
        #print(wholeContent)
        start = 0
        boolEnd = False
        startIndex = 0
        afterEqual = 0
        noteIndexStart = 0
        noteIndexEnd = 0
        while start<len(wholeContent) and start != 1 and afterEqual != -1:

            start = str(wholeContent).find("==", start)
            beforeEqual = start
            while start<len(wholeContent) and wholeContent[start] == "=":
                start += 1

            afterEqual = start

            if not boolEnd:
                startIndex = afterEqual
                lastbE = beforeEqual
                noteIndexEnd = lastbE
                boolEnd = True

            elif boolEnd:
                noteIndexStart = afterEqual
                contentList.append([str(wholeContent[startIndex:beforeEqual]), afterEqual, lastbE])
                boolEnd = False

        return contentList

    def getSplit(cList, pos, page):
        parTitle = ""
        parSIndex = 0
        parEIndex = 0
        for i in range(0, len(cList)):
            if i == pos:
                if i == len(cList) - 1:
                    parTitle = str(cList[i][0])
                    parSIndex = int(cList[i][1])
                    parEIndex = -1
                else:
                    parTitle = str(cList[i][0])
                    parSIndex = int(cList[i][1])
                    parEIndex = int(cList[i + 1][2])

            else:
                continue
            return parTitle + "\n" + page[parSIndex:parEIndex].lstrip()
    def setContList(cList,page):
        global globalContenList
        global globalPage
        globalContenList=cList
        globalPage=page
    def getContList():

        return globalContenList
    def getPage():
        return globalPage


    while (True):
        try:
            bot.polling()
        except Exception as e:
            logging.error(e)

            time.sleep(15)

try:
    MainMethod()
except Exception as e:
    logging.error(str(e))