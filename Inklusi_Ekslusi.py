from matplotlib_venn import venn3
import matplotlib.pyplot as plt

kopi = 50
teh = 30
susu = 20
kopi_teh = 15
kopi_susu = 10
teh_susu = 5
kopi_teh_susu = 3
total_orang = 100

suka_minimal_satu = (kopi + teh + susu - kopi_teh - kopi_susu - teh_susu + kopi_teh_susu)
tidak_suka_apapun = total_orang - suka_minimal_satu

print("\nHasil Perhitungan :")
print("-" * 33)
print(f"Total orang yang disurvei : {total_orang}")
print(f"Suka minimal satu minuman : {suka_minimal_satu}")
print(f"Tidak suka minuman apapun : {tidak_suka_apapun}")
print("-" * 33)

hanya_kopi = kopi - kopi_teh - kopi_susu + kopi_teh_susu
hanya_teh = teh - kopi_teh - teh_susu + kopi_teh_susu
hanya_susu = susu - kopi_susu - teh_susu + kopi_teh_susu

hanya_kopi_teh = kopi_teh - kopi_teh_susu
hanya_kopi_susu = kopi_susu - kopi_teh_susu
hanya_teh_susu = teh_susu - kopi_teh_susu
ketiganya = kopi_teh_susu

venn3(subsets=(
    hanya_kopi,         
    hanya_teh,         
    hanya_susu,         
    hanya_kopi_teh,    
    hanya_kopi_susu,   
    hanya_teh_susu,     
    ketiganya          
), set_labels=('Kopi', 'Teh', 'Susu'))

plt.title("Diagram Venn Penyuka Minuman")
plt.show()
