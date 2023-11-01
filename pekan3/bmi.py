tinggi = int(input("Masukan tinggi badan Anda:"))

# untuk laki-laki
beratL = int((tinggi - 100) - (tinggi - 100) * 0.1)


# untuk perempuan
beratP = (tinggi - 100) - (tinggi - 100) * 0.15

print("Berat badan ideal laki-laki", beratL, "kg")
print("Berat badan ideal perempuan", beratP, "kg")