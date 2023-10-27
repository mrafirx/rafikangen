# JUDUL: TUGAS BESAR PENGKOM SEMESTER 1
# Anggota Kelompok
# 1. Muhammad Rafi Ramadhan - 19623288
# 2. Muhammad Omar Berliansyah - 19623295
# 3. Muammar Qaddafi - 16523029
# 4. Azizah Savira Mecca - 16523183
# 5. Tita Athalia Cahyadewi - 16523225

# Kamus
# Ini isinya fungsi
# Library yang diperlukan:
import math
import random

# 1 - Scan Masuk

def scanMasuk(kodeMasuk, terbacaMasuk):
    # Cek apakah kode kartu valid
    kodeHurufResmi = ["A", "B", "C"]
    kodeAngkaResmi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(kodeMasuk) == 4 and kodeMasuk[0] in kodeHurufResmi and kodeMasuk[1] in kodeAngkaResmi and kodeMasuk[2] in kodeAngkaResmi and kodeMasuk[3] in kodeAngkaResmi:
        terbacaMasuk = True

    return terbacaMasuk
# scan()

# 2 - Cek Saldo Masuk

def cekSaldoMasuk(saldo, hargaTol):
    if saldo < hargaTol:
        print("Peringatan! Saldo Anda tidak cukup untuk perjalanan di tol ini")
        print("Apakah Anda ingin mengisi disini? [Y/T]")
        isiMasuk = str(input("Pilih: "))
        if isiMasuk == "y" or isiMasuk == "Y":
            print("Anda memutuskan untuk mengisi saldo disini...")
            saldo += int(input("Masukkan jumlah top-up saldo: "))
            print ("Selamat menikmati perjalanan!")
        else:
            print("Jangan lupa mengisi saldo di perjalanan!: ")
    else:
        print("Saldo Anda mencukupi! Selamat menikmati perjalanan")
    
    print(f"Saldo anda saat ini: {saldo}")

# 3 - Rest Area
def restArea(saldo):
    print("Rest Area sudah dekat, apakah Anda ingin mengunjunginya dan mengisi ulang saldo? [Y/T]")
    kunjungi = str(input("Pilih: "))
    if kunjungi == "y" or kunjungi == "Y":
        isiUlang = int(input("Berapa saldo yang ingin Anda isi ulang? "))
    else:
        print("Anda melanjutkan perjalanan")
        isiUlang = 0
    saldo += isiUlang
    return saldo

# 4 - Scan Keluar
def scanKeluar(kodeKeluar, terbacaKeluar):
    # Cek apakah kode kartu valid
    kodeHurufResmi = ["A", "B", "C"]
    kodeAngkaResmi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(kodeKeluar) == 4 and kodeKeluar[0] in kodeHurufResmi and kodeKeluar[1] in kodeAngkaResmi and kodeKeluar[2] in kodeAngkaResmi and kodeKeluar[3] in kodeAngkaResmi:
        terbacaKeluar = True

    return terbacaKeluar

# 5 - Saldo Keluar
def cekSaldoKeluar(saldo, hargaTol):
    if saldo < hargaTol:
        saldoKurang = True
    else:
        saldoKurang = False
    return saldoKurang
        # print("Saldo Anda kurang dan Anda memanggil petugas")
        # isiUlang = hargaTol - saldo
        # print(f"Anda mengisi saldo sebanyak Rp{isiUlang} untuk membayar tol")

# 6 - Cek Timeout
def cekTimeout(durasiMasuk, durasiKeluar, jumlahRestArea):
    durasiMaksimal = jumlahRestArea * 60
    durasiTotal = durasiKeluar - durasiMasuk
    if durasiTotal > durasiMaksimal:
        timeout = True
    else:
        timeout = False
    return timeout

timeout = cekTimeout(durasiMasuk=60, durasiKeluar=120, jumlahRestArea=1)
if timeout == True:
    print("A")
else:
    print("B")

# ALGORITMA

# # 1 - Masuk Tol
print("Anda merasa bosan dengan kehidupan di kota...")

gambarKota = '''                       .|
                       | |
                       |'|            ._____
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____'''
# Art by Joan Stark, taken from https://www.asciiart.eu/buildings-and-places/cities

print(gambarKota)
print("")

gambarJalan = '''
                 __
               .'/\'.
             .'-/__\-'.
           .'--/____\--'.
         .'--./______\.--'.
       .'--../________\..--'.
     .'--.._/__________\_..--'.
   .'--..__/____________\__..--'.
 .'--..___/______________\___..--'.
'========'================'========' '''
# Art by Igbeard, taken from https://www.asciiart.eu/buildings-and-places/other

print("Akhirnya Anda pun memutuskan untuk bepergian melalui jalan tol...")
print("")
print(gambarJalan)
print(" ")

# 2 - Selamat Datang di Tol Cisantuy
print("Selamat datang di Tol Cisantuy!")
cisantuy = '''

.___________.  ______    __      
|           | /  __  \  |  |     
`---|  |----`|  |  |  | |  |     
    |  |     |  |  |  | |  |     
    |  |     |  `--'  | |  `----.
    |__|      \______/  |_______|
                                 

  ______  __       _______.     ___      .__   __. .___________. __    __  ____    ____ 
 /      ||  |     /       |    /   \     |  \ |  | |           ||  |  |  | \   \  /   / 
|  ,----'|  |    |   (----`   /  ^  \    |   \|  | `---|  |----`|  |  |  |  \   \/   /  
|  |     |  |     \   \      /  /_\  \   |  . `  |     |  |     |  |  |  |   \_    _/   
|  `----.|  | .----)   |    /  _____  \  |  |\   |     |  |     |  `--'  |     |  |     
 \______||__| |_______/    /__/     \__\ |__| \__|     |__|      \______/      |__|     
                                                                                        

'''
# Generated from https://patorjk.com/
print(cisantuy)

# 3 - Scan Kartu Masuk (Scan Kartu 1)
print("Format kode kartu Tol adalah 1 huruf kapital diikuti 3 angka")
print("Contoh: A000")
print("")
kodeMasuk = str(input("Masukkan kode kartu Tol: "))
terbacaMasuk = False

kodeHurufResmi = ["A", "B", "C"]
kodeAngkaResmi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
terbacaMasuk = scanMasuk(kodeMasuk, terbacaMasuk)
print(kodeMasuk)

if terbacaMasuk == False:
    # Jika kartu tidak valid: beli kartu baru
    print("Kartu tidak terbaca!")
    print("Anda pun memanggil petugas")
    print("Petugas datang dan Anda harus memberi kartu baru seharga Rp100.000")
    print("Saldo dalam kartu tersebut adalah Rp50.000")
    saldo = 50000
    kodeMasuk = ["" for i in range (4)]
    kodeMasuk[0] = random.choice(kodeHurufResmi)
    kodeMasuk[1] = random.choice(kodeAngkaResmi)
    kodeMasuk[2] = random.choice(kodeAngkaResmi)
    kodeMasuk[3] = random.choice(kodeAngkaResmi)
else:
    print("Kartu terbaca!")
print("")

print("-----------------------------------------------------------------")
print("Berikut informasi kartu Anda:")
print("Kode Kartu: ", end="")
for i in range (4):
    print(kodeMasuk[i], end="")
print()

# 4 - Cek Saldo Masuk (Cek Saldo 1)
if terbacaMasuk == True:
    saldo = int(input("Masukkan jumlah saldo Anda: "))

print("-----------------------------------------------------------------")
print("Harga tol ini adalah Rp15.000!")
hargaTol = 15000
print(f"Saldo: Rp{saldo}")
cekSaldoMasuk(saldo, hargaTol)
print("-----------------------------------------------------------------")

# 5 - Input Waktu Masuk
print("")
print("Masukkan waktu masuk tol!")
waktuMasuk = [0, 0]
waktuMasuk[0] = int(input("Masukkan jam: "))
waktuMasuk[1] = int(input("Masukkan menit: "))

# Mengolah waktu masuk ke dalam menit
durasiMasuk = waktuMasuk[0] * 60 + waktuMasuk[1]
print("-----------------------------------------------------------------")

# 6 - Palang Terbuka
print("Palang gerbang tol pun terbuka dan perjalanan dimulai...")
selamatJalan = '''

     _______. _______  __          ___      .___  ___.      ___   .___________.          __       ___       __          ___      .__   __. 
    /       ||   ____||  |        /   \     |   \/   |     /   \  |           |         |  |     /   \     |  |        /   \     |  \ |  | 
   |   (----`|  |__   |  |       /  ^  \    |  \  /  |    /  ^  \ `---|  |----`         |  |    /  ^  \    |  |       /  ^  \    |   \|  | 
    \   \    |   __|  |  |      /  /_\  \   |  |\/|  |   /  /_\  \    |  |        .--.  |  |   /  /_\  \   |  |      /  /_\  \   |  . `  | 
.----)   |   |  |____ |  `----./  _____  \  |  |  |  |  /  _____  \   |  |        |  `--'  |  /  _____  \  |  `----./  _____  \  |  |\   | 
|_______/    |_______||_______/__/     \__\ |__|  |__| /__/     \__\  |__|         \______/  /__/     \__\ |_______/__/     \__\ |__| \__| 
                                                                                                                                           
'''
# Generated from https://patorjk.com/
print(selamatJalan)

# 7 - RNG Rute Rest Area
# Menentukan jumlah rest area yang akan ditemui selama perjalanan secara acak
kemungkinanRestArea = [1, 2, 3]
jumlahRestArea = random.choice(kemungkinanRestArea)


# 8 - Rest Area
gambarRestArea = '''

.______       _______     _______.___________.        ___      .______       _______     ___                                             
|   _  \     |   ____|   /       |           |       /   \     |   _  \     |   ____|   /   \                                            
|  |_)  |    |  |__     |   (----`---|  |----`      /  ^  \    |  |_)  |    |  |__     /  ^  \                                           
|      /     |   __|     \   \       |  |          /  /_\  \   |      /     |   __|   /  /_\  \                                          
|  |\  \----.|  |____.----)   |      |  |         /  _____  \  |  |\  \----.|  |____ /  _____  \                                         
| _| `._____||_______|_______/       |__|        /__/     \__\ | _| `._____||_______/__/     \__\                                        
                                                                                                                                         
  _______  __   __          ___      .__   __.   _______      _______  _______ .___  ___.  __   __          ___      .__   __.   _______ 
 /  _____||  | |  |        /   \     |  \ |  |  /  _____|    /  _____||   ____||   \/   | |  | |  |        /   \     |  \ |  |  /  _____|
|  |  __  |  | |  |       /  ^  \    |   \|  | |  |  __     |  |  __  |  |__   |  \  /  | |  | |  |       /  ^  \    |   \|  | |  |  __  
|  | |_ | |  | |  |      /  /_\  \   |  . `  | |  | |_ |    |  | |_ | |   __|  |  |\/|  | |  | |  |      /  /_\  \   |  . `  | |  | |_ | 
|  |__| | |  | |  `----./  _____  \  |  |\   | |  |__| |    |  |__| | |  |____ |  |  |  | |  | |  `----./  _____  \  |  |\   | |  |__| | 
 \______| |__| |_______/__/     \__\ |__| \__|  \______|     \______| |_______||__|  |__| |__| |_______/__/     \__\ |__| \__|  \______| 
                                                                                                                                         

'''
# Generated from https://patorjk.com/

for i in range (0, jumlahRestArea):
    print(gambarRestArea)
    saldo += restArea(saldo)

# 9 - Perjalanan akan berakhir segera
print("Perlanan akan segera selesai...")

# 10 - Scan Kartu Keluar (Scan Kartu 2)
print("Format kode kartu Tol adalah 1 huruf kapital diikuti 3 angka")
print("Contoh: A000")
print("")
kodeKeluar = str(input("Masukkan kode kartu Tol: "))
terbacaKeluar = False

kodeHurufResmi = ["A", "B", "C"]
kodeAngkaResmi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
terbacaKeluar = scanKeluar(kodeKeluar, terbacaKeluar)

# 11 - Cek Kartu Bermasalah
if kodeMasuk != kodeKeluar or terbacaKeluar == False:
    bermasalah = True
else:
    bermasalah = False

# 12 - Cek Saldo Keluar (Cek Saldo 2)
if bermasalah == False:
    saldoKurang = cekSaldoKeluar(saldo, hargaTol)

# 13 - Cek Timeout
waktuKeluar = [0, 0]
waktuKeluar[0] = int(input("Masukkan jam keluar: "))
waktuKeluar[1] = int(input("Masukkan menit keluar: "))
durasiKeluar = (waktuKeluar[0] * 60) + waktuKeluar[1]

timeout = cekTimeout(durasiMasuk, durasiKeluar, jumlahRestArea)

# 14 - Perjalanan Selesai
if bermasalah == True:
    print("Ending 1: Kartu bermasalah. Panggil petugas, bayar denda, dan keluar")
elif bermasalah == False:
    if saldoKurang == True:
        if timeout == True:
            print('''Ending 2: Saldo kurang dan timeout. Panggil petugas untuk bayar 
                  kekurangan saldo dan meminta dibukakan gerbang karena timeout''')
        elif timeout == False:
            print('''Ending 3: Saldu kurang tapi tidak timeout.
                  Panggil petugas untuk bayar kekurangan saldo''')
    elif saldoKurang == False:
        if timeout == True:
            print('''Ending 4: Timeout saja. Panggil petugas untuk membukakan gerbang''')
        elif timeout == False:
            print('''Ending 5 (True Ending): Tidak ada masalah selama perjalanan
                  sampai jumpa lagi di tol berikutnya ^-^ ''')
            
simulasiSelesai = '''

     _______. __  .___  ___.  __    __   __          ___           _______. __  
    /       ||  | |   \/   | |  |  |  | |  |        /   \         /       ||  | 
   |   (----`|  | |  \  /  | |  |  |  | |  |       /  ^  \       |   (----`|  | 
    \   \    |  | |  |\/|  | |  |  |  | |  |      /  /_\  \       \   \    |  | 
.----)   |   |  | |  |  |  | |  `--'  | |  `----./  _____  \  .----)   |   |  | 
|_______/    |__| |__|  |__|  \______/  |_______/__/     \__\ |_______/    |__| 
                                                                                
     _______. _______  __       _______     _______.     ___       __           
    /       ||   ____||  |     |   ____|   /       |    /   \     |  |          
   |   (----`|  |__   |  |     |  |__     |   (----`   /  ^  \    |  |          
    \   \    |   __|  |  |     |   __|     \   \      /  /_\  \   |  |          
.----)   |   |  |____ |  `----.|  |____.----)   |    /  _____  \  |  |          
|_______/    |_______||_______||_______|_______/    /__/     \__\ |__|          
                                                                                

'''
# Generated from https://patorjk.com/
print(simulasiSelesai)