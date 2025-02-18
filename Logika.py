# P = True
# Q = False

# negasi = not P 
# print("Nilai negasi P adalah", negasi)

# negasi = not Q 
# print("Nilai negasi Q adalah", negasi)

# konjungsi = P and Q
# print("Nilai P konjungsi Q adalah", konjungsi)

# disjungsi = P or Q
# print("Nilai P dijungsi Q adalah", disjungsi)

# Exclusive_OR_XOR = P ^ Q
# print("\n Nilai P exclusive or Q adalah", Exclusive_OR_XOR)

# menampilkan/membuat judul tabel
print("-------------------------------")
print(">> TABEL KEBENARAN KONJUNGSI <<")
print("-------------------------------")

# menampilka header tabel
print("| P\t| Q\t| P AND Q |")
print("-------------------------------")

# menggunakan operator logika 'AND'
for P in [True, False]:                       # loop ke 1 untuk P
    for Q in [True, False]:                   # loop ke 2 untuk Q
        konjungsi = P and Q                   # melakukan operasi P AND Q
        print(f"{P}\t{Q}\t{konjungsi}")       # mencetak hasil
print("-------------------------------")

# menampilka header tabel
print("-------------------------------")
print(">> TABEL KEBENARAN KONJUNGSI <<")
print("-------------------------------")

print("| P\t| Q\t| P OR Q |")
print("-------------------------------")

# menggunakan operator logika 'OR'
for P in [True, False]:                       # loop ke 1 untuk P
    for Q in [True, False]:                   # loop ke 2 untuk Q
        disjungsi = P or Q                    # melakukan operasi P OR Q
        print(f"{P}\t{Q}\t{disjungsi}")       # mencetak hasil
print("------------------------------")


print(">>  TABEL KEBENARAN NEGASI  <<")
print("------------------------------")
print("| P\t| Q\t| -P OR Q |")
print("------------------------------")

# menggunakan operator logika 'negasi'
for P in [True, False]:                         # loop ke 1 untuk P
    for Q in [True, False]:                     # loop ke 2 untuk Q
        negasi = not P or Q                     # melakukan operasi Negasi P OR Q
        print(f"{P}\t{Q}\t{negasi}")            # mencetak hasil
print("------------------------------")
