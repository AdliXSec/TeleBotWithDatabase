from telebot import *
from pyqrcode import QRCode
from bs4 import BeautifulSoup as bes
from config.confff import api, ig_log, ig_pw
import os
import pafy
import requests
import shutil

bot = TeleBot(api)

def ig_download(message):
    try:
        isi = message.text.replace("/ig_download ", "").replace("https://www.instagram.com/reel/", "").replace("/?utm_source=ig_web_copy_link", "").replace("https://www.instagram.com/p/","").replace("/?igshid=YmMyMTA2M2Y=", "")
        bot.reply_to(message, "Download Sedang di proses Silahkan menunggu, Download mungkin agak lama.....")
        os.system(f"instaloader --login={ig_log} --password={ig_pw} -- -{isi}")
        
        for i in os.listdir(f'-{isi}'):
            print(i)
            if i.endswith(".jpg"):
                print("anjay")
                bot.send_photo(message.chat.id, open(f'-{isi}/{i}', 'rb'))
            elif i.endswith(".mp4"):
                print("anjass")
                bot.send_video(message.chat.id, open(f'-{isi}/{i}', 'rb'))
        shutil.rmtree(f"-{isi}")
    except:
        bot.reply_to(message, '''Maaf, Ada Kesalahan Silahkan Masukkan Kembali Link Dengan Benar''')
        
def qrcode(message):
    data = message.text.replace("/text_to_qrcode ", "")
    qrfile = f"hasil qrcode {message.from_user.id}.png"

    try:
        QR_Code = QRCode(data)
        QR_Code.png(qrfile, scale=10)
        for i in os.listdir():
            if i.endswith(f"{message.from_user.id}.png"):
                print(i)
                bot.send_photo(message.chat.id, open(qrfile, "rb"))
                bot.reply_to(message, f"hasil dari text {data} ke qrcode")
                os.remove(qrfile)
    except:
        bot.reply_to(message, "maaf gagal membuat qrcode masukkan kalimat yang benar")
        
def ytAudio(message):
    try:
        filter = message.text.replace("/yt_audio ", "")
        url = pafy.new(filter)
        bot.reply_to(message, f'''Note : versi k2 dalam proses pengembangan, maaf jika ada error

Judul : {url.title}
Thumbnail : {url.thumb}
Durasi : {url.duration}

Sedang Mendownload Mohon Tunggu Sesaat
estimasi download [3 menit jika sinyal lancar]

''')
        result = url.getbestaudio()
        result.download(f'{url.title} {message.from_user.id}.mp3')
        
        for i in os.listdir():
            if i.endswith(f"{message.from_user.id}.mp3"):
                print(i)
                bot.send_audio(message.chat.id, open(i, 'rb'))
                os.remove(i)
    except:
        bot.reply_to(message, "Maaf, Ada Kesalahan Silahkan Masukkan Kembali Link Dengan Benar")
        
def ytVid(message):
    
    text = message.text.replace("/yt_vidmate ", "")
    if text:
        try:
            url = text.replace('[','').replace(']','')
            ytAudio = requests.post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
            find = bes(ytAudio['result'], 'html.parser').findAll('td')
            ukuran = find[len(find)-10].text
            id = re.findall('var k__id = "(.*?)"', ytAudio['result'])
            judul = bes(ytAudio['result'], 'html.parser').find('b').text
            link_download = bes(requests.post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
            bot.reply_to(message, f'''Judul : {judul}
Ukuran : {ukuran}
Download link : {link_download}''')
        except Exception as e:
            print(e)
            bot.reply_to(message, "Maaf sepertinya link ini telah error")