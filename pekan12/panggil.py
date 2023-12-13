from gempa import *

gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Memanggil fungsi dampak untuk setiap objek
hasil_dampak1 = gempa1.dampak()
hasil_dampak2 = gempa2.dampak()
hasil_dampak3 = gempa3.dampak()
hasil_dampak4 = gempa4.dampak()
hasil_dampak5 = gempa5.dampak()

# Menampilkan hasil dampak
print(hasil_dampak1)
print(hasil_dampak2)
print(hasil_dampak3)
print(hasil_dampak4)
print(hasil_dampak5)