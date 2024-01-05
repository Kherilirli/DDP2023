from tkinter import *
from ttkbootstrap import ttk

#
root = Tk()

root.geometry('500x500')

root.title("Aplikasi Penghitung Luas Segitiga")

ttk.Label(root, text="Aplikasi Penghitung Luas Segitiga", font=('calibri', 15, 'bold')).pack(pady=9)

ttk.Label(root, text="Masukkan alas:").pack(pady=5)

alas = Entry()
alas.insert(END, 0)
alas.pack()

ttk.Label(root, text="Masukkan tinggi:").pack(pady=5,)

tinggi = Entry()
tinggi.insert(END, 0)
tinggi.pack()

def hitung():
    hasil_alas = int(alas.get())
    hasil_tinggi = int(tinggi.get())
    
    luas = 0.5 * hasil_alas * hasil_tinggi

    hasil = f"Hasil perhitungan luas adalah: {luas}"
    ttk.Label(root, text=hasil).pack()

ttk.Button(root, text="Hitung",command=hitung).pack()

root.mainloop()