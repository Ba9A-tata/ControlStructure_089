n = int(input("Masukkan nilai n: "))
a, b = 0, 1

#Daftar kosong untuk menyimpan hasil deret Fibonacci
hasil = []

#Untuk menghasilkan deret Fibonacci hingga n angka
for i in range(n):
    # Menambahkan angka saat ini (a) ke daftar hasil
    hasil.append(a)
    
    # Mengupdate nilai a dan b untuk langkah berikutnya dalam deret Fibonacci
    a, b = b, a + b

#Menampilkan deret Fibonacci 
print("Deret Fibonacci hingga", n, ":", hasil)