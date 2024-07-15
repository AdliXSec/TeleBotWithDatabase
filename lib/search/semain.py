from telebot import *
from youtubesearchpython import VideosSearch
from config.confff import api
from requests_html import HTMLSession
import requests

bot = TeleBot(api)

def google(message):
    Query = message.text.replace("/google_dork ", "")
    Limit = 20

    file = open('Results.txt', 'w')

    s = HTMLSession()

    headers = {
        'authority': 'www.google.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {
        'q': Query,
        'num': Limit,
    }

    response = s.get('https://www.google.com/search', params=params)

    if 'did not match any documents' in response.text:
        bot.reply_to(message, "Not Found Sorry")
        exit()
    elif 'Our systems have detected unusual traffic from your computer' in response.text:
        bot.reply_to(message, "Captcha Triggered!\nUse Vpn Or Try After Sometime.")
        exit()
    else:
        links = list(response.html.absolute_links)
        bot.reply_to(message, "menampilkan sekitar 20 url")
        time.sleep(3)
        for url in links[:]:
            if not 'google' in url:
                bot.reply_to(message, url)
                file.write(url+'\n')
                
def wiki(message):
    
    text = message.text.replace("/apa_itu ", "")
    if text:
        try:
            dpt = f'https://id.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={text}'
            hasil = requests.get(dpt).json()
            filter = hasil['query']['pages']
            d = re.findall(r'(\d+)', str(filter))
            result = filter[d[0]]['extract']
            bot.reply_to(message, f'''Pertanyaan : {text}

Jawaban : {result}''')
        except Exception as e:
            print(e)
            bot.reply_to(message, f'Maaf, Yang anda cari "{text}" tidak bisa ditemukan di wikipedia!')
            
def ytSearch(message):
    text = message.text.replace("/yt_search ","")
    video = VideosSearch(text)
    limit = 5
    hasil = video.result()
    
    for i in range(5):
        judul = hasil['result'][i]['title']
        url = hasil['result'][i]['link']
        bot.reply_to(message, f"{judul} \n\n{url}")