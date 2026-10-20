# total = 0

# for angka in range(1,20,2):
#     total += angka

# if angka ==19:
#       print(angka, end="=")
#         else:
#            print(angka, end="+")

# print(total)

baris = int(input("Masukkan jumlah baris: "))

for i in range(1, baris + 1):
    print("*" * i)