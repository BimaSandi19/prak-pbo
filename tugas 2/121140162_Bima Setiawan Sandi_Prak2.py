class Orang:

    def __init__(self, nama, nim, kelas_pbo_siakad, sks ):
        self.nama = nama
        self.nim = nim
        self.kelas_pbo_siakad = kelas_pbo_siakad
        self.sks = sks

    def menampilkan_data(self):
        print("Nama = ", self.nama)
        print("NIM = ", self.nim)
        print("Kelas PBO SIAKAD = ", self.kelas_pbo_siakad)
        print("Jumlah SKS = ", self.sks)

nama = input("Masukkan Nama = ")
nim =  input("Masukkan NIM = ")
kelas_pbo_siakad = input("Masukkan Kelas PBO SIAKAD = ")
sks = input("Masukkan jumlah SKS = ")

bima = Orang(nama, nim, kelas_pbo_siakad, sks)
bima.menampilkan_data()
