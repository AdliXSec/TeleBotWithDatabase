# Meminta input dari pengguna
input_string = input("Masukkan angka-angka (pisahkan dengan spasi): ")

# Membagi string menjadi potongan-potongan berdasarkan spasi
tokens = input_string.split()

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
