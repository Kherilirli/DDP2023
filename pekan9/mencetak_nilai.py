def cari_ganjil(batas):
    for i in range(batas + 1):
        if i % 2 != 0:
            print("Angka ganjil ditemukan:", i)
            
cari_ganjil(100)