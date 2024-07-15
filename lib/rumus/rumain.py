from telebot import *
from config.confff import api

bot = TeleBot(api)

def suhu(message):
    suhu = message.text.replace("/konversi_suhu ", "")
    nilai = ['celsius', 'fahrenheit', 'kelvin', 'reamur', 'Celsius', 'Fahrenheit', 'Kelvin', 'Reamur']
    
    if "celsius" in suhu:
        cels = suhu.replace("celsius ", "")
        cels = float(cels)
        
        fahr = (9/5 * cels) + 32
        kelv = cels + 273.15
        ream = cels * (4/5)
        
        bot.reply_to(message, f'''suhu = {cels} celsius

{cels} derajat celsius = {fahr} derajat Fahrenheit
{cels} derajat celcius = {kelv} derajat Kelvin
{cels} deraajt celcius = {ream} derajat Reamur''')
        
    elif "fahrenheit" in suhu:
        fahr = suhu.replace("fahrenheit ", "")
        fahr = float(fahr)
        
        cels = (fahr - 32) * 9/5