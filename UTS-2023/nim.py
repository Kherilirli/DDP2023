nim = int(input("Masukkan NIM:"))

if nim % 2 == 1:
    print("Menghitung Luas dan Keliling Layang")
    d1 = int(input("Masukkan diagonal 1:"))
    d2 = int(input("Masukkan diagonal 2:"))

    luas = 1/2 * d1 * d2

    sisi1 = int(input("Masukkan sisi1:"))
    sisi2 = int(input("Masukkan sisi2:"))

    keliling = 2 * (sisi1 + sisi2)

else:
    print("Menghitung Luas dan Keliling Trapesium")
    a = int(input("Masukkan sisi atas:"))
    b = int(input("Masukkan sisi bawah"))
    t = int(input("Masukkan tinggi:"))

    luas = 1/2 * (a+b) * t

    keliling = 2 * (a+b)

print(f"Luas: {luas}")
print(f"Keliling: {keliling}")