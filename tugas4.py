def print_odd_numbers(n):
    # Looping dari 1 hingga n
    for i in range(1, n + 1):
        # Jika i adalah angka ganjil, cetak i
        if i % 2 != 0:
            print(i)

# Input nilai n dari user
n = int(input("Enter the value of n: "))

# Cetak judul
print("Odd numbers up to", n, "are:")

# Cetak hasil angka ganjil
print_odd_numbers(n)