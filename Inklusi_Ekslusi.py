import matplotlib.pyplot as plt
from matplotlib_venn import venn3  

def hitung_tidak_suka():
    total_orang = 100
    kopi = 50
    teh = 30
    susu = 20
    kopi_teh = 15
    kopi_susu = 10
    teh_susu = 5
    semua = 3

    suka_minuman = (kopi + teh + susu) - (kopi_teh + kopi_susu + teh_susu) + semua
    tidak_suka = total_orang - suka_minuman
    return tidak_suka

def gambar_venn():
    plt.figure(figsize=(6, 6))
    venn3(subsets=(50, 30, 20, 15, 10, 5, 3), set_labels=('Kopi', 'Teh', 'Susu'))
    plt.title("Diagram Venn \n Konsumsi Minuman")

    # Menampilkan jumlah orang yang tidak suka minuman apa pun
    plt.text(0.3, -0.6, f"Tidak suka minuman: {hitung_tidak_suka()}", fontsize=11, color="black")
    plt.show()

# Tampilkan diagram
gambar_venn()
