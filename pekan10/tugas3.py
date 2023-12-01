def duplikasi(list_buah):
    list_hasil = []
    for buah in list_buah:
        list_hasil.extend([buah, buah])
    return list_hasil

list_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(list_buah)
print(hasil_duplikasi)