from email import message
from click import command
from telebot import *
import math
from datetime import datetime
import png
import re
import requests
import time
from re import U
from lib.database import *
from lib.greetings import *
from lib.download.domain import *
from lib.rumus.rumain import *
from lib.search.semain import *
from lib.other.otmain import *
# import mysql.connector
from config.confff import api
# pip install pyqrcode
# pip install pypng
# pip install pafy
# pip install pytelegrambotapi
# pip install youtube_dl
# pip install requests
# pip install instaloader
# pip install beautifulsoup4
# pip install instaloader
# pip install youtube-search-python

# Note : edit file backend_youtube_dl.py in library pafy
# line 53 and 54, 
# change to self._likes = self._ydl_info.get('like_count',0) 
# And self._dislikes = self._ydl_info.get('dislike_count',0)

# Connection
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     database='telegram'
# )

# print(db)
# sql = db.cursor()


bot = TeleBot(api)

@bot.message_handler(commands=['start'])
def start(message):
    try:
        start_message(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['deleteregister'])
def deleteregister(message):
    try:
        hapus_data(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['register'])
def reg(message):
    try:
        register_tele(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['notif'])
def notf(message):
    try:
        notif(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['cek_id'])
def ci(message):
    try:
        action_id(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['help'])
def help(message):
    try:
        menu(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['lainnya'])
def lain(message):
    try:
        otherstools(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['downloads'])
def downl(message):
    try:
        downloads(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['search'])
def secr(message):
    try:
        search(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['rumus'])
def rum(message):
    try:
        rumus(message)
    except Exception as e:
        bot.reply_to(message, str(e))


# BAGIAN TOOLS

@bot.message_handler(commands=['owner'])
def own(message):
    try:
        owner(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['google_dork'])
def gdork(message):
    try:
        google(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['konversi_suhu'])
def konsu(message):
    try:
        suhu(message)
    except Exception as e:
        bot.reply_to(message, str(e))
    
@bot.message_handler(commands=['domain_to_ip'])
def dotoip(message):
    try:
        domain_to_ip(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['md5'])
def md5(message):
    try:
        hashmd5(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['sha1'])
def sha1(message):
    try:
        hashsha(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['ip_geo'])
def ipge(message):
    try:
        ipgeo(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['pw_hash'])
def pha(message):
    try:
        pw_hash(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['random_quotes'])
def quotes(message):
    try:
        random_quotes(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['cj_tester'])
def cjtest(message):
    try:
        ClickjackingTester(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['apa_itu'])
def apit(message):
    try:
        wiki(message)
    except Exception as e:
        bot.reply_to(message, str(e))
            
@bot.message_handler(commands=['yt_vidmate'])
def yaud(message):
    try:
        ytVid(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['yt_audio'])
def yaud(message):
    try:
        ytAudio(message)
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands=['text_to_qrcode'])
def textqr(message):
    try:
        qrcode(message)
    except Exception as e:
        bot.reply_to(message, str(e))
            
        
@bot.message_handler(commands=['ig_download'])
def igdo(message):
    try:
        ig_download(message)
    except Exception as e:
        bot.reply_to(message, str(e))
            
@bot.message_handler(commands=['yt_search'])
def yesea(message):
    try:
        ytSearch(message)
    except Exception as e:
        bot.reply_to(message, str(e))
            

# @bot.message_handler(commands=['story_horror'])
# def story(message):
    
#     texts = message.text.split()
#     filter = texts[1]
#     text = filter.replace("_", " ")
#     if text == "judul":
#         query = "select judul_cerita from cerita"
#         sql.execute(query)
#         result = sql.fetchall()
#         pesan = ''
#         for data in result:
#             pesan = pesan + 'Judul : ' + str(data).replace("'", "").replace("(", "").replace(")", "").replace(",", "")  + '\nCara Akses : /story_horror ' + str(data).replace(" ", "_").replace("'", "").replace("(", "").replace(")", "").replace(",", "") + '\n\n'
#         bot.reply_to(message, pesan)
#     else:
#         query = f"select isi_cerita from cerita where judul_cerita = '{text}'"
#         sql.execute(query)
#         result = sql.fetchall()
#         pesan = ''
#         for data in result:
#             pesan = pesan + str(data) + '\n'
#             if len(str(data)) > 4096:
#                 text = "Cerita Gagal Terkirim"
#                 pesan = f"Maaf, cerita ini tidak dapat terkitim karena melebihi 4096 karakter/batas karakter chat di telegram. \ncerita ini memiliki {len(str(data))} karakter"
#         bot.reply_to(message, f'''{text}

# {pesan.replace("'", "").replace("(", "").replace(")", "")}''')
        
# @bot.message_handler(commands=['add_story'])
# def add_story(message):
#     if message.from_user.id == id and message.from_user.username == username_owner:
#         bot.reply_to(message, "Cerita Anda Segera Kami Proses")
#     else:
#         bot.reply_to(message, "Sorry, just owner can use this commands")
    
    
# @bot.message_handler(commands=['tes_inp'])
# def tes_inp(message):
#     text = message.text.replace("/tes_inp ", "")
#     bot.reply_to(message, text)
    
# @bot.message_handler(commands=['spam_call'])
# def spamcall(message):
#     nohp = message.text.replace("/spam_call ", "")
#     if nohp == "":
#         bot.reply_to(message, "Maaf, nomor target harus di isi contoh /spam_call 896*****114")
#     else:
#         bot.reply_to(message, "spam pada nomor "+nohp+" sedang di proses silahkan tunggu")
#         for i in range(5):
#                 req = requests.get('https://id.jagreward.com/member/verify-mobile/'+nohp)
#                 js = json.loads(req.text)
#                 if js['result'] == 1:
#                     bot.reply_to(message, "spam berhasil di kirim ke target")
#                 elif js['result'] == 0:
#                     bot.reply_to(message, "maaf anda melebihi batas spam")
#                 else:
#                     bot.reply_to(message, "spam gagal")
                    
@bot.message_handler(commands=['cek_ip_website'])
def ciw(message):
    try:
        ip(message)
    except Exception as e:
        bot.reply_to(message, str(e))
                    
@bot.message_handler(commands=['base64_encode'])
def b64e(message):
    try:
        b64encode(message)
    except Exception as e:
        bot.reply_to(message, str(e))

@bot.message_handler(commands=['base64_decode'])
def b64d(message):
    try:
        b64decode(message)
    except Exception as e:
        bot.reply_to(message, str(e))
                    
@bot.message_handler(commands=['fisika'])
def fisika(message):
    BIL = message.text.replace("/fisika ", "")
    # Menghitung sin dari sudut 30 derajat
    sudut_radian = math.radians(30)  # Mengubah sudut dari derajat ke radian
    sin_value = math.sin(sudut_radian)
    print("sin(30 derajat) =", sin_value)

    # Menghitung cos dari sudut 45 derajat
    sudut_radian = math.radians(45)  # Mengubah sudut dari derajat ke radian
    cos_value = math.cos(sudut_radian)
    print("cos(45 derajat) =", cos_value)

    # Menghitung tan dari sudut 60 derajat
    sudut_radian = math.radians(60)  # Mengubah sudut dari derajat ke radian
    tan_value = math.tan(sudut_radian)
    print("tan(60 derajat) =", tan_value)

    totalsct = sin_value * cos_value * tan_value
    print(totalsct)
    # Membagi string menjadi potongan-potongan berdasarkan spasi
    tokens = BIL.split()

    # Mengonversi setiap token menjadi float dan menyimpannya dalam daftar (list)
    angka_float = []
    for token in tokens:
        angka_float.append(float(token))

    # Menampilkan daftar angka dalam tipe data float
    print(angka_float)
    print(angka_float[0])
    print(angka_float[1])
    print(angka_float[2])
    print()
    print("Hasil : ")
    print(angka_float[0] * angka_float[1] * angka_float[2])
    ttl = angka_float[0] * angka_float[1] * angka_float[2]
    bot.reply_to(message, f"Hasil : {ttl}")
    

hitwhile = 0
while True:
    try:
        now = datetime.now()
        current_date = now.strftime("%d %B %Y %H:%M:%S")
        print(f"bot sedang berjalan, Date : {current_date}")
        hitwhile = hitwhile + 1
        print(hitwhile)
        bot.polling()
    except:
        pass