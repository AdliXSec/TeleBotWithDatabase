from telebot import *
from urllib.request import urlopen
from config.confff import api, id, username_owner
import hashlib
import socket
import requests
import json
import random
import base64

bot = TeleBot(api)

def action_id(message):
    
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    id_telegram = message.from_user.id
    username = message.from_user.username
    bot.reply_to(message, '''
Hi, ini ID Telegram kamu
Nama = {}
Username = {}
ID = {}
'''.format(first_name, username, id_telegram))   
    
def owner(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    id_telegram = message.from_user.id
    username = message.from_user.username
    owner = message.text.replace("/owner ", "")
    if owner == "/owner":
        bot.reply_to(message, '''Silahkan masukkan 
command : /owner keluhan
contoh : /owner error pada tools /yt_download''')
    else:
        bot.send_message(id, "Pesan : \n\n" + owner + f"\n\nID : {id_telegram}\nNAME : {first_name}\nUSRNM : {username}")
        bot.reply_to(message, "Pesan telah terkirim ke owner bot silahkan tunggu untuk respon berikutnya")
        
def pw_hash(message):
    
    text = message.text.replace("/pw_hash ", "")
    sha1 = hashlib.sha1()
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()

    sha1.update(text.encode("utf-8"))
    md5.update(text.encode("utf-8"))
    sha256.update(text.encode("utf-8"))
    sha384.update(text.encode("utf-8"))
    sha512.update(text.encode("utf-8"))
    bot.reply_to(message, f'''Note: Password tidak boleh menggunakan spasi ( )

Password hash sha1 :  {sha1.hexdigest()}

Password hash md5 :  {md5.hexdigest()}

Password hash sha256 :  {sha256.hexdigest()}

Password hash sha384 :  {sha384.hexdigest()}

Password hash sha512 :  {sha512.hexdigest()}''')
    
def domain_to_ip(message):
    
    text = message.text.replace("/domain_to_ip ", "")
    
    if text:
        bot.reply_to(message, "Cek Domain {}".format(text))
        bot.reply_to(message, "IP {} Adalah {}".format(text, socket.gethostbyname(text)))
        
def hashmd5(message):
    
    text = message.text.replace("/md5 ", "")
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    bot.reply_to(message, '''nilai asli : {} 
nilai hash md5 : {}'''.format(text, md5.hexdigest()))
    
def hashsha(message):
    
    text = message.text.replace("/sha1 ", "")
    sha = hashlib.sha1()
    sha.update(text.encode("utf-8"))
    bot.reply_to(message, '''nilai asli : {} 
nilai hash sha1 : {}'''.format(text, sha.hexdigest()))
    
def ipgeo(message):
    
    ipaddr = message.text.replace("/ip_geo ", "")
    ipreq = requests.get(f"http://ip-api.com/json/{ipaddr}")

    if ipreq.status_code == 200:
        ipdata = json.loads(ipreq.text)

        if ipdata["status"] == "success":
            for key in ipdata:
                bot.reply_to(message, f"{key.capitalize()} : {ipdata[key]}")
                
                if key == "lon":
                    lat = ipdata["lat"]
                    lon = ipdata["lon"]
                    maps = f"https://www.google.com/maps/@{lat},{lon},9z"
                    bot.reply_to(message, f" Maps : {maps}")
                    
def random_quotes(message):
    
    file = open('q.json','r').read()
    sl = json.loads(file)
    js = random.choice(sl)
    bot.reply_to(message, f'{js["quote"]} \n\nby {js["nama"]}')
    
def ClickjackingTester(message):
    
    def check(url):

        try:
            if "http" not in url: url = "http://" + url

            data = urlopen(url)
            headers = data.info()

            if not "X-Frame-Options" in headers: return True

        except: return False


    def code_html(url):

        code = f"""
<html>
    <head><title>Clickjack test page</title></head>
    <body>
        <p>Website is vulnerable to clickjacking!</p>
        <iframe src="{url}" width="500" height="500" ></iframe>
    </body>
</html>
        """
        return code

    site = message.text.replace("/cj_tester ", "")

        
    bot.reply_to(message, f"[*] Checking {site}")
    status = check(site)

    if status:
        bot.reply_to(message, f" [+] Website is vulnerable! \n[*] Copy This Code and Try This \n{code_html(site)}")
    elif not status: 
        bot.reply_to(message, " [-] Website is not vulnerable!")
    else: 
        bot.reply_to(message, "ERROR")
        
def ip(message):
    web = message.text.replace("/cek_ip_website ", "")
    bot.reply_to(message, "IP web "+web+"  : "+socket.gethostbyname(web))
    
def b64encode(message):
    sample_string = message.text.replace("/base64_encode ", "")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    bot.reply_to(message, "encode base64 : "+sample_string+" -> "+base64_string)
    
def b64decode(message):
    sample_string = message.text.replace("/base64_decode ", "")
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64decode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    bot.reply_to(message, "decode base64 : "+sample_string+" -> "+base64_string)