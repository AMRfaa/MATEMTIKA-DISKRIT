# # input bilangan desimal
angka = int(input("Masukkan bilangan: "))

# konversi desimal ke biner
print (f"Biner          : {bin(angka)}")
# konversi desimal ke oktal
print (f"Oktal          : {oct(angka)}")
# konversi desimal ke heksadesimal
print (f"Heksadesimal   : {hex(angka)}")

# input bilangan biner
biner = input("Masukkan bilangan biner: ")

# konversi biner ke desimal
desimal = int(biner, 2)

# konversi biner ke desimal
print("Desimal     :", desimal)
# konversi biner ke oktal
print("Oktal       :", oct(desimal))
# konversi biner ke heksadesimal
print("Heksadesimal:", hex(desimal))
