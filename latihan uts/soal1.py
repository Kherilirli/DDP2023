bensin = {
    "Pertalite" : {"harga": 10000, "jarak_tempuh": 12},
    "Pertamax" : {"harga": 14000, "jarak_tempuh": 13},
    "Pertamax Turbo" : {"harga": 17000, "jarak_tempuh": 13.5},
}

nama_kendaraan = input("Nama Kendaraan (contoh: mobil, motor): ")
jenis_bensin = input("Jenis Bensin (Pertalite, Pertamax, Pertamax Turbo): ")
kota_tujuan = input("Kota yang dituju: ")

JarakKota = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6,
}

jarak = JarakKota[kota_tujuan]
jarak_tempuh = bensin[jenis_bensin]["jarak_tempuh"]
bensin_per_km = 1 / jarak_tempuh
pemakaian_bensin = jarak * bensin_per_km
harga_per_liter = bensin[jenis_bensin]["harga"]
HargaTotal = pemakaian_bensin * harga_per_liter

# Menampilkan hasil perhitungan
print("\n--- Rincian Biaya Perjalanan ---")
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota yang dituju:", kota_tujuan)
print(f"Pemakaian bensin (liter): {pemakaian_bensin:.2f}")
print(f"Total Harga Bensin: Rp. {HargaTotal:.2f}")