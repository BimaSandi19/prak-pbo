import os

class AkunBank:

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.nama_pelanggan = nama_pelanggan
        self.no_pelanggan = no_pelanggan
        self.__jumlah_saldo = jumlah_saldo 

    def lihat_saldo(self):
        print(f"Saldo anda saat ini adalah : {self.__jumlah_saldo}")

    def tarik_tunai(self, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            print(f"Tarik tunai senilai {jumlah_uang} berhasil")
        else:
            print(f"Saldo tidak mencukupi!")

    def transfer(self, penerima, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            penerima.__jumlah_saldo += jumlah_uang #penambahan saldo ke rekening tujuan
            print(f"Transfer senilai {jumlah_uang} ke {penerima.nama_pelanggan} berhasil")
        else:
            print(f"Saldo tidak mencukupi!")

os.system("cls")

Akun1 = AkunBank(1221, "Bima Setiawan Sandi", 1000000000)
Akun2 = AkunBank(1121, "Marco", 7777777777)
Akun3 = AkunBank(1234, "James", 8888888888)

base_akun = [Akun1, Akun2, Akun3]

while True:
    print("Selamat datang di Bank Sky")
    print(f"""Halo {Akun1.nama_pelanggan}, ingin melakukan transaksi apa?
    1. Lihat saldo
    2. Tarik tunai
    3. Transfer saldo
    4. Keluar""")
    masukan = int(input("Masukkan nomor input: "))

    if (masukan == 1):
        Akun1.lihat_saldo()

    elif(masukan == 2):
        jumlah_tarik = int(input("Masukan jumlah tarik tunai : "))
        Akun1.tarik_tunai(jumlah_tarik)

    elif(masukan == 3):
        jumlah_transfer = int(input("Masukan jumlah uang yang ingin ditranfer : "))
        no_tujuan = int(input("Masukan no pelanggan tujuan : "))
        for akun_tujuan in base_akun:
            if akun_tujuan.no_pelanggan == no_tujuan:
                Akun1.transfer(akun_tujuan, jumlah_transfer)

    elif(masukan == 4):
        break

    print("\n")



     