import matplotlib.pyplot as plt

#Parameter gerak benda
percepatan = 2.25 #percepatan konstan dalam meter per detik kuadrat
waktu_total = 20 # waktu dalam detik
kecepatan_awal = 60 # kecepatan awal dalam meter per detik

# Variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# Loop untuk menghitung posisi setiap detik 
for t in range(waktu_total + 1):
    x = kecepatan_awal * t - (1/2) * percepatan * t**2 #posisi benda pada waktu t
    waktu.append(t)
    posisi.append(x)

# Plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='purple', linestyle='-')
plt.title("Grafik Gerak Benda dengan Kecepatan Konstan")
plt.xlabel("Posisi (x)")
plt.ylabel("Waktu (t)")
plt.grid(True)
plt.show()