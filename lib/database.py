import mysql.connector
from telebot import *
from config.confff import api
# from telebot import types, TeleBot
bot = TeleBot(api)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='telegram'
)

print(db)
sql = db.cursor()

def notif(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    id_telegram = message.from_user.id
    username = message.from_user.username
    message = message
    
    query_p = f"SELECT id_user_tele,username_user_tele,nama_user_tele FROM user_tele WHERE id_user_tele='{id_telegram}'"
    sql.execute(query_p)
    result = sql.fetchall()
    
    pesan = ''
    for data in result:
        pesan = pesan + str(data) + '\n'
    if str(id_telegram) in pesan:
        # lakukan sesuatu 
        # print("Sesuatu")
        
        query_u = "UPDATE user_tele SET notif_user_tele = %s WHERE id_user_tele = %s"
        inpq =  ("aktif", id_telegram)
        sql.execute(query_u, inpq)
        db.commit()
        bot.reply_to(message, f'Selamat kepada {first_name} notifikasi telah di aktifkan, jika ada update tools atau waktu pengingat akan di beri tahu')
    else:
        bot.reply_to(message, "Maaf tidak dapat mengaktifkan notifikasi, pastikan akun anda telah melakukan registrasi, dengan cara menekan /register")

def register_tele(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    id_telegram = message.from_user.id
    username = message.from_user.username
    message = message
    
    query_a = f"SELECT id_user_tele,username_user_tele,nama_user_tele FROM user_tele WHERE id_user_tele='{id_telegram}'"
    sql.execute(query_a)
    result = sql.fetchall()
    
    pesan = ''
    for data in result:
        pesan = pesan + str(data) + '\n'
    if str(id_telegram) in pesan:
        print(pesan)
        bot.send_message(id_telegram, '''
Kamu Telah Registrasi, tidak dapat registrasi kembali

Nama = {}
Username = {}
ID = {}

Jika ingin menghapus data registrasi kamu silahkan ketik
/deleteregister'''.format(first_name, username, id_telegram))
    else:
        query = "INSERT INTO user_tele (id_user_tele, username_user_tele, nama_user_tele, notif_user_tele) VALUES (%s, %s, %s, %s)"
        dlix = (id_telegram, username, first_name, "nonaktif")
        sql.execute(query, dlix)
        db.commit()
    
        bot.send_message(id_telegram, '''
Selamat, Kamu Berhasil Registrasi

Hi, ini Data Telegram kamu
Nama = {}
Username = {}
ID = {}

Jika ingin menghapus data registrasi kamu silahkan ketik
/deleteregister
'''.format(first_name, username, id_telegram))

def hapus_data(message):
    # def konfirmasi_hapus(message):
    #     if message.text == 'Iya':
            
    #             # hapus data dari tabel user_tele berdasarkan ID dari user tele
    sqll = "DELETE FROM user_tele WHERE id_user_tele = '%s'"
    val = (message.from_user.id, )
    sql.execute(sqll, val)
    db.commit()
                    
    bot.reply_to(message, 'Data berhasil dihapus.')
            
                
    #     elif message.text == 'Tidak':
    #         bot.reply_to(message, 'Penghapusan data dibatalkan.')   
    # chat_type = message.chat.type
    
    # if chat_type == 'private':
    #     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    #     markup.add('Iya', 'Tidak')
    #     msg = bot.reply_to(message, 'Apakah Anda yakin ingin menghapus data?', reply_markup=markup)
    #     bot.register_next_step_handler(msg, konfirmasi_hapus)
        
    # elif chat_type == 'group':
    #     bot.reply_to(message, 'Perintah ini hanya bisa digunakan di private chat.')   
      

