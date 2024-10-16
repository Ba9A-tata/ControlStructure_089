#Mencetak desain
def print_design(n):
    # Looping dari 1 hingga n
    for i in range(1, n + 1):
        # Looping dari 0 hingga i
        for j in range(i):
            # Cetak i
            print(i, end=" ")
        # Cetak baris baru
        print()

# Input nilai n dari user
n = int(input("Enter the value of n: "))

# Cetak hasil desain
print_design(n)
