class Hewan:
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = cara_berkembang_biak

    def info(self):
        print("="*20)
        print("Animal Information")
        print("Nama     \t:", self.nama)
        print("Makanan \t:", self.makanan)
        print("Hidup    \t:", self.habitat)
        print("Berkembang Biak :", self.berkembang_biak)
        print("="*20)

class Badak(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, panjang_cula, warna_kulit):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)


class Ikan(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, ukuran_sirip, warna_sisik):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)


class Ular(Hewan):
    def __init__(self, nama, makanan, habitat, cara_berkembang_biak, panjang_tubuh, berbisa):
        super().__init__(nama, makanan, habitat, cara_berkembang_biak)
        self.panjang_tubuh = panjang_tubuh
        self.berbisa = berbisa


badak = Badak("Badak Jawa", "Rumput", "Daratan", "Vivipar", 50, "Coklat")
ikan = Ikan("Nemo", "Plankton", "Air", "Ovipar", "Kecil", "Warna-warni")
ular = Ular("Kobra", "Hewan kecil", "Daratan", "Ovipar", 3, True)

badak.info()
ikan.info()
ular.info()