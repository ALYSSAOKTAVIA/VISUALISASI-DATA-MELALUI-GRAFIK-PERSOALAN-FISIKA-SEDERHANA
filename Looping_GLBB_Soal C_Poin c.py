import matplotlib.pyplot as plt

#Parameter gerak benda
percepatan = 2 #percepatan konstan dalam meter per detik kuadrat
waktu_total = 100 # waktu dalam detik

# Variabel untuk menyimpan data waktu dan posisi
waktu = []
posisi = []

# Loop untuk menghitung posisi setiap detik 
for t in range(waktu_total + 1):
    x = (1/2) * percepatan * t**2 #posisi benda pada waktu t
    waktu.append(t)
    posisi.append(x)

# Plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='r', linestyle='-')
plt.title("Grafik Gerak Benda dengan Percepatan Konstan")
plt.xlabel("Waktu (detik)")
plt.ylabel("Posisi (meter)")
plt.grid(True)
plt.show()