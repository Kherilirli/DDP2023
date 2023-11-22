angka1 = int(input("Masukkan angka 1:"))
angka2 = int(input("Masukkan angka 2:"))
operator = input("Pilih operator (+,-,*,/,**):")

if operator == '+':
    hasil =  int(angka1 + angka2)
    operasi = "tambah"

elif operator == '-':
    hasil = int(angka1 - angka2)
    operasi = "kurang"

elif operator == '*':
    hasil = int(angka1 * angka2)
    operasi = "kali"

elif operator == '/':
    if angka2 != 0:
        hasil = int(angka1 / angka2)
        operasi = "bagi"

    else:
        hasil = int("underfined (pembagian oleh 0)")
        operasi = "bagi"

elif operator == '**':
    hasil = int(angka1 ** angka2)
    operasi = "pangkat"

else:
    hasil = "operator tidal valid"
    operator = "Tidak Valid"

print("---Hasil perhitungan tambah diatas adalah---",)
print("Angka pertama:", angka1)
print("Angka kedua:", angka2)
print("Pilih Operator:", operasi)
print("Hasil Operator:", angka1, operator, angka2,"adalah", hasil)
