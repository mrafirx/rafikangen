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