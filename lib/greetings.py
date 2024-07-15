from telebot import *
from config.confff import api, id, username_owner

bot = TeleBot(api)


def start_message(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if message.from_user.id == id and message.from_user.username == username_owner:
        bot.reply_to(message, 'Hallo, senang bertemu anda kembali. Tuan, apakah ada yang bisa saya bantu?')
    else:
        bot.reply_to(message, 'Hi, apa kabar {}? Ada yang bisa saya bantu? Jika ada ketik \n/help'.format(first_name))
        
def menu(message):
    
    bot.reply_to(message, ''' -= TOOLS MENU =-

Ada beberapa jenis tools yang tersedia disini, kamu
bisa memilih jenis tools sesuai apa yang kamu butuhkan
jika jenis tools yang kamu butuhkan tidak tersedia 
cobalah cek di tools lainya mungkin tools yang kamu 
butuhkan tersedia di situ :)

Tools Lainnya  -->  /lainnya
Tools Download -->  /downloads
Tools Google   -->  /search
Tools Rumus    -->  /rumus

Kamu juga bisa mengaktifkan notifikasi pemberitahuan dengan cara 
mengetikkan /notif

pastikan kamu telah registrasi dengan cara mengetik /register

Jika terdapat bug dapat menghubungi owner yang tersedia
/owner

-= Terimakasih Telah Mencoba Bot Kami =-''')
    
def otherstools(message):
    bot.reply_to(message, '''
Check ID:
/cek_id — Digunakan untuk mengecek ID Telegram anda, cara penggunaan nya.
ex = /cek_id 

Domain To IP:
/domain_to_ip — Digunakan mengubah dari domain ke IP, cara penggunaan nya.
ex = /domain_to_ip example.com

MD5:
/md5 — Digunakan untuk mengubah kalimat / huruf ke hash MD5, cara penggunaan nya.
ex = /md5 example

SHA1:
/sha1 — Digunakan untuk mengubah kalimat / huruf ke hash sha1, cara penggunaan nya.
ex = /sha1 example

IP Geolocation:
/ip_geo — Digunakan untuk mengetahui informasi tentang IP, mulai dari nama negara hingga ke lokasi IP tersebut, cara penggunaan nya.
ex = /ip_geo 8.8.8.8

Password Hash:
/pw_hash — Digunakan untuk mengencripsi password ke hash md5 hingga hash sha512, cara penggunaan nya.
ex = /pw_hash yourPass123

Random Quotes:
/random_quotes — Digunakan untuk memunculkan kata kata keren dan memotivasi, cara penggunaan nya.
ex = /random_quotes

ClickJacking Tester
/cj_tester — Digunakan untuk mengecek sebuah website apakah website tersebut vuln terhadap clickjacking atau tidak, cara penggunaan nya.
ex = /cj_tester https://example.com

Base64 Encode:
/base64_encode — digunakan untuk mengubah text ke Base64
ex = /base64_encode halo
output = aGFsbw==

Base64 Decode:
/base64_decode — digunakan untuk mengubah base64 ke text
ex = /base64_decode aGFsbw==
output = halo''')
    
def downloads(message):
    bot.reply_to(message, '''
-= DOWNLOADER TOOLS =-


YT Vidmate Download:
/yt_vidmate — Digunakan untuk download musik youtube, berupa link download, cara penggunaan.
ex = /yt_vidmate https://youtube/gcJVgFQwnpc

YT Audio Download:
/yt_audio — Digunakan untuk download musik youtube, dapat mendownload secara otomatis, dan di kirim otomatis ke telegram, cara penggunaan.
ex = /yt_audio https://youtube/gcJVgFQwnpc

YT Search:
/yt_search — Digunakan untuk mencari semua video di youtube dengan limit 5.
ex = /yt_search lagu yang enak

Instagram Download:
/ig_download — Digunakan untuk download postingan instagram, caranya.
ex = /ig_download linkpostingan.com

QR Code Generator:
/text_to_qrcode — Digunakan untuk mengubah text to QR Code
ex = /text_to_qrcode haii semuaaa''')
    
def search(message):
    bot.reply_to(message, '''
-= Google Tools =-


Tanya Wiki:
/apa_itu — Digunakan untuk mencaritahu sesuatu, dan mendapatkan jawaban dari wikipeadia, contoh.
ex = /apa_itu cahaya
ex2 = /apa_itu Google LLC

Google Dork:
/google_dork — Digunakan untuk mencari url url website yang andah butuhkan.
ex = /google_dork cara membuat kue
''')
    
def rumus(message):
    bot.reply_to(message, '''
-= Rumus =-

/konversi_suhu — Digunakan untuk mengkonversi suhu dari celcius ke Fahrenheit, Kelvin, Reamur contoh.
ex = /konversi_suhu celsius 80
''')