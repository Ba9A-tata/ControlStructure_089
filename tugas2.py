#Masukan angka pertama
a = int(input("Masukkan Angka Pertama: "))

#Masukan angka kedua
b = int(input("Masukkan Angka Kedua: "))

#Masukan angka ke 3
c = int(input("Masukkan Angka Ketiga: "))

#Menentukan angka terbesar di antara ketiga angka 
if a >= b and a >= c:
    AngkaTerbesar = a

elif b >= a and b >= c:
    AngkaTerbesar = b

else:
    AngkaTerbesar = c

#Menampilkan angka terbesar 
print("Angka Terbesar:", AngkaTerbesar)
