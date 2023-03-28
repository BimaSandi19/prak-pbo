class Produk:
    def __init__(self, nama, harga, deskripsi):
        self.nama = nama
        self.harga = harga
        self.deskripsi = deskripsi
        
    def __str__(self):
        return f"{self.nama} ({self.deskripsi}) : Rp {self.harga}"
        

class Makanan(Produk):
    def __init__(self, nama, harga, deskripsi, kalori):
        super().__init__(nama, harga, deskripsi)
        self.kalori = kalori
        
    def __str__(self):
        return f"{super().__str__()} ({self.kalori} kalori)"
        

class Minuman(Produk):
    def __init__(self, nama, harga, deskripsi, ukuran):
        super().__init__(nama, harga, deskripsi)
        self.ukuran = ukuran
        
    def __str__(self):
        return f"{super().__str__()} ({self.ukuran} ml)"
        

class BarangLainnya(Produk):
    pass
    

class KeranjangBelanja:
    def __init__(self):
        self.daftar_produk = []
        self.total_belanja = 0
        
    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        self.total_belanja += produk.harga
        
    def __str__(self):
        output = "Daftar belanja: \n"
        for produk in self.daftar_produk:
            output += f"- {produk}\n"
        output += f"Total belanja: Rp {self.total_belanja}"
        return output

# membuat objek produk
makanan1 = Makanan("Nasi goreng", 15000, "Nasi goreng dengan bumbu rempah", 500)
minuman1 = Minuman("Teh botol", 5000, "Teh siap minum", 250)
barang1 = BarangLainnya("Tas", 200000, "Tas ransel untuk laptop")

# membuat objek keranjang belanja
keranjang = KeranjangBelanja()

